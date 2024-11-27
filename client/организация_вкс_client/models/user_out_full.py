import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.user_priority import UserPriority
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.department_bare import DepartmentBare
    from ..models.role_bare import RoleBare


T = TypeVar("T", bound="UserOutFull")


@_attrs_define
class UserOutFull:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        id (int):
        login (str):
        last_name (str):
        first_name (str):
        email (str):
        role_ids (List[int]):
        is_active (bool):
        created_at (datetime.datetime):
        roles (List['RoleBare']):
        middle_name (Union[Unset, str]):
        department_id (Union[Unset, int]):
        post (Union[Unset, str]):
        priority (Union[Unset, UserPriority]): Приоритет пользователей при резервировании ВКС.

            Больший приоритет обеспечивает большие возможности по резервированию.

            Приоритеты делятся по уровням, самый большой приоритет обеспечивает 100% возможность резервирования комнаты
            (при недостаче ВКС или при назначении ВКС на занятое в текущее время положение, имеющийся сеанс будет отменён)
        phone (Union[Unset, str]):
        birthday (Union[Unset, datetime.date]):
        deleted_at (Union[Unset, datetime.datetime]):
        department (Union[Unset, DepartmentBare]): Промежуточная модель pydantic'а для унифицирования конфигов и
            удобного администрирования
    """

    id: int
    login: str
    last_name: str
    first_name: str
    email: str
    role_ids: List[int]
    is_active: bool
    created_at: datetime.datetime
    roles: List["RoleBare"]
    middle_name: Union[Unset, str] = UNSET
    department_id: Union[Unset, int] = UNSET
    post: Union[Unset, str] = UNSET
    priority: Union[Unset, UserPriority] = UNSET
    phone: Union[Unset, str] = UNSET
    birthday: Union[Unset, datetime.date] = UNSET
    deleted_at: Union[Unset, datetime.datetime] = UNSET
    department: Union[Unset, "DepartmentBare"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        login = self.login

        last_name = self.last_name

        first_name = self.first_name

        email = self.email

        role_ids = self.role_ids

        is_active = self.is_active

        created_at = self.created_at.isoformat()

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.to_dict()
            roles.append(roles_item)

        middle_name = self.middle_name

        department_id = self.department_id

        post = self.post

        priority: Union[Unset, int] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        phone = self.phone

        birthday: Union[Unset, str] = UNSET
        if not isinstance(self.birthday, Unset):
            birthday = self.birthday.isoformat()

        deleted_at: Union[Unset, str] = UNSET
        if not isinstance(self.deleted_at, Unset):
            deleted_at = self.deleted_at.isoformat()

        department: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.department, Unset):
            department = self.department.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "login": login,
                "lastName": last_name,
                "firstName": first_name,
                "email": email,
                "roleIds": role_ids,
                "isActive": is_active,
                "createdAt": created_at,
                "roles": roles,
            }
        )
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if department_id is not UNSET:
            field_dict["departmentId"] = department_id
        if post is not UNSET:
            field_dict["post"] = post
        if priority is not UNSET:
            field_dict["priority"] = priority
        if phone is not UNSET:
            field_dict["phone"] = phone
        if birthday is not UNSET:
            field_dict["birthday"] = birthday
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if department is not UNSET:
            field_dict["department"] = department

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.department_bare import DepartmentBare
        from ..models.role_bare import RoleBare

        d = src_dict.copy()
        id = d.pop("id")

        login = d.pop("login")

        last_name = d.pop("lastName")

        first_name = d.pop("firstName")

        email = d.pop("email")

        role_ids = cast(List[int], d.pop("roleIds"))

        is_active = d.pop("isActive")

        created_at = isoparse(d.pop("createdAt"))

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = RoleBare.from_dict(roles_item_data)

            roles.append(roles_item)

        middle_name = d.pop("middleName", UNSET)

        department_id = d.pop("departmentId", UNSET)

        post = d.pop("post", UNSET)

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

        _deleted_at = d.pop("deletedAt", UNSET)
        deleted_at: Union[Unset, datetime.datetime]
        if isinstance(_deleted_at, Unset):
            deleted_at = UNSET
        else:
            deleted_at = isoparse(_deleted_at)

        _department = d.pop("department", UNSET)
        department: Union[Unset, DepartmentBare]
        if isinstance(_department, Unset):
            department = UNSET
        else:
            department = DepartmentBare.from_dict(_department)

        user_out_full = cls(
            id=id,
            login=login,
            last_name=last_name,
            first_name=first_name,
            email=email,
            role_ids=role_ids,
            is_active=is_active,
            created_at=created_at,
            roles=roles,
            middle_name=middle_name,
            department_id=department_id,
            post=post,
            priority=priority,
            phone=phone,
            birthday=birthday,
            deleted_at=deleted_at,
            department=department,
        )

        user_out_full.additional_properties = d
        return user_out_full

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
