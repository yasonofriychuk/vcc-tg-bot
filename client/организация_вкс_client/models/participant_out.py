from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ParticipantOut")


@_attrs_define
class ParticipantOut:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        id (int):  Example: 1.
        email (str):
        last_name (Union[Unset, str]):  Default: ''.
        first_name (Union[Unset, str]):  Default: ''.
        middle_name (Union[Unset, str]):
        is_approved (Union[Unset, bool]): Подтвердил ли пользовать участи в ВКС (через средство уведомления, например,
            почту)
    """

    id: int
    email: str
    last_name: Union[Unset, str] = ""
    first_name: Union[Unset, str] = ""
    middle_name: Union[Unset, str] = UNSET
    is_approved: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        email = self.email

        last_name = self.last_name

        first_name = self.first_name

        middle_name = self.middle_name

        is_approved = self.is_approved

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
            }
        )
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if is_approved is not UNSET:
            field_dict["isApproved"] = is_approved

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        email = d.pop("email")

        last_name = d.pop("lastName", UNSET)

        first_name = d.pop("firstName", UNSET)

        middle_name = d.pop("middleName", UNSET)

        is_approved = d.pop("isApproved", UNSET)

        participant_out = cls(
            id=id,
            email=email,
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
            is_approved=is_approved,
        )

        participant_out.additional_properties = d
        return participant_out

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
