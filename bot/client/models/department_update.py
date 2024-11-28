from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DepartmentUpdate")


@_attrs_define
class DepartmentUpdate:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        name (str):  Example: Очень важный департамент.
        short_name (str):
        address (str):
        email (str):  Example: test_email@email.com.
        parent_id (Union[Unset, int]):
    """

    name: str
    short_name: str
    address: str
    email: str
    parent_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        short_name = self.short_name

        address = self.address

        email = self.email

        parent_id = self.parent_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "shortName": short_name,
                "address": address,
                "email": email,
            }
        )
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        short_name = d.pop("shortName")

        address = d.pop("address")

        email = d.pop("email")

        parent_id = d.pop("parentId", UNSET)

        department_update = cls(
            name=name,
            short_name=short_name,
            address=address,
            email=email,
            parent_id=parent_id,
        )

        department_update.additional_properties = d
        return department_update

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
