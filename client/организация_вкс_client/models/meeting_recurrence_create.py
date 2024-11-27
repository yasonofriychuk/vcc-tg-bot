import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.meeting_recurrence_frequency import MeetingRecurrenceFrequency
from ..models.meeting_recurrence_weekday import MeetingRecurrenceWeekday
from ..types import UNSET, Unset

T = TypeVar("T", bound="MeetingRecurrenceCreate")


@_attrs_define
class MeetingRecurrenceCreate:
    """Промежуточная модель pydantic'а для унифицирования конфигов и удобного администрирования

    Attributes:
        frequency (MeetingRecurrenceFrequency): An enumeration.
        started_at (datetime.datetime): Дата, начиная с которой будут повторяться ВКС
        interval (Union[Unset, int]): Интервал между каждой итерацией повторения Default: 1.
        count (Union[Unset, int]): Сколько раз должно повториться ВКС (допустимо указывать без until)
        until (Union[Unset, datetime.datetime]): Дата, до которой ВКС будет повторяться (допустимо указывать без count)
        week_days (Union[Unset, List[MeetingRecurrenceWeekday]]): Дни недели, в которые будет применяться повторение
        additional_dates (Union[Unset, List[datetime.datetime]]): Дополнительные даты ВКС, которые не входят в основное
            правило
        exclude_dates (Union[Unset, List[datetime.datetime]]): Даты, которые нужно исключить из основного правила
    """

    frequency: MeetingRecurrenceFrequency
    started_at: datetime.datetime
    interval: Union[Unset, int] = 1
    count: Union[Unset, int] = UNSET
    until: Union[Unset, datetime.datetime] = UNSET
    week_days: Union[Unset, List[MeetingRecurrenceWeekday]] = UNSET
    additional_dates: Union[Unset, List[datetime.datetime]] = UNSET
    exclude_dates: Union[Unset, List[datetime.datetime]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        frequency = self.frequency.value

        started_at = self.started_at.isoformat()

        interval = self.interval

        count = self.count

        until: Union[Unset, str] = UNSET
        if not isinstance(self.until, Unset):
            until = self.until.isoformat()

        week_days: Union[Unset, List[int]] = UNSET
        if not isinstance(self.week_days, Unset):
            week_days = []
            for week_days_item_data in self.week_days:
                week_days_item = week_days_item_data.value
                week_days.append(week_days_item)

        additional_dates: Union[Unset, List[str]] = UNSET
        if not isinstance(self.additional_dates, Unset):
            additional_dates = []
            for additional_dates_item_data in self.additional_dates:
                additional_dates_item = additional_dates_item_data.isoformat()
                additional_dates.append(additional_dates_item)

        exclude_dates: Union[Unset, List[str]] = UNSET
        if not isinstance(self.exclude_dates, Unset):
            exclude_dates = []
            for exclude_dates_item_data in self.exclude_dates:
                exclude_dates_item = exclude_dates_item_data.isoformat()
                exclude_dates.append(exclude_dates_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "frequency": frequency,
                "startedAt": started_at,
            }
        )
        if interval is not UNSET:
            field_dict["interval"] = interval
        if count is not UNSET:
            field_dict["count"] = count
        if until is not UNSET:
            field_dict["until"] = until
        if week_days is not UNSET:
            field_dict["weekDays"] = week_days
        if additional_dates is not UNSET:
            field_dict["additionalDates"] = additional_dates
        if exclude_dates is not UNSET:
            field_dict["excludeDates"] = exclude_dates

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        frequency = MeetingRecurrenceFrequency(d.pop("frequency"))

        started_at = isoparse(d.pop("startedAt"))

        interval = d.pop("interval", UNSET)

        count = d.pop("count", UNSET)

        _until = d.pop("until", UNSET)
        until: Union[Unset, datetime.datetime]
        if isinstance(_until, Unset):
            until = UNSET
        else:
            until = isoparse(_until)

        week_days = []
        _week_days = d.pop("weekDays", UNSET)
        for week_days_item_data in _week_days or []:
            week_days_item = MeetingRecurrenceWeekday(week_days_item_data)

            week_days.append(week_days_item)

        additional_dates = []
        _additional_dates = d.pop("additionalDates", UNSET)
        for additional_dates_item_data in _additional_dates or []:
            additional_dates_item = isoparse(additional_dates_item_data)

            additional_dates.append(additional_dates_item)

        exclude_dates = []
        _exclude_dates = d.pop("excludeDates", UNSET)
        for exclude_dates_item_data in _exclude_dates or []:
            exclude_dates_item = isoparse(exclude_dates_item_data)

            exclude_dates.append(exclude_dates_item)

        meeting_recurrence_create = cls(
            frequency=frequency,
            started_at=started_at,
            interval=interval,
            count=count,
            until=until,
            week_days=week_days,
            additional_dates=additional_dates,
            exclude_dates=exclude_dates,
        )

        meeting_recurrence_create.additional_properties = d
        return meeting_recurrence_create

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
