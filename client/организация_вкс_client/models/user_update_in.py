import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.user_priority import UserPriority
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserUpdateIn")


@_attrs_define
class UserUpdateIn:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        login (Union[Unset, str]):
        password (Union[Unset, str]):
        email (Union[Unset, str]):
        last_name (Union[Unset, str]):
        first_name (Union[Unset, str]):
        middle_name (Union[Unset, str]):
        is_active (Union[Unset, bool]): Запрещена блокировка самого себя Default: True.
        role_ids (Union[Unset, List[int]]):  Example: [5].
        department_id (Union[Unset, int]):
        priority (Union[Unset, UserPriority]): Приоритет пользователей при резервировании ВКС.

            Больший приоритет обеспечивает большие возможности по резервированию.

            Приоритеты делятся по уровням, самый большой приоритет обеспечивает 100% возможность резервирования комнаты
            (при недостаче ВКС или при назначении ВКС на занятое в текущее время положение, имеющийся сеанс будет отменён)
        phone (Union[Unset, str]):
        birthday (Union[Unset, datetime.date]):
    """

    login: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = True
    role_ids: Union[Unset, List[int]] = UNSET
    department_id: Union[Unset, int] = UNSET
    priority: Union[Unset, UserPriority] = UNSET
    phone: Union[Unset, str] = UNSET
    birthday: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        login = self.login

        password = self.password

        email = self.email

        last_name = self.last_name

        first_name = self.first_name

        middle_name = self.middle_name

        is_active = self.is_active

        role_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.role_ids, Unset):
            role_ids = self.role_ids

        department_id = self.department_id

        priority: Union[Unset, int] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        phone = self.phone

        birthday: Union[Unset, str] = UNSET
        if not isinstance(self.birthday, Unset):
            birthday = self.birthday.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if login is not UNSET:
            field_dict["login"] = login
        if password is not UNSET:
            field_dict["password"] = password
        if email is not UNSET:
            field_dict["email"] = email
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if role_ids is not UNSET:
            field_dict["roleIds"] = role_ids
        if department_id is not UNSET:
            field_dict["departmentId"] = department_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if phone is not UNSET:
            field_dict["phone"] = phone
        if birthday is not UNSET:
            field_dict["birthday"] = birthday

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        login = d.pop("login", UNSET)

        password = d.pop("password", UNSET)

        email = d.pop("email", UNSET)

        last_name = d.pop("lastName", UNSET)

        first_name = d.pop("firstName", UNSET)

        middle_name = d.pop("middleName", UNSET)

        is_active = d.pop("isActive", UNSET)

        role_ids = cast(List[int], d.pop("roleIds", UNSET))

        department_id = d.pop("departmentId", UNSET)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, UserPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = UserPriority(_priority)

        phone = d.pop("phone", UNSET)

        _birthday = d.pop("birthday", UNSET)
        birthday: Union[Unset, datetime.date]
        if isinstance(_birthday, Unset):
            birthday = UNSET
        else:
            birthday = isoparse(_birthday).date()

        user_update_in = cls(
            login=login,
            password=password,
            email=email,
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
            is_active=is_active,
            role_ids=role_ids,
            department_id=department_id,
            priority=priority,
            phone=phone,
            birthday=birthday,
        )

        user_update_in.additional_properties = d
        return user_update_in

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
