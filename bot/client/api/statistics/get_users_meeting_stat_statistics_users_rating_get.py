import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx
from dateutil.parser import isoparse

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_meetings_list import UserMeetingsList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    top: Union[Unset, int] = 10,
    start_date: Union[Unset, datetime.date] = isoparse("2024-05-29").date(),
    end_date: Union[Unset, datetime.date] = isoparse("2025-05-29").date(),
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["top"] = top

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    json_end_date: Union[Unset, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/statistics/users-rating",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, UserMeetingsList]]:
    if response.status_code == 200:
        response_200 = UserMeetingsList.from_dict(response.json())

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
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError, UserMeetingsList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    top: Union[Unset, int] = 10,
    start_date: Union[Unset, datetime.date] = isoparse("2024-05-29").date(),
    end_date: Union[Unset, datetime.date] = isoparse("2025-05-29").date(),
) -> Response[Union[Any, HTTPValidationError, UserMeetingsList]]:
    """Get Users Meeting Stat

     Получение рейтинга пользователей. Критерий - количество участий в ВКС

    Args:
        top (Union[Unset, int]):  Default: 10.
        start_date (Union[Unset, datetime.date]):  Default: isoparse('2024-05-29').date().
        end_date (Union[Unset, datetime.date]):  Default: isoparse('2025-05-29').date().

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, UserMeetingsList]]
    """

    kwargs = _get_kwargs(
        top=top,
        start_date=start_date,
        end_date=end_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    top: Union[Unset, int] = 10,
    start_date: Union[Unset, datetime.date] = isoparse("2024-05-29").date(),
    end_date: Union[Unset, datetime.date] = isoparse("2025-05-29").date(),
) -> Optional[Union[Any, HTTPValidationError, UserMeetingsList]]:
    """Get Users Meeting Stat

     Получение рейтинга пользователей. Критерий - количество участий в ВКС

    Args:
        top (Union[Unset, int]):  Default: 10.
        start_date (Union[Unset, datetime.date]):  Default: isoparse('2024-05-29').date().
        end_date (Union[Unset, datetime.date]):  Default: isoparse('2025-05-29').date().

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, UserMeetingsList]
    """

    return sync_detailed(
        client=client,
        top=top,
        start_date=start_date,
        end_date=end_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    top: Union[Unset, int] = 10,
    start_date: Union[Unset, datetime.date] = isoparse("2024-05-29").date(),
    end_date: Union[Unset, datetime.date] = isoparse("2025-05-29").date(),
) -> Response[Union[Any, HTTPValidationError, UserMeetingsList]]:
    """Get Users Meeting Stat

     Получение рейтинга пользователей. Критерий - количество участий в ВКС

    Args:
        top (Union[Unset, int]):  Default: 10.
        start_date (Union[Unset, datetime.date]):  Default: isoparse('2024-05-29').date().
        end_date (Union[Unset, datetime.date]):  Default: isoparse('2025-05-29').date().

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, UserMeetingsList]]
    """

    kwargs = _get_kwargs(
        top=top,
        start_date=start_date,
        end_date=end_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    top: Union[Unset, int] = 10,
    start_date: Union[Unset, datetime.date] = isoparse("2024-05-29").date(),
    end_date: Union[Unset, datetime.date] = isoparse("2025-05-29").date(),
) -> Optional[Union[Any, HTTPValidationError, UserMeetingsList]]:
    """Get Users Meeting Stat

     Получение рейтинга пользователей. Критерий - количество участий в ВКС

    Args:
        top (Union[Unset, int]):  Default: 10.
        start_date (Union[Unset, datetime.date]):  Default: isoparse('2024-05-29').date().
        end_date (Union[Unset, datetime.date]):  Default: isoparse('2025-05-29').date().

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, UserMeetingsList]
    """

    return (
        await asyncio_detailed(
            client=client,
            top=top,
            start_date=start_date,
            end_date=end_date,
        )
    ).parsed