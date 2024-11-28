from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CiscoRoomPublicBare")


@_attrs_define
class CiscoRoomPublicBare:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        connect_url (Union[Unset, str]): Ссылка для подключения к ВКС для обычных пользователей
        room_uri (Union[Unset, str]): SIP код
        sip_domain_url (Union[Unset, str]): SIP адрес для подключения через домен
        sip_ip_url (Union[Unset, str]): SIP адрес для подключения через адрес
        call_id (Union[Unset, str]): Идентификатор ВКС для обычных пользователей, его можно ввести в поле "Идентификатор
            совещания"
    """

    connect_url: Union[Unset, str] = UNSET
    room_uri: Union[Unset, str] = UNSET
    sip_domain_url: Union[Unset, str] = UNSET
    sip_ip_url: Union[Unset, str] = UNSET
    call_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connect_url = self.connect_url

        room_uri = self.room_uri

        sip_domain_url = self.sip_domain_url

        sip_ip_url = self.sip_ip_url

        call_id = self.call_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connect_url is not UNSET:
            field_dict["connectUrl"] = connect_url
        if room_uri is not UNSET:
            field_dict["roomUri"] = room_uri
        if sip_domain_url is not UNSET:
            field_dict["sipDomainUrl"] = sip_domain_url
        if sip_ip_url is not UNSET:
            field_dict["sipIpUrl"] = sip_ip_url
        if call_id is not UNSET:
            field_dict["callId"] = call_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connect_url = d.pop("connectUrl", UNSET)

        room_uri = d.pop("roomUri", UNSET)

        sip_domain_url = d.pop("sipDomainUrl", UNSET)

        sip_ip_url = d.pop("sipIpUrl", UNSET)

        call_id = d.pop("callId", UNSET)

        cisco_room_public_bare = cls(
            connect_url=connect_url,
            room_uri=room_uri,
            sip_domain_url=sip_domain_url,
            sip_ip_url=sip_ip_url,
            call_id=call_id,
        )

        cisco_room_public_bare.additional_properties = d
        return cisco_room_public_bare

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
