import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.room_bare import RoomBare


T = TypeVar("T", bound="EventFull")


@_attrs_define
class EventFull:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        is_offline_event (bool):
        name (str):
        started_at (datetime.datetime):
        id (int):
        room_id (Union[Unset, int]):
        ended_at (Union[Unset, datetime.datetime]): Время окончания мероприятия
        duration (Union[Unset, int]): Продолжительность мероприятия в минутах
        room (Union[Unset, RoomBare]): Базовая модель для выдачи любого каталога
    """

    is_offline_event: bool
    name: str
    started_at: datetime.datetime
    id: int
    room_id: Union[Unset, int] = UNSET
    ended_at: Union[Unset, datetime.datetime] = UNSET
    duration: Union[Unset, int] = UNSET
    room: Union[Unset, "RoomBare"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_offline_event = self.is_offline_event

        name = self.name

        started_at = self.started_at.isoformat()

        id = self.id

        room_id = self.room_id

        ended_at: Union[Unset, str] = UNSET
        if not isinstance(self.ended_at, Unset):
            ended_at = self.ended_at.isoformat()

        duration = self.duration

        room: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.room, Unset):
            room = self.room.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isOfflineEvent": is_offline_event,
                "name": name,
                "startedAt": started_at,
                "id": id,
            }
        )
        if room_id is not UNSET:
            field_dict["roomId"] = room_id
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if duration is not UNSET:
            field_dict["duration"] = duration
        if room is not UNSET:
            field_dict["room"] = room

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.room_bare import RoomBare

        d = src_dict.copy()
        is_offline_event = d.pop("isOfflineEvent")

        name = d.pop("name")

        started_at = isoparse(d.pop("startedAt"))

        id = d.pop("id")

        room_id = d.pop("roomId", UNSET)

        _ended_at = d.pop("endedAt", UNSET)
        ended_at: Union[Unset, datetime.datetime]
        if isinstance(_ended_at, Unset):
            ended_at = UNSET
        else:
            ended_at = isoparse(_ended_at)

        duration = d.pop("duration", UNSET)

        _room = d.pop("room", UNSET)
        room: Union[Unset, RoomBare]
        if isinstance(_room, Unset):
            room = UNSET
        else:
            room = RoomBare.from_dict(_room)

        event_full = cls(
            is_offline_event=is_offline_event,
            name=name,
            started_at=started_at,
            id=id,
            room_id=room_id,
            ended_at=ended_at,
            duration=duration,
            room=room,
        )

        event_full.additional_properties = d
        return event_full

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
