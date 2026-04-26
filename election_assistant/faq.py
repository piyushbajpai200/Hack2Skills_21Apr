FAQ_TOPICS = {
    "registration": "Registration means getting on your state's voter rolls before the deadline. If your state offers same-day registration, check exact rules and required documents.",
    "id requirements": "ID rules vary by state. Check your official state election website for accepted photo/non-photo IDs and alternatives.",
    "mail ballot rules": "Mail ballots often require strict steps like signatures, sealed envelopes, and specific return deadlines. Follow your ballot packet instructions exactly.",
    "polling place": "Your polling place may change between elections. Confirm your location and hours through your local election office.",
    "issue help": "If you have issues, ask poll workers for assistance, request a provisional ballot if needed, and contact your local election office immediately.",
}


def answer_topic(topic: str) -> str:
    normalized = topic.strip().lower()
    return FAQ_TOPICS.get(
        normalized,
        "I can help with: registration, ID requirements, mail ballot rules, polling place, or issue help.",
    )
