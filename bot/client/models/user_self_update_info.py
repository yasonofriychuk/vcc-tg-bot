import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserSelfUpdateInfo")


@_attrs_define
class UserSelfUpdateInfo:
    """Перечень полей пользователя, которые он сам способен редактировать у своей учетной записи

    Attributes:
        first_name (str):
        last_name (str):
        email (str):
        password (Union[Unset, str]):
        middle_name (Union[Unset, str]):
        phone (Union[Unset, str]):
        birthday (Union[Unset, datetime.date]):
    """

    first_name: str
    last_name: str
    email: str
    password: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    birthday: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        email = self.email

        password = self.password

        middle_name = self.middle_name

        phone = self.phone

        birthday: Union[Unset, str] = UNSET
        if not isinstance(self.birthday, Unset):
            birthday = self.birthday.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if birthday is not UNSET:
            field_dict["birthday"] = birthday

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        first_name = d.pop("firstName")

        last_name = d.pop("lastName")

        email = d.pop("email")

        password = d.pop("password", UNSET)

        middle_name = d.pop("middleName", UNSET)

        phone = d.pop("phone", UNSET)

        _birthday = d.pop("birthday", UNSET)
        birthday: Union[Unset, datetime.date]
        if isinstance(_birthday, Unset) or _birthday is None:
            birthday = UNSET
        else:
            birthday = isoparse(_birthday).date()

        user_self_update_info = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            middle_name=middle_name,
            phone=phone,
            birthday=birthday,
        )

        user_self_update_info.additional_properties = d
        return user_self_update_info

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
