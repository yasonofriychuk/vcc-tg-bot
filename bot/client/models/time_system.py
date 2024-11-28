from enum import Enum


class TimeSystem(str, Enum):
    HOURS = "hours"
    MINUTES = "minutes"

    def __str__(self) -> str:
        return str(self.value)
