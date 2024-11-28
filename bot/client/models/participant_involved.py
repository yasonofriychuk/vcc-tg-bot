from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_bare import GroupBare
    from ..models.meeting_short import MeetingShort


T = TypeVar("T", bound="ParticipantInvolved")


@_attrs_define
class ParticipantInvolved:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        id (int):  Example: 1.
        meeting (Union[Unset, MeetingShort]): Промежуточная модель pydantic'а для унифицирования конфигов и удобного
            администрирования
        groups (Union[Unset, List['GroupBare']]):
    """

    id: int
    meeting: Union[Unset, "MeetingShort"] = UNSET
    groups: Union[Unset, List["GroupBare"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        meeting: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meeting, Unset):
            meeting = self.meeting.to_dict()

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
                "id": id,
            }
        )
        if meeting is not UNSET:
            field_dict["meeting"] = meeting
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.group_bare import GroupBare
        from ..models.meeting_short import MeetingShort

        d = src_dict.copy()
        id = d.pop("id")

        _meeting = d.pop("meeting", UNSET)
        meeting: Union[Unset, MeetingShort]
        if isinstance(_meeting, Unset):
            meeting = UNSET
        else:
            meeting = MeetingShort.from_dict(_meeting)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = GroupBare.from_dict(groups_item_data)

            groups.append(groups_item)

        participant_involved = cls(
            id=id,
            meeting=meeting,
            groups=groups,
        )

        participant_involved.additional_properties = d
        return participant_involved

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
