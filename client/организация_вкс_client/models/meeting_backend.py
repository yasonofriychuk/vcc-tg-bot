from enum import Enum


class MeetingBackend(str, Enum):
    CISCO = "cisco"
    EXTERNAL = "external"
    PERMANENTROOM = "permanentroom"
    VINTEO = "vinteo"

    def __str__(self) -> str:
        return str(self.value)
