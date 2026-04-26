from election_assistant.models import UserProfile


GENERAL_MILESTONES = [
    ("Now", "Confirm your voter registration status and your legal name/address are current."),
    ("This week", "Review ID requirements and choose your voting method."),
    ("Before your state's deadlines", "Verify registration, ballot request, and ballot return cutoffs on official state election websites."),
    ("Election period", "Vote during early voting or on Election Day at the correct location/time."),
    ("After voting", "Track ballot status if your state provides ballot tracking."),
]


def build_roadmap(profile: UserProfile) -> list[tuple[str, str]]:
    roadmap = list(GENERAL_MILESTONES)

    if profile.voting_method == "mail_absentee":
        roadmap.insert(
            3,
            (
                "Mail ballot prep",
                "Request your absentee/mail ballot early and return it with the exact signature/witness steps required by your state.",
            ),
        )
    elif profile.voting_method == "election_day":
        roadmap.insert(
            3,
            (
                "Election Day prep",
                "Confirm polling place hours, transportation, and your accepted ID before Election Day.",
            ),
        )
    elif profile.voting_method == "early_in_person":
        roadmap.insert(
            3,
            (
                "Early voting prep",
                "Find early voting locations and operating dates/hours in your county.",
            ),
        )

    if profile.first_time_voter:
        roadmap.insert(
            1,
            (
                "First-time voter setup",
                "Review sample ballots and basic polling-place expectations so voting feels predictable.",
            ),
        )

    return roadmap


def format_roadmap(roadmap: list[tuple[str, str]]) -> str:
    lines = ["Timeline view:"]
    for phase, action in roadmap:
        lines.append(f"- {phase}: {action}")
    return "\n".join(lines)
