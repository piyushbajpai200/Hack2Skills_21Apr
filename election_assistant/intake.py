from election_assistant.models import UserProfile, VotingMethod


def _normalize_method(raw: str) -> VotingMethod:
    cleaned = raw.strip().lower()
    mapping = {
        "in-person early": "early_in_person",
        "early in person": "early_in_person",
        "early": "early_in_person",
        "election day": "election_day",
        "day": "election_day",
        "mail": "mail_absentee",
        "mail or absentee": "mail_absentee",
        "absentee": "mail_absentee",
        "not sure": "not_sure",
        "unsure": "not_sure",
    }
    return mapping.get(cleaned, "not_sure")


def build_profile(state: str, first_time_raw: str, method_raw: str) -> UserProfile:
    first_time = first_time_raw.strip().lower() in {"yes", "y", "true", "1"}
    method = _normalize_method(method_raw)
    return UserProfile(state=state.strip(), first_time_voter=first_time, voting_method=method)
