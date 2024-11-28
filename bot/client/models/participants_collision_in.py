import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.id_mixin import IdMixin
    from ..models.participant_mock import ParticipantMock


T = TypeVar("T", bound="ParticipantsCollisionIn")


@_attrs_define
class ParticipantsCollisionIn:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        started_at (datetime.datetime):  Example: 2024-11-27T18:32:19.849285.
        ended_at (Union[Unset, datetime.datetime]):  Example: 2024-11-27T20:32:19.849311.
        current_meeting_id (Union[Unset, int]): Для обновления списка участников, когда не нужно учитывать занятость в
            текущем ВКС Example: 1.
        duration (Union[Unset, int]):  Example: 120.
        participants (Union[Unset, List['ParticipantMock']]):
        groups (Union[Unset, List['IdMixin']]): Группы, для которых необходимо проверить участников
    """

    started_at: datetime.datetime
    ended_at: Union[Unset, datetime.datetime] = UNSET
    current_meeting_id: Union[Unset, int] = UNSET
    duration: Union[Unset, int] = UNSET
    participants: Union[Unset, List["ParticipantMock"]] = UNSET
    groups: Union[Unset, List["IdMixin"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        started_at = self.started_at.isoformat()

        ended_at: Union[Unset, str] = UNSET
        if not isinstance(self.ended_at, Unset):
            ended_at = self.ended_at.isoformat()

        current_meeting_id = self.current_meeting_id

        duration = self.duration

        participants: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.participants, Unset):
            participants = []
            for participants_item_data in self.participants:
                participants_item = participants_item_data.to_dict()
                participants.append(participants_item)

        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startedAt": started_at,
            }
        )
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if current_meeting_id is not UNSET:
            field_dict["currentMeetingId"] = current_meeting_id
        if duration is not UNSET:
            field_dict["duration"] = duration
        if participants is not UNSET:
            field_dict["participants"] = participants
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.id_mixin import IdMixin
        from ..models.participant_mock import ParticipantMock

        d = src_dict.copy()
        started_at = isoparse(d.pop("startedAt"))

        _ended_at = d.pop("endedAt", UNSET)
        ended_at: Union[Unset, datetime.datetime]
        if isinstance(_ended_at, Unset):
            ended_at = UNSET
        else:
            ended_at = isoparse(_ended_at)

        current_meeting_id = d.pop("currentMeetingId", UNSET)

        duration = d.pop("duration", UNSET)

        participants = []
        _participants = d.pop("participants", UNSET)
        for participants_item_data in _participants or []:
            participants_item = ParticipantMock.from_dict(participants_item_data)

            participants.append(participants_item)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = IdMixin.from_dict(groups_item_data)

            groups.append(groups_item)

        participants_collision_in = cls(
            started_at=started_at,
            ended_at=ended_at,
            current_meeting_id=current_meeting_id,
            duration=duration,
            participants=participants,
            groups=groups,
        )

        participants_collision_in.additional_properties = d
        return participants_collision_in

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
