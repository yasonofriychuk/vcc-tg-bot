import datetime
from typing import Any, Dict, List, Literal, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RegisterUserIn")


@_attrs_define
class RegisterUserIn:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        login (str):
        password (str):
        email (str):
        last_name (str):
        first_name (str):
        middle_name (Union[Unset, str]):
        phone (Union[Unset, str]):
        birthday (Union[Unset, datetime.date]):
        role_id (Union[Literal[5], Unset]):
        type (Union[Literal['native'], Unset]):
    """

    login: str
    password: str
    email: str
    last_name: str
    first_name: str
    middle_name: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    birthday: Union[Unset, datetime.date] = UNSET
    role_id: Union[Literal[5], Unset] = UNSET
    type: Union[Literal["native"], Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        login = self.login

        password = self.password

        email = self.email

        last_name = self.last_name

        first_name = self.first_name

        middle_name = self.middle_name

        phone = self.phone

        birthday: Union[Unset, str] = UNSET
        if not isinstance(self.birthday, Unset):
            birthday = self.birthday.isoformat()

        role_id = self.role_id

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "login": login,
                "password": password,
                "email": email,
                "lastName": last_name,
                "firstName": first_name,
            }
        )
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if birthday is not UNSET:
            field_dict["birthday"] = birthday
        if role_id is not UNSET:
            field_dict["roleId"] = role_id
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        login = d.pop("login")

        password = d.pop("password")

        email = d.pop("email")

        last_name = d.pop("lastName")

        first_name = d.pop("firstName")

        middle_name = d.pop("middleName", UNSET)

        phone = d.pop("phone", UNSET)

        _birthday = d.pop("birthday", UNSET)
        birthday: Union[Unset, datetime.date]
        if isinstance(_birthday, Unset) or _birthday is None:
            birthday = UNSET
        else:
            birthday = isoparse(_birthday).date()

        role_id = cast(Union[Literal[5], Unset], d.pop("roleId", UNSET))
        if role_id != 5 and not isinstance(role_id, Unset):
            raise ValueError(f"roleId must match const 5, got '{role_id}'")

        type = cast(Union[Literal["native"], Unset], d.pop("type", UNSET))
        if type != "native" and not isinstance(type, Unset):
            raise ValueError(f"type must match const 'native', got '{type}'")

        register_user_in = cls(
            login=login,
            password=password,
            email=email,
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
            phone=phone,
            birthday=birthday,
            role_id=role_id,
            type=type,
        )

        register_user_in.additional_properties = d
        return register_user_in

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
