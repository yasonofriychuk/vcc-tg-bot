import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx
from dateutil.parser import isoparse

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.meeting_states import MeetingStates
from ...models.meetings_calendar_list import MeetingsCalendarList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_date: Union[Unset, datetime.date] = isoparse("2024-11-27").date(),
    end_date: Union[Unset, datetime.date] = isoparse("2024-12-27").date(),
    department_id: Union[Unset, int] = UNSET,
    states: Union[Unset, List[MeetingStates]] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    json_end_date: Union[Unset, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    params["departmentId"] = department_id

    json_states: Union[Unset, List[str]] = UNSET
    if not isinstance(states, Unset):
        json_states = []
        for states_item_data in states:
            states_item = states_item_data.value
            json_states.append(states_item)

    params["states"] = json_states

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/statistics/meetings-calendar",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, MeetingsCalendarList]]:
    if response.status_code == 200:
        response_200 = MeetingsCalendarList.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == 410:
        response_410 = cast(Any, None)
        return response_410
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError, MeetingsCalendarList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, datetime.date] = isoparse("2024-11-27").date(),
    end_date: Union[Unset, datetime.date] = isoparse("2024-12-27").date(),
    department_id: Union[Unset, int] = UNSET,
    states: Union[Unset, List[MeetingStates]] = UNSET,
) -> Response[Union[Any, HTTPValidationError, MeetingsCalendarList]]:
    """Get Meetings Calendar

     Календарь ВКС

    Args:
        start_date (Union[Unset, datetime.date]):  Default: isoparse('2024-11-27').date().
        end_date (Union[Unset, datetime.date]):  Default: isoparse('2024-12-27').date().
        department_id (Union[Unset, int]):
        states (Union[Unset, List[MeetingStates]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, MeetingsCalendarList]]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        department_id=department_id,
        states=states,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, datetime.date] = isoparse("2024-11-27").date(),
    end_date: Union[Unset, datetime.date] = isoparse("2024-12-27").date(),
    department_id: Union[Unset, int] = UNSET,
    states: Union[Unset, List[MeetingStates]] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, MeetingsCalendarList]]:
    """Get Meetings Calendar

     Календарь ВКС

    Args:
        start_date (Union[Unset, datetime.date]):  Default: isoparse('2024-11-27').date().
        end_date (Union[Unset, datetime.date]):  Default: isoparse('2024-12-27').date().
        department_id (Union[Unset, int]):
        states (Union[Unset, List[MeetingStates]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, MeetingsCalendarList]
    """

    return sync_detailed(
        client=client,
        start_date=start_date,
        end_date=end_date,
        department_id=department_id,
        states=states,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, datetime.date] = isoparse("2024-11-27").date(),
    end_date: Union[Unset, datetime.date] = isoparse("2024-12-27").date(),
    department_id: Union[Unset, int] = UNSET,
    states: Union[Unset, List[MeetingStates]] = UNSET,
) -> Response[Union[Any, HTTPValidationError, MeetingsCalendarList]]:
    """Get Meetings Calendar

     Календарь ВКС

    Args:
        start_date (Union[Unset, datetime.date]):  Default: isoparse('2024-11-27').date().
        end_date (Union[Unset, datetime.date]):  Default: isoparse('2024-12-27').date().
        department_id (Union[Unset, int]):
        states (Union[Unset, List[MeetingStates]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, MeetingsCalendarList]]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        department_id=department_id,
        states=states,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, datetime.date] = isoparse("2024-11-27").date(),
    end_date: Union[Unset, datetime.date] = isoparse("2024-12-27").date(),
    department_id: Union[Unset, int] = UNSET,
    states: Union[Unset, List[MeetingStates]] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, MeetingsCalendarList]]:
    """Get Meetings Calendar

     Календарь ВКС

    Args:
        start_date (Union[Unset, datetime.date]):  Default: isoparse('2024-11-27').date().
        end_date (Union[Unset, datetime.date]):  Default: isoparse('2024-12-27').date().
        department_id (Union[Unset, int]):
        states (Union[Unset, List[MeetingStates]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, MeetingsCalendarList]
    """

    return (
        await asyncio_detailed(
            client=client,
            start_date=start_date,
            end_date=end_date,
            department_id=department_id,
            states=states,
        )
    ).parsed
