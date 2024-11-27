from enum import Enum


class MeetingSortingFields(str, Enum):
    CREATEDAT = "createdAt"
    EVENTID = "eventId"
    ID = "id"
    NAME = "name"
    STARTEDAT = "startedAt"

    def __str__(self) -> str:
        return str(self.value)
