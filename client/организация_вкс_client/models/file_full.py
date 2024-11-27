from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_brief import UserBrief


T = TypeVar("T", bound="FileFull")


@_attrs_define
class FileFull:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        name (str):
        id (str):
        created_user (UserBrief): Промежуточная модель pydantic'а для унифицирования конфигов и удобного
            администрирования
    """

    name: str
    id: str
    created_user: "UserBrief"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        id = self.id

        created_user = self.created_user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "id": id,
                "createdUser": created_user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_brief import UserBrief

        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id")

        created_user = UserBrief.from_dict(d.pop("createdUser"))

        file_full = cls(
            name=name,
            id=id,
            created_user=created_user,
        )

        file_full.additional_properties = d
        return file_full

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
