import json
from urllib.error import URLError
from urllib.parse import quote_plus
from urllib.request import urlopen

from election_assistant.models import UserProfile

FAQ_TOPICS = {
    "registration": "Registration means getting on your state's voter rolls before the deadline. If your state offers same-day registration, check exact rules and required documents.",
    "id requirements": "ID rules vary by state. Check your official state election website for accepted photo/non-photo IDs and alternatives.",
    "mail ballot rules": "Mail ballots often require strict steps like signatures, sealed envelopes, and specific return deadlines. Follow your ballot packet instructions exactly.",
    "polling place": "Your polling place may change between elections. Confirm your location and hours through your local election office.",
    "issue help": "If you have issues, ask poll workers for assistance, request a provisional ballot if needed, and contact your local election office immediately.",
}

TOPIC_KEYWORDS = {
    "registration": ["registration", "register", "registering", "voter rolls"],
    "id requirements": ["id", "identification", "photo id", "driver's license", "license"],
    "mail ballot rules": ["mail", "absentee", "mail ballot", "absentee ballot", "drop box", "postmark", "signature"],
    "polling place": ["poll", "polling", "location", "where do i vote", "where can i vote"],
    "issue help": ["issue", "problem", "help", "support", "provisional", "rejected", "contest"],
}

ELECTION_KEYWORDS = [
    "elect", "vote", "voting", "ballot", "registration", "poll", "polling", "voter",
    "id", "identification", "absentee", "mail ballot", "early voting", "deadline",
    "precinct", "provisional", "signature", "drop box", "county election", "state election",
    "election office", "poll worker", "voter registration",
]


def answer_topic(topic: str) -> str:
    normalized = topic.strip().lower()
    return FAQ_TOPICS.get(
        normalized,
        "I can help with: registration, ID requirements, mail ballot rules, polling place, or issue help.",
    )


def search_web(query: str) -> str:
    encoded = quote_plus(query)
    url = f"https://api.duckduckgo.com/?q={encoded}&format=json&no_html=1&skip_disambig=1"
    try:
        with urlopen(url, timeout=8) as response:
            data = json.load(response)
    except (URLError, ValueError, OSError):
        return ""

    # Try various fields for answers
    for field in ["AbstractText", "Definition", "Answer"]:
        if text := data.get(field):
            return text

    related = data.get("RelatedTopics")
    if isinstance(related, list) and related:
        for item in related:
            if isinstance(item, dict):
                if text := item.get("Text"):
                    return text

    return ""


def answer_question(question: str, profile: UserProfile | None = None) -> str:
    normalized = question.strip().lower()
    if not normalized:
        return (
            "Ask me anything about voting: registration, ID requirements, mail ballots, polling places, "
            "or how to get help if something goes wrong."
        )

    if not any(keyword in normalized for keyword in ELECTION_KEYWORDS):
        return (
            "I am an election process assistant and don't have any input for this question. "
            "Please ask something about voting, registration, ballots, polling, or election deadlines."
        )

    search_result = search_web(question)
    if search_result:
        return f"Web answer: {search_result}"

    if "deadline" in normalized:
        answer = (
            "Election deadlines vary by state. Check your official state election website for exact registration, "
            "absentee ballot, and early voting deadlines."
        )
        if profile and profile.state:
            answer += f" For {profile.state}, search for '{profile.state} voter registration deadline' on your state election site."
        return answer

    if "where" in normalized and "vote" in normalized:
        answer = (
            "Your polling place and voting options depend on your state and county. Visit your state's election website "
            "or your local election office to confirm your exact voting location."
        )
        if profile and profile.state:
            answer += f" In {profile.state}, use your county election website for the most accurate polling place details."
        return answer

    # If no web result and no specific match, provide general guidance
    return (
        "No web result found. I can help with registration, ID requirements, mail ballot rules, polling places, "
        "or issue help. Ask a specific question and I'll give you an answer."
    )
