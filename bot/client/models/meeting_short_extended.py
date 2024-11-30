import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.meeting_backend import MeetingBackend
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.participant_out import ParticipantOut
    from ..models.room_short import RoomShort
    from ..models.user_brief import UserBrief


T = TypeVar("T", bound="MeetingShortExtended")


@_attrs_define
class MeetingShortExtended:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        id (int):
        name (str):
        started_at (datetime.datetime):  Example: 2024-11-27T18:32:19.827487.
        ended_at (datetime.datetime):  Example: 2024-11-27T20:32:19.827513.
        backend (MeetingBackend): Поддерживаемый вариант запуска ВКС.

            На данный момент на уровне API поддерживается только cisco,
            всё остальное рассматривается как внешний сервис, для которого нет интеграции
        organized_by (int):
        participants (List['ParticipantOut']):
        room_id (Union[Unset, int]):
        room (Union[Unset, RoomShort]): Базовая модель для выдачи любого каталога
        participants_count (Union[Unset, int]):
        organized_user (Union[Unset, UserBrief]): Промежуточная модель pydantic'а для унифицирования конфигов и удобного
            администрирования
    """

    id: int
    name: str
    started_at: datetime.datetime
    ended_at: datetime.datetime
    backend: MeetingBackend
    organized_by: int
    participants: List["ParticipantOut"]
    room_id: Union[Unset, int] = UNSET
    room: Union[Unset, "RoomShort"] = UNSET
    participants_count: Union[Unset, int] = UNSET
    organized_user: Union[Unset, "UserBrief"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        started_at = self.started_at.isoformat()

        ended_at = self.ended_at.isoformat()

        backend = self.backend.value

        organized_by = self.organized_by

        participants = []
        for participants_item_data in self.participants:
            participants_item = participants_item_data.to_dict()
            participants.append(participants_item)

        room_id = self.room_id

        room: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.room, Unset):
            room = self.room.to_dict()

        participants_count = self.participants_count

        organized_user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.organized_user, Unset):
            organized_user = self.organized_user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "startedAt": started_at,
                "endedAt": ended_at,
                "backend": backend,
                "organizedBy": organized_by,
                "participants": participants,
            }
        )
        if room_id is not UNSET:
            field_dict["roomId"] = room_id
        if room is not UNSET:
            field_dict["room"] = room
        if participants_count is not UNSET:
            field_dict["participantsCount"] = participants_count
        if organized_user is not UNSET:
            field_dict["organizedUser"] = organized_user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.participant_out import ParticipantOut
        from ..models.room_short import RoomShort
        from ..models.user_brief import UserBrief

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        started_at = isoparse(d.pop("startedAt"))

        ended_at = isoparse(d.pop("endedAt"))

        backend = MeetingBackend(d.pop("backend"))

        organized_by = d.pop("organizedBy")

        participants = []
        _participants = d.pop("participants")
        for participants_item_data in _participants:
            participants_item = ParticipantOut.from_dict(participants_item_data)

            participants.append(participants_item)

        room_id = d.pop("roomId", UNSET)

        _room = d.pop("room", UNSET)
        room: Union[Unset, RoomShort]
        if isinstance(_room, Unset) or _room is _room:
            room = UNSET
        else:
            room = RoomShort.from_dict(_room)

        participants_count = d.pop("participantsCount", UNSET)

        _organized_user = d.pop("organizedUser", UNSET)
        organized_user: Union[Unset, UserBrief]
        if isinstance(_organized_user, Unset):
            organized_user = UNSET
        else:
            organized_user = UserBrief.from_dict(_organized_user)

        meeting_short_extended = cls(
            id=id,
            name=name,
            started_at=started_at,
            ended_at=ended_at,
            backend=backend,
            organized_by=organized_by,
            participants=participants,
            room_id=room_id,
            room=room,
            participants_count=participants_count,
            organized_user=organized_user,
        )

        meeting_short_extended.additional_properties = d
        return meeting_short_extended

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
