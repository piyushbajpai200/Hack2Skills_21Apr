from dataclasses import dataclass
from typing import Literal

VotingMethod = Literal["early_in_person", "election_day", "mail_absentee", "not_sure"]


@dataclass
class UserProfile:
    state: str
    first_time_voter: bool
    voting_method: VotingMethod
