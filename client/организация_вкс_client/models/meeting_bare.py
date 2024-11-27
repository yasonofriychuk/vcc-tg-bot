import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.meeting_states import MeetingStates
from ..types import UNSET, Unset

T = TypeVar("T", bound="MeetingBare")


@_attrs_define
class MeetingBare:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        name (str):
        send_notifications_at (Union[datetime.datetime, int]):  Example: 2024-11-27T16:32:19.816061.
        started_at (datetime.datetime):  Example: 2024-11-27T18:32:19.816087.
        ended_at (datetime.datetime):  Example: 2024-11-27T20:32:19.816099.
        is_governor_presents (bool):
        created_at (datetime.datetime):
        state (MeetingStates): Перечень состояний, в которых может находиться сущность ВКС
        created_by (int):
        is_notify_accepted (bool):
        permalink_id (Union[Unset, str]): идентификатор постоянной ссылка на ВКС. доступна сразу после создания и
            содержит базовую информацию для подключения к ВКС
        permalink (Union[Unset, str]): Ссылка на frontend страницу для перехода в вкс
        id (Union[Unset, int]):
        room_id (Union[Unset, int]):
        participants_count (Union[Unset, int]):
        duration (Union[Unset, int]):  Example: 120.
        closed_at (Union[Unset, datetime.datetime]):
        organized_by (Union[Unset, int]):
        is_virtual (Union[Unset, bool]): Является ли ВКС виртуально созданным объектом Default: False.
    """

    name: str
    send_notifications_at: Union[datetime.datetime, int]
    started_at: datetime.datetime
    ended_at: datetime.datetime
    is_governor_presents: bool
    created_at: datetime.datetime
    state: MeetingStates
    created_by: int
    is_notify_accepted: bool
    permalink_id: Union[Unset, str] = UNSET
    permalink: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    room_id: Union[Unset, int] = UNSET
    participants_count: Union[Unset, int] = UNSET
    duration: Union[Unset, int] = UNSET
    closed_at: Union[Unset, datetime.datetime] = UNSET
    organized_by: Union[Unset, int] = UNSET
    is_virtual: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        send_notifications_at: Union[int, str]
        if isinstance(self.send_notifications_at, datetime.datetime):
            send_notifications_at = self.send_notifications_at.isoformat()
        else:
            send_notifications_at = self.send_notifications_at

        started_at = self.started_at.isoformat()

        ended_at = self.ended_at.isoformat()

        is_governor_presents = self.is_governor_presents

        created_at = self.created_at.isoformat()

        state = self.state.value

        created_by = self.created_by

        is_notify_accepted = self.is_notify_accepted

        permalink_id = self.permalink_id

        permalink = self.permalink

        id = self.id

        room_id = self.room_id

        participants_count = self.participants_count

        duration = self.duration

        closed_at: Union[Unset, str] = UNSET
        if not isinstance(self.closed_at, Unset):
            closed_at = self.closed_at.isoformat()

        organized_by = self.organized_by

        is_virtual = self.is_virtual

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "sendNotificationsAt": send_notifications_at,
                "startedAt": started_at,
                "endedAt": ended_at,
                "isGovernorPresents": is_governor_presents,
                "createdAt": created_at,
                "state": state,
                "createdBy": created_by,
                "isNotifyAccepted": is_notify_accepted,
            }
        )
        if permalink_id is not UNSET:
            field_dict["permalinkId"] = permalink_id
        if permalink is not UNSET:
            field_dict["permalink"] = permalink
        if id is not UNSET:
            field_dict["id"] = id
        if room_id is not UNSET:
            field_dict["roomId"] = room_id
        if participants_count is not UNSET:
            field_dict["participantsCount"] = participants_count
        if duration is not UNSET:
            field_dict["duration"] = duration
        if closed_at is not UNSET:
            field_dict["closedAt"] = closed_at
        if organized_by is not UNSET:
            field_dict["organizedBy"] = organized_by
        if is_virtual is not UNSET:
            field_dict["isVirtual"] = is_virtual

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        def _parse_send_notifications_at(data: object) -> Union[datetime.datetime, int]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                send_notifications_at_type_1 = isoparse(data)

                return send_notifications_at_type_1
            except:  # noqa: E722
                pass
            return cast(Union[datetime.datetime, int], data)

        send_notifications_at = _parse_send_notifications_at(d.pop("sendNotificationsAt"))

        started_at = isoparse(d.pop("startedAt"))

        ended_at = isoparse(d.pop("endedAt"))

        is_governor_presents = d.pop("isGovernorPresents")

        created_at = isoparse(d.pop("createdAt"))

        state = MeetingStates(d.pop("state"))

        created_by = d.pop("createdBy")

        is_notify_accepted = d.pop("isNotifyAccepted")

        permalink_id = d.pop("permalinkId", UNSET)

        permalink = d.pop("permalink", UNSET)

        id = d.pop("id", UNSET)

        room_id = d.pop("roomId", UNSET)

        participants_count = d.pop("participantsCount", UNSET)

        duration = d.pop("duration", UNSET)

        _closed_at = d.pop("closedAt", UNSET)
        closed_at: Union[Unset, datetime.datetime]
        if isinstance(_closed_at, Unset):
            closed_at = UNSET
        else:
            closed_at = isoparse(_closed_at)

        organized_by = d.pop("organizedBy", UNSET)

        is_virtual = d.pop("isVirtual", UNSET)

        meeting_bare = cls(
            name=name,
            send_notifications_at=send_notifications_at,
            started_at=started_at,
            ended_at=ended_at,
            is_governor_presents=is_governor_presents,
            created_at=created_at,
            state=state,
            created_by=created_by,
            is_notify_accepted=is_notify_accepted,
            permalink_id=permalink_id,
            permalink=permalink,
            id=id,
            room_id=room_id,
            participants_count=participants_count,
            duration=duration,
            closed_at=closed_at,
            organized_by=organized_by,
            is_virtual=is_virtual,
        )

        meeting_bare.additional_properties = d
        return meeting_bare

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
