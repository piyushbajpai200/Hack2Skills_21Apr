from election_assistant.models import UserProfile


def official_resources(profile: UserProfile) -> list[str]:
    state_query = profile.state.replace(" ", "-").lower()
    return [
        "https://www.vote.gov/",
        f"https://www.usa.gov/state-election-office?state={state_query}",
    ]


def format_escalation(profile: UserProfile) -> str:
    links = official_resources(profile)
    lines = [
        "Official sources to verify deadlines and legal requirements:",
        *[f"- {link}" for link in links],
        "If anything is unclear, contact your county or state election office directly.",
    ]
    return "\n".join(lines)
