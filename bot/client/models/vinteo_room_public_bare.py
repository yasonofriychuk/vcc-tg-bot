from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VinteoRoomPublicBare")


@_attrs_define
class VinteoRoomPublicBare:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        id (int):  Example: 1.
        call_id (str): Номер конференции Vinteo
        connect_code (int): Пин-код для входа в конференцию
        connect_url (Union[Unset, str]): Ссылка для подключения к конференции
        sip_domain_url (Union[Unset, str]): SIP адрес для подключения через домен
        sip_ip_url (Union[Unset, str]): SIP адрес для подключения через адрес
    """

    id: int
    call_id: str
    connect_code: int
    connect_url: Union[Unset, str] = UNSET
    sip_domain_url: Union[Unset, str] = UNSET
    sip_ip_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        call_id = self.call_id

        connect_code = self.connect_code

        connect_url = self.connect_url

        sip_domain_url = self.sip_domain_url

        sip_ip_url = self.sip_ip_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "callId": call_id,
                "connectCode": connect_code,
            }
        )
        if connect_url is not UNSET:
            field_dict["connectUrl"] = connect_url
        if sip_domain_url is not UNSET:
            field_dict["sipDomainUrl"] = sip_domain_url
        if sip_ip_url is not UNSET:
            field_dict["sipIpUrl"] = sip_ip_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        call_id = d.pop("callId")

        connect_code = d.pop("connectCode")

        connect_url = d.pop("connectUrl", UNSET)

        sip_domain_url = d.pop("sipDomainUrl", UNSET)

        sip_ip_url = d.pop("sipIpUrl", UNSET)

        vinteo_room_public_bare = cls(
            id=id,
            call_id=call_id,
            connect_code=connect_code,
            connect_url=connect_url,
            sip_domain_url=sip_domain_url,
            sip_ip_url=sip_ip_url,
        )

        vinteo_room_public_bare.additional_properties = d
        return vinteo_room_public_bare

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
