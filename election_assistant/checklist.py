from election_assistant.models import UserProfile


def build_checklist(profile: UserProfile) -> dict[str, list[str]]:
    today = [
        "Check your voter registration status on your official state election site.",
        "Confirm your current address and name match registration records.",
    ]
    this_week = [
        "Review ID requirements and acceptable documents.",
        "Look up your polling place or early-vote locations.",
    ]
    final_48h = [
        "Prepare required ID/documents and transportation plan.",
        "Verify polling place hours or ballot drop-off rules.",
    ]

    if profile.voting_method == "mail_absentee":
        today.append("Request your mail/absentee ballot as early as possible.")
        this_week.append("Read instructions carefully (signature, envelope, witness/notary if required).")
        final_48h.append("Return your ballot with enough time to meet your state's return rules.")

    if profile.first_time_voter:
        today.append("Review a sample ballot so choices and ballot layout are familiar.")

    if profile.voting_method == "not_sure":
        this_week.append("Choose a voting method after comparing your state's deadlines and options.")

    return {
        "Do this today": today,
        "Do this this week": this_week,
        "Final 48-hour prep": final_48h,
    }


def format_checklist(checklist: dict[str, list[str]]) -> str:
    lines: list[str] = []
    for section, items in checklist.items():
        lines.append(section)
        for item in items:
            lines.append(f"- [ ] {item}")
        lines.append("")
    return "\n".join(lines).strip()
