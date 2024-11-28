from enum import Enum


class MeetingRecurrenceUpdateType(str, Enum):
    ALL = "all"
    ONLY = "only"
    ONLY_FOLLOWING = "only_following"

    def __str__(self) -> str:
        return str(self.value)
