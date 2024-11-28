from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SimpleUserBare")


@_attrs_define
class SimpleUserBare:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        id (int):
        login (Union[Unset, str]):
        last_name (Union[Unset, str]):
        first_name (Union[Unset, str]):
        middle_name (Union[Unset, str]):
        department_id (Union[Unset, int]):
        email (Union[Unset, str]):
    """

    id: int
    login: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    department_id: Union[Unset, int] = UNSET
    email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        login = self.login

        last_name = self.last_name

        first_name = self.first_name

        middle_name = self.middle_name

        department_id = self.department_id

        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if login is not UNSET:
            field_dict["login"] = login
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if department_id is not UNSET:
            field_dict["departmentId"] = department_id
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        login = d.pop("login", UNSET)

        last_name = d.pop("lastName", UNSET)

        first_name = d.pop("firstName", UNSET)

        middle_name = d.pop("middleName", UNSET)

        department_id = d.pop("departmentId", UNSET)

        email = d.pop("email", UNSET)

        simple_user_bare = cls(
            id=id,
            login=login,
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
            department_id=department_id,
            email=email,
        )

        simple_user_bare.additional_properties = d
        return simple_user_bare

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
