from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DepartmentBare")


@_attrs_define
class DepartmentBare:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        name (str):  Example: Очень важный департамент.
        short_name (str):
        id (int):
        address (Union[Unset, str]):
        email (Union[Unset, str]):
        parent_id (Union[Unset, int]):
        ldap_name (Union[Unset, str]):
    """

    name: str
    short_name: str
    id: int
    address: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    parent_id: Union[Unset, int] = UNSET
    ldap_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        short_name = self.short_name

        id = self.id

        address = self.address

        email = self.email

        parent_id = self.parent_id

        ldap_name = self.ldap_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "shortName": short_name,
                "id": id,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if email is not UNSET:
            field_dict["email"] = email
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if ldap_name is not UNSET:
            field_dict["ldapName"] = ldap_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        short_name = d.pop("shortName")

        id = d.pop("id")

        address = d.pop("address", UNSET)

        email = d.pop("email", UNSET)

        parent_id = d.pop("parentId", UNSET)

        ldap_name = d.pop("ldapName", UNSET)

        department_bare = cls(
            name=name,
            short_name=short_name,
            id=id,
            address=address,
            email=email,
            parent_id=parent_id,
            ldap_name=ldap_name,
        )

        department_bare.additional_properties = d
        return department_bare

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
