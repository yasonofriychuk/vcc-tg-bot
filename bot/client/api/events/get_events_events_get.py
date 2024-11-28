import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_list import EventList
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: Union[Unset, int] = 1,
    rows_per_page: Union[Unset, int] = 25,
    from_datetime: Union[Unset, datetime.datetime] = UNSET,
    to_datetime: Union[Unset, datetime.datetime] = UNSET,
    is_offline: Union[Unset, bool] = UNSET,
    room_id: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = "id",
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["page"] = page

    params["rowsPerPage"] = rows_per_page

    json_from_datetime: Union[Unset, str] = UNSET
    if not isinstance(from_datetime, Unset):
        json_from_datetime = from_datetime.isoformat()
    params["from_datetime"] = json_from_datetime

    json_to_datetime: Union[Unset, str] = UNSET
    if not isinstance(to_datetime, Unset):
        json_to_datetime = to_datetime.isoformat()
    params["to_datetime"] = json_to_datetime

    params["is_offline"] = is_offline

    params["room_id"] = room_id

    params["name"] = name

    params["sort_by"] = sort_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, EventList, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = EventList.from_dict(response.json())

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
) -> Response[Union[Any, EventList, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    rows_per_page: Union[Unset, int] = 25,
    from_datetime: Union[Unset, datetime.datetime] = UNSET,
    to_datetime: Union[Unset, datetime.datetime] = UNSET,
    is_offline: Union[Unset, bool] = UNSET,
    room_id: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = "id",
) -> Response[Union[Any, EventList, HTTPValidationError]]:
    """Get Events

     Получение всех событий, доступных в системе

    Args:
        page (Union[Unset, int]):  Default: 1.
        rows_per_page (Union[Unset, int]):  Default: 25.
        from_datetime (Union[Unset, datetime.datetime]):
        to_datetime (Union[Unset, datetime.datetime]):
        is_offline (Union[Unset, bool]): Оффлайн событие вне системы
        room_id (Union[Unset, int]): Идентификатор комнаты, в которой проводятся события
        name (Union[Unset, str]):
        sort_by (Union[Unset, str]):  Default: 'id'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventList, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        page=page,
        rows_per_page=rows_per_page,
        from_datetime=from_datetime,
        to_datetime=to_datetime,
        is_offline=is_offline,
        room_id=room_id,
        name=name,
        sort_by=sort_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    rows_per_page: Union[Unset, int] = 25,
    from_datetime: Union[Unset, datetime.datetime] = UNSET,
    to_datetime: Union[Unset, datetime.datetime] = UNSET,
    is_offline: Union[Unset, bool] = UNSET,
    room_id: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = "id",
) -> Optional[Union[Any, EventList, HTTPValidationError]]:
    """Get Events

     Получение всех событий, доступных в системе

    Args:
        page (Union[Unset, int]):  Default: 1.
        rows_per_page (Union[Unset, int]):  Default: 25.
        from_datetime (Union[Unset, datetime.datetime]):
        to_datetime (Union[Unset, datetime.datetime]):
        is_offline (Union[Unset, bool]): Оффлайн событие вне системы
        room_id (Union[Unset, int]): Идентификатор комнаты, в которой проводятся события
        name (Union[Unset, str]):
        sort_by (Union[Unset, str]):  Default: 'id'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EventList, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        page=page,
        rows_per_page=rows_per_page,
        from_datetime=from_datetime,
        to_datetime=to_datetime,
        is_offline=is_offline,
        room_id=room_id,
        name=name,
        sort_by=sort_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    rows_per_page: Union[Unset, int] = 25,
    from_datetime: Union[Unset, datetime.datetime] = UNSET,
    to_datetime: Union[Unset, datetime.datetime] = UNSET,
    is_offline: Union[Unset, bool] = UNSET,
    room_id: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = "id",
) -> Response[Union[Any, EventList, HTTPValidationError]]:
    """Get Events

     Получение всех событий, доступных в системе

    Args:
        page (Union[Unset, int]):  Default: 1.
        rows_per_page (Union[Unset, int]):  Default: 25.
        from_datetime (Union[Unset, datetime.datetime]):
        to_datetime (Union[Unset, datetime.datetime]):
        is_offline (Union[Unset, bool]): Оффлайн событие вне системы
        room_id (Union[Unset, int]): Идентификатор комнаты, в которой проводятся события
        name (Union[Unset, str]):
        sort_by (Union[Unset, str]):  Default: 'id'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventList, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        page=page,
        rows_per_page=rows_per_page,
        from_datetime=from_datetime,
        to_datetime=to_datetime,
        is_offline=is_offline,
        room_id=room_id,
        name=name,
        sort_by=sort_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = 1,
    rows_per_page: Union[Unset, int] = 25,
    from_datetime: Union[Unset, datetime.datetime] = UNSET,
    to_datetime: Union[Unset, datetime.datetime] = UNSET,
    is_offline: Union[Unset, bool] = UNSET,
    room_id: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = "id",
) -> Optional[Union[Any, EventList, HTTPValidationError]]:
    """Get Events

     Получение всех событий, доступных в системе

    Args:
        page (Union[Unset, int]):  Default: 1.
        rows_per_page (Union[Unset, int]):  Default: 25.
        from_datetime (Union[Unset, datetime.datetime]):
        to_datetime (Union[Unset, datetime.datetime]):
        is_offline (Union[Unset, bool]): Оффлайн событие вне системы
        room_id (Union[Unset, int]): Идентификатор комнаты, в которой проводятся события
        name (Union[Unset, str]):
        sort_by (Union[Unset, str]):  Default: 'id'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EventList, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            rows_per_page=rows_per_page,
            from_datetime=from_datetime,
            to_datetime=to_datetime,
            is_offline=is_offline,
            room_id=room_id,
            name=name,
            sort_by=sort_by,
        )
    ).parsed
