import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.user_priority import UserPriority
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateUserIn")


@_attrs_define
class CreateUserIn:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        login (str):
        password (str):
        email (str):
        last_name (str):
        first_name (str):
        role_ids (List[int]):  Example: [5].
        priority (UserPriority): Приоритет пользователей при резервировании ВКС.

            Больший приоритет обеспечивает большие возможности по резервированию.

            Приоритеты делятся по уровням, самый большой приоритет обеспечивает 100% возможность резервирования комнаты
            (при недостаче ВКС или при назначении ВКС на занятое в текущее время положение, имеющийся сеанс будет отменён)
        department_id (int):  Example: 1.
        middle_name (Union[Unset, str]):
        phone (Union[Unset, str]):
        birthday (Union[Unset, datetime.date]):
        is_send_email (Union[Unset, bool]): Отправлять на почту данны для входа в учётную запись Default: True.
    """

    login: str
    password: str
    email: str
    last_name: str
    first_name: str
    role_ids: List[int]
    priority: UserPriority
    department_id: int
    middle_name: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    birthday: Union[Unset, datetime.date] = UNSET
    is_send_email: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        login = self.login

        password = self.password

        email = self.email

        last_name = self.last_name

        first_name = self.first_name

        role_ids = self.role_ids

        priority = self.priority.value

        department_id = self.department_id

        middle_name = self.middle_name

        phone = self.phone

        birthday: Union[Unset, str] = UNSET
        if not isinstance(self.birthday, Unset):
            birthday = self.birthday.isoformat()

        is_send_email = self.is_send_email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "login": login,
                "password": password,
                "email": email,
                "lastName": last_name,
                "firstName": first_name,
                "roleIds": role_ids,
                "priority": priority,
                "departmentId": department_id,
            }
        )
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if birthday is not UNSET:
            field_dict["birthday"] = birthday
        if is_send_email is not UNSET:
            field_dict["isSendEmail"] = is_send_email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        login = d.pop("login")

        password = d.pop("password")

        email = d.pop("email")

        last_name = d.pop("lastName")

        first_name = d.pop("firstName")

        role_ids = cast(List[int], d.pop("roleIds"))

        priority = UserPriority(d.pop("priority"))

        department_id = d.pop("departmentId")

        middle_name = d.pop("middleName", UNSET)

        phone = d.pop("phone", UNSET)

        _birthday = d.pop("birthday", UNSET)
        birthday: Union[Unset, datetime.date]
        if isinstance(_birthday, Unset):
            birthday = UNSET
        else:
            birthday = isoparse(_birthday).date()

        is_send_email = d.pop("isSendEmail", UNSET)

        create_user_in = cls(
            login=login,
            password=password,
            email=email,
            last_name=last_name,
            first_name=first_name,
            role_ids=role_ids,
            priority=priority,
            department_id=department_id,
            middle_name=middle_name,
            phone=phone,
            birthday=birthday,
            is_send_email=is_send_email,
        )

        create_user_in.additional_properties = d
        return create_user_in

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
