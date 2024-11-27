from enum import Enum


class CumulativeType(str, Enum):
    MEETINGS = "meetings"
    USERS = "users"

    def __str__(self) -> str:
        return str(self.value)
