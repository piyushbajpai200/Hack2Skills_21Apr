from election_assistant.assistant import generate_guidance
from election_assistant.checklist import build_checklist
from election_assistant.intake import build_profile
from election_assistant.timeline import build_roadmap


def test_build_profile_normalizes_method() -> None:
    profile = build_profile("Georgia", "Yes", "Mail or absentee")
    assert profile.first_time_voter is True
    assert profile.voting_method == "mail_absentee"


def test_roadmap_includes_first_time_and_mail_steps() -> None:
    profile = build_profile("Georgia", "Yes", "mail")
    roadmap = build_roadmap(profile)
    text = " ".join(part for _, part in roadmap)
    assert "First-time voter setup" in " ".join(name for name, _ in roadmap)
    assert "absentee/mail ballot" in text


def test_checklist_sections_exist() -> None:
    profile = build_profile("Texas", "No", "Not sure")
    checklist = build_checklist(profile)
    assert "Do this today" in checklist
    assert "Do this this week" in checklist
    assert "Final 48-hour prep" in checklist


def test_generate_guidance_contains_official_sources() -> None:
    result = generate_guidance("California", "No", "Election Day")
    assert "https://www.vote.gov/" in result
    assert "Big picture:" in result
