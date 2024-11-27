from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_create_params import GroupCreateParams
    from ..models.id_mixin import IdMixin


T = TypeVar("T", bound="GroupCreate")


@_attrs_define
class GroupCreate:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        name (str):
        description (Union[Unset, str]):
        params (Union[Unset, GroupCreateParams]):
        is_public (Union[Unset, bool]):  Default: False.
        members (Union[Unset, List['IdMixin']]):
        meeting_id (Union[Unset, int]):
    """

    name: str
    description: Union[Unset, str] = UNSET
    params: Union[Unset, "GroupCreateParams"] = UNSET
    is_public: Union[Unset, bool] = False
    members: Union[Unset, List["IdMixin"]] = UNSET
    meeting_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        description = self.description

        params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        is_public = self.is_public

        members: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        meeting_id = self.meeting_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if params is not UNSET:
            field_dict["params"] = params
        if is_public is not UNSET:
            field_dict["isPublic"] = is_public
        if members is not UNSET:
            field_dict["members"] = members
        if meeting_id is not UNSET:
            field_dict["meetingId"] = meeting_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.group_create_params import GroupCreateParams
        from ..models.id_mixin import IdMixin

        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description", UNSET)

        _params = d.pop("params", UNSET)
        params: Union[Unset, GroupCreateParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = GroupCreateParams.from_dict(_params)

        is_public = d.pop("isPublic", UNSET)

        members = []
        _members = d.pop("members", UNSET)
        for members_item_data in _members or []:
            members_item = IdMixin.from_dict(members_item_data)

            members.append(members_item)

        meeting_id = d.pop("meetingId", UNSET)

        group_create = cls(
            name=name,
            description=description,
            params=params,
            is_public=is_public,
            members=members,
            meeting_id=meeting_id,
        )

        group_create.additional_properties = d
        return group_create

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
