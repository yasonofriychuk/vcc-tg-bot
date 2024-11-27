from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_full_params import GroupFullParams
    from ..models.simple_user_bare import SimpleUserBare


T = TypeVar("T", bound="GroupFull")


@_attrs_define
class GroupFull:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        id (int):  Example: 1.
        name (str):
        created_by (int):
        description (Union[Unset, str]):
        params (Union[Unset, GroupFullParams]):
        is_public (Union[Unset, bool]):  Default: False.
        copied_from_id (Union[Unset, int]):
        members_count (Union[Unset, int]):
        members (Union[Unset, List['SimpleUserBare']]):
    """

    id: int
    name: str
    created_by: int
    description: Union[Unset, str] = UNSET
    params: Union[Unset, "GroupFullParams"] = UNSET
    is_public: Union[Unset, bool] = False
    copied_from_id: Union[Unset, int] = UNSET
    members_count: Union[Unset, int] = UNSET
    members: Union[Unset, List["SimpleUserBare"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        created_by = self.created_by

        description = self.description

        params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        is_public = self.is_public

        copied_from_id = self.copied_from_id

        members_count = self.members_count

        members: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()
                members.append(members_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "createdBy": created_by,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if params is not UNSET:
            field_dict["params"] = params
        if is_public is not UNSET:
            field_dict["isPublic"] = is_public
        if copied_from_id is not UNSET:
            field_dict["copiedFromId"] = copied_from_id
        if members_count is not UNSET:
            field_dict["membersCount"] = members_count
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.group_full_params import GroupFullParams
        from ..models.simple_user_bare import SimpleUserBare

        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        created_by = d.pop("createdBy")

        description = d.pop("description", UNSET)

        _params = d.pop("params", UNSET)
        params: Union[Unset, GroupFullParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = GroupFullParams.from_dict(_params)

        is_public = d.pop("isPublic", UNSET)

        copied_from_id = d.pop("copiedFromId", UNSET)

        members_count = d.pop("membersCount", UNSET)

        members = []
        _members = d.pop("members", UNSET)
        for members_item_data in _members or []:
            members_item = SimpleUserBare.from_dict(members_item_data)

            members.append(members_item)

        group_full = cls(
            id=id,
            name=name,
            created_by=created_by,
            description=description,
            params=params,
            is_public=is_public,
            copied_from_id=copied_from_id,
            members_count=members_count,
            members=members,
        )

        group_full.additional_properties = d
        return group_full

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
