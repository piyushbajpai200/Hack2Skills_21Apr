from election_assistant.checklist import build_checklist, format_checklist
from election_assistant.escalation import format_escalation
from election_assistant.faq import answer_topic
from election_assistant.intake import build_profile
from election_assistant.timeline import build_roadmap, format_roadmap


def generate_guidance(state: str, first_time: str, method: str, topic: str | None = None) -> str:
    profile = build_profile(state, first_time, method)
    roadmap = build_roadmap(profile)
    checklist = build_checklist(profile)

    sections = [
        "Big picture:\nI'll help you understand your election process with a simple, nonpartisan plan tailored to your state and voting method.",
        format_roadmap(roadmap),
        "Step-by-step actions:\n1. Verify registration status.\n2. Confirm ID and voting location/rules.\n3. Complete your chosen voting method before the deadlines.\n4. Verify your ballot status when available.",
        "Common mistakes to avoid:\n- Waiting until the final deadline window.\n- Assuming last election's polling place is unchanged.\n- Missing mail ballot signature/packaging rules.",
        f"Your next best step:\nCheck your registration status today for {profile.state}.",
        format_checklist(checklist),
        format_escalation(profile),
    ]

    if topic:
        sections.append(f"Details on '{topic}':\n{answer_topic(topic)}")

    return "\n\n".join(sections)
