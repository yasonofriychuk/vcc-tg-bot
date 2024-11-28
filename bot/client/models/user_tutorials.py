from enum import Enum


class UserTutorials(str, Enum):
    MEETING_CREATE = "meeting_create"
    SYSTEM = "system"
    VCC_PAGE = "vcc_page"

    def __str__(self) -> str:
        return str(self.value)
