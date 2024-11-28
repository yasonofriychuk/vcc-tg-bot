import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx
from dateutil.parser import isoparse

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cumulative_meetings import CumulativeMeetings
from ...models.cumulative_type import CumulativeType
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_date: Union[Unset, datetime.date] = isoparse("2024-11-20").date(),
    end_date: Union[Unset, datetime.date] = isoparse("2024-11-27").date(),
    department_id: Union[Unset, int] = UNSET,
    cumulative_type: Union[Unset, CumulativeType] = CumulativeType.MEETINGS,
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

    json_cumulative_type: Union[Unset, str] = UNSET
    if not isinstance(cumulative_type, Unset):
        json_cumulative_type = cumulative_type.value

    params["cumulativeType"] = json_cumulative_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/statistics/meetings-cumulative",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CumulativeMeetings, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = CumulativeMeetings.from_dict(response.json())

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
) -> Response[Union[Any, CumulativeMeetings, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, datetime.date] = isoparse("2024-11-20").date(),
    end_date: Union[Unset, datetime.date] = isoparse("2024-11-27").date(),
    department_id: Union[Unset, int] = UNSET,
    cumulative_type: Union[Unset, CumulativeType] = CumulativeType.MEETINGS,
) -> Response[Union[Any, CumulativeMeetings, HTTPValidationError]]:
    """Get Meetings Cumulative

     Суммарное количество ВКС/участников за период накопительным итогом

    Args:
        start_date (Union[Unset, datetime.date]):  Default: isoparse('2024-11-20').date().
        end_date (Union[Unset, datetime.date]):  Default: isoparse('2024-11-27').date().
        department_id (Union[Unset, int]):
        cumulative_type (Union[Unset, CumulativeType]): An enumeration. Default:
            CumulativeType.MEETINGS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CumulativeMeetings, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        department_id=department_id,
        cumulative_type=cumulative_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, datetime.date] = isoparse("2024-11-20").date(),
    end_date: Union[Unset, datetime.date] = isoparse("2024-11-27").date(),
    department_id: Union[Unset, int] = UNSET,
    cumulative_type: Union[Unset, CumulativeType] = CumulativeType.MEETINGS,
) -> Optional[Union[Any, CumulativeMeetings, HTTPValidationError]]:
    """Get Meetings Cumulative

     Суммарное количество ВКС/участников за период накопительным итогом

    Args:
        start_date (Union[Unset, datetime.date]):  Default: isoparse('2024-11-20').date().
        end_date (Union[Unset, datetime.date]):  Default: isoparse('2024-11-27').date().
        department_id (Union[Unset, int]):
        cumulative_type (Union[Unset, CumulativeType]): An enumeration. Default:
            CumulativeType.MEETINGS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CumulativeMeetings, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        start_date=start_date,
        end_date=end_date,
        department_id=department_id,
        cumulative_type=cumulative_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, datetime.date] = isoparse("2024-11-20").date(),
    end_date: Union[Unset, datetime.date] = isoparse("2024-11-27").date(),
    department_id: Union[Unset, int] = UNSET,
    cumulative_type: Union[Unset, CumulativeType] = CumulativeType.MEETINGS,
) -> Response[Union[Any, CumulativeMeetings, HTTPValidationError]]:
    """Get Meetings Cumulative

     Суммарное количество ВКС/участников за период накопительным итогом

    Args:
        start_date (Union[Unset, datetime.date]):  Default: isoparse('2024-11-20').date().
        end_date (Union[Unset, datetime.date]):  Default: isoparse('2024-11-27').date().
        department_id (Union[Unset, int]):
        cumulative_type (Union[Unset, CumulativeType]): An enumeration. Default:
            CumulativeType.MEETINGS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CumulativeMeetings, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        department_id=department_id,
        cumulative_type=cumulative_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start_date: Union[Unset, datetime.date] = isoparse("2024-11-20").date(),
    end_date: Union[Unset, datetime.date] = isoparse("2024-11-27").date(),
    department_id: Union[Unset, int] = UNSET,
    cumulative_type: Union[Unset, CumulativeType] = CumulativeType.MEETINGS,
) -> Optional[Union[Any, CumulativeMeetings, HTTPValidationError]]:
    """Get Meetings Cumulative

     Суммарное количество ВКС/участников за период накопительным итогом

    Args:
        start_date (Union[Unset, datetime.date]):  Default: isoparse('2024-11-20').date().
        end_date (Union[Unset, datetime.date]):  Default: isoparse('2024-11-27').date().
        department_id (Union[Unset, int]):
        cumulative_type (Union[Unset, CumulativeType]): An enumeration. Default:
            CumulativeType.MEETINGS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CumulativeMeetings, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            start_date=start_date,
            end_date=end_date,
            department_id=department_id,
            cumulative_type=cumulative_type,
        )
    ).parsed
