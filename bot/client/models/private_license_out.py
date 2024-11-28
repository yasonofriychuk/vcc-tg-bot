import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="PrivateLicenseOut")


@_attrs_define
class PrivateLicenseOut:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        email (str):  Example: test_email@email.com.
        id (int):
        created_at (datetime.datetime):
    """

    email: str
    id: int
    created_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email

        id = self.id

        created_at = self.created_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "id": id,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email")

        id = d.pop("id")

        created_at = isoparse(d.pop("createdAt"))

        private_license_out = cls(
            email=email,
            id=id,
            created_at=created_at,
        )

        private_license_out.additional_properties = d
        return private_license_out

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
