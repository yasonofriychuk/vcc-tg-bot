from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_brief import UserBrief


T = TypeVar("T", bound="TopByOrganizedUser")


@_attrs_define
class TopByOrganizedUser:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        count (int):
        user (UserBrief): Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования
    """

    count: int
    user: "UserBrief"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count

        user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "count": count,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_brief import UserBrief

        d = src_dict.copy()
        count = d.pop("count")

        user = UserBrief.from_dict(d.pop("user"))

        top_by_organized_user = cls(
            count=count,
            user=user,
        )

        top_by_organized_user.additional_properties = d
        return top_by_organized_user

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
