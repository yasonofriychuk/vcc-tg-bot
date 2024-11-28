import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_brief import UserBrief


T = TypeVar("T", bound="EventShort")


@_attrs_define
class EventShort:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        started_at (datetime.datetime):  Example: 2024-11-27T18:32:19.726611.
        ended_at (datetime.datetime):  Example: 2024-11-27T20:32:19.726635.
        id (int):
        name (str):
        is_offline_event (bool):
        created_user (UserBrief): Промежуточная модель pydantic'а для унифицирования конфигов и удобного
            администрирования
        room_id (Union[Unset, int]):
        can_kickoff (Union[Unset, bool]): Может ли текущий пользователь выместить данный ВКС при создании своего на то
            же время Default: False.
    """

    started_at: datetime.datetime
    ended_at: datetime.datetime
    id: int
    name: str
    is_offline_event: bool
    created_user: "UserBrief"
    room_id: Union[Unset, int] = UNSET
    can_kickoff: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        started_at = self.started_at.isoformat()

        ended_at = self.ended_at.isoformat()

        id = self.id

        name = self.name

        is_offline_event = self.is_offline_event

        created_user = self.created_user.to_dict()

        room_id = self.room_id

        can_kickoff = self.can_kickoff

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startedAt": started_at,
                "endedAt": ended_at,
                "id": id,
                "name": name,
                "isOfflineEvent": is_offline_event,
                "createdUser": created_user,
            }
        )
        if room_id is not UNSET:
            field_dict["roomId"] = room_id
        if can_kickoff is not UNSET:
            field_dict["canKickoff"] = can_kickoff

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_brief import UserBrief

        d = src_dict.copy()
        started_at = isoparse(d.pop("startedAt"))

        ended_at = isoparse(d.pop("endedAt"))

        id = d.pop("id")

        name = d.pop("name")

        is_offline_event = d.pop("isOfflineEvent")

        created_user = UserBrief.from_dict(d.pop("createdUser"))

        room_id = d.pop("roomId", UNSET)

        can_kickoff = d.pop("canKickoff", UNSET)

        event_short = cls(
            started_at=started_at,
            ended_at=ended_at,
            id=id,
            name=name,
            is_offline_event=is_offline_event,
            created_user=created_user,
            room_id=room_id,
            can_kickoff=can_kickoff,
        )

        event_short.additional_properties = d
        return event_short

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
