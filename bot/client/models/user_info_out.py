import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.department_bare import DepartmentBare
    from ..models.role_bare import RoleBare


T = TypeVar("T", bound="UserInfoOut")


@_attrs_define
class UserInfoOut:
    """Перечень полей пользователя, передаваемых при авторизации вместе с JWT токеном

    Attributes:
        id (int):
        email (str):
        last_name (str):
        first_name (str):
        updated_at (datetime.datetime):
        roles (List['RoleBare']):
        department_id (Union[Unset, int]):
        post (Union[Unset, str]):
        permissions (Union[Unset, List[str]]):
        login (Union[Unset, str]):
        middle_name (Union[Unset, str]):
        birthday (Union[Unset, datetime.date]):
        phone (Union[Unset, str]):
        priority (Union[Unset, int]):
        department (Union[Unset, DepartmentBare]): Промежуточная модель pydantic'а для унифицирования конфигов и
            удобного администрирования
    """

    id: int
    email: str
    last_name: str
    first_name: str
    updated_at: datetime.datetime
    roles: List["RoleBare"]
    department_id: Union[Unset, int] = UNSET
    post: Union[Unset, str] = UNSET
    permissions: Union[Unset, List[str]] = UNSET
    login: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    birthday: Union[Unset, datetime.date] = UNSET
    phone: Union[Unset, str] = UNSET
    priority: Union[Unset, int] = UNSET
    department: Union[Unset, "DepartmentBare"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        email = self.email

        last_name = self.last_name

        first_name = self.first_name

        updated_at = self.updated_at.isoformat()

        roles = []
        for roles_item_data in self.roles:
            roles_item = roles_item_data.to_dict()
            roles.append(roles_item)

        department_id = self.department_id

        post = self.post

        permissions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions

        login = self.login

        middle_name = self.middle_name

        birthday: Union[Unset, str] = UNSET
        if not isinstance(self.birthday, Unset):
            birthday = self.birthday.isoformat()

        phone = self.phone

        priority = self.priority

        department: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.department, Unset):
            department = self.department.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
                "lastName": last_name,
                "firstName": first_name,
                "updatedAt": updated_at,
                "roles": roles,
            }
        )
        if department_id is not UNSET:
            field_dict["departmentId"] = department_id
        if post is not UNSET:
            field_dict["post"] = post
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if login is not UNSET:
            field_dict["login"] = login
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if birthday is not UNSET:
            field_dict["birthday"] = birthday
        if phone is not UNSET:
            field_dict["phone"] = phone
        if priority is not UNSET:
            field_dict["priority"] = priority
        if department is not UNSET:
            field_dict["department"] = department

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.department_bare import DepartmentBare
        from ..models.role_bare import RoleBare

        d = src_dict.copy()
        id = d.pop("id")

        email = d.pop("email")

        last_name = d.pop("lastName")

        first_name = d.pop("firstName")

        updated_at = isoparse(d.pop("updatedAt"))

        roles = []
        _roles = d.pop("roles")
        for roles_item_data in _roles:
            roles_item = RoleBare.from_dict(roles_item_data)

            roles.append(roles_item)

        department_id = d.pop("departmentId", UNSET)

        post = d.pop("post", UNSET)

        permissions = cast(List[str], d.pop("permissions", UNSET))

        login = d.pop("login", UNSET)

        middle_name = d.pop("middleName", UNSET)

        _birthday = d.pop("birthday", UNSET)
        birthday: Union[Unset, datetime.date]
        if isinstance(_birthday, Unset) or _birthday is None:
            birthday = UNSET
        else:
            birthday = isoparse(_birthday).date()

        phone = d.pop("phone", UNSET)

        priority = d.pop("priority", UNSET)

        _department = d.pop("department", UNSET)
        department: Union[Unset, DepartmentBare]
        if isinstance(_department, Unset):
            department = UNSET
        else:
            department = DepartmentBare.from_dict(_department)

        user_info_out = cls(
            id=id,
            email=email,
            last_name=last_name,
            first_name=first_name,
            updated_at=updated_at,
            roles=roles,
            department_id=department_id,
            post=post,
            permissions=permissions,
            login=login,
            middle_name=middle_name,
            birthday=birthday,
            phone=phone,
            priority=priority,
            department=department,
        )

        user_info_out.additional_properties = d
        return user_info_out

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
