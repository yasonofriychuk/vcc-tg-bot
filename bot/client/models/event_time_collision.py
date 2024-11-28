import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventTimeCollision")


@_attrs_define
class EventTimeCollision:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        started_at (datetime.datetime):  Example: 2024-11-27T18:32:19.726611.
        ended_at (datetime.datetime):  Example: 2024-11-27T20:32:19.726635.
        room_id (Union[Unset, int]):
    """

    started_at: datetime.datetime
    ended_at: datetime.datetime
    room_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        started_at = self.started_at.isoformat()

        ended_at = self.ended_at.isoformat()

        room_id = self.room_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startedAt": started_at,
                "endedAt": ended_at,
            }
        )
        if room_id is not UNSET:
            field_dict["roomId"] = room_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        started_at = isoparse(d.pop("startedAt"))

        ended_at = isoparse(d.pop("endedAt"))

        room_id = d.pop("roomId", UNSET)

        event_time_collision = cls(
            started_at=started_at,
            ended_at=ended_at,
            room_id=room_id,
        )

        event_time_collision.additional_properties = d
        return event_time_collision

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
