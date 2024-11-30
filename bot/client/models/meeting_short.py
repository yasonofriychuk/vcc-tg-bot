import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.room_short import RoomShort


T = TypeVar("T", bound="MeetingShort")


@_attrs_define
class MeetingShort:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        id (int):
        name (str):
        started_at (datetime.datetime):  Example: 2024-11-27T18:32:19.827487.
        ended_at (datetime.datetime):  Example: 2024-11-27T20:32:19.827513.
        room_id (Union[Unset, int]):
        room (Union[Unset, RoomShort]): Базовая модель для выдачи любого каталога
    """

    id: int
    name: str
    started_at: datetime.datetime
    ended_at: datetime.datetime
    room_id: Union[Unset, int] = UNSET
    room: Union[Unset, "RoomShort"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        started_at = self.started_at.isoformat()

        ended_at = self.ended_at.isoformat()

        room_id = self.room_id

        room: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.room, Unset):
            room = self.room.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "startedAt": started_at,
                "endedAt": ended_at,
            }
        )
        if room_id is not UNSET:
            field_dict["roomId"] = room_id
        if room is not UNSET:
            field_dict["room"] = room

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.room_short import RoomShort

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        started_at = isoparse(d.pop("startedAt"))

        ended_at = isoparse(d.pop("endedAt"))

        room_id = d.pop("roomId", UNSET)

        _room = d.pop("room", UNSET)
        room: Union[Unset, RoomShort]
        if isinstance(_room, Unset) or _room is _room:
            room = UNSET
        else:
            room = RoomShort.from_dict(_room)

        meeting_short = cls(
            id=id,
            name=name,
            started_at=started_at,
            ended_at=ended_at,
            room_id=room_id,
            room=room,
        )

        meeting_short.additional_properties = d
        return meeting_short

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
