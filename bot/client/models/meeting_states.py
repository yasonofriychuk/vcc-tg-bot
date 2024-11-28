from enum import Enum


class MeetingStates(str, Enum):
    BOOKED = "booked"
    CANCELLED = "cancelled"
    ENDED = "ended"
    STARTED = "started"

    def __str__(self) -> str:
        return str(self.value)
