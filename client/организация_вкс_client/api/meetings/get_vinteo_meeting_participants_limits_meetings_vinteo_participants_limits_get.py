import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.vinteo_participants_limit_out import VinteoParticipantsLimitOut
from ...types import UNSET, Response


def _get_kwargs(
    *,
    from_period: datetime.datetime,
    to_period: datetime.datetime,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_from_period = from_period.isoformat()
    params["fromPeriod"] = json_from_period

    json_to_period = to_period.isoformat()
    params["toPeriod"] = json_to_period

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/meetings/vinteo/participants-limits",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, VinteoParticipantsLimitOut]]:
    if response.status_code == 200:
        response_200 = VinteoParticipantsLimitOut.from_dict(response.json())

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
) -> Response[Union[Any, HTTPValidationError, VinteoParticipantsLimitOut]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    from_period: datetime.datetime,
    to_period: datetime.datetime,
) -> Response[Union[Any, HTTPValidationError, VinteoParticipantsLimitOut]]:
    """Get Vinteo Meeting Participants Limits

     Получение информации о нагруженности vinteo сервера на конкретный период времени.

    Args:
        from_period (datetime.datetime): Начало временного промежутка для проверки
        to_period (datetime.datetime): Конец временного промежутка для проверки

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, VinteoParticipantsLimitOut]]
    """

    kwargs = _get_kwargs(
        from_period=from_period,
        to_period=to_period,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    from_period: datetime.datetime,
    to_period: datetime.datetime,
) -> Optional[Union[Any, HTTPValidationError, VinteoParticipantsLimitOut]]:
    """Get Vinteo Meeting Participants Limits

     Получение информации о нагруженности vinteo сервера на конкретный период времени.

    Args:
        from_period (datetime.datetime): Начало временного промежутка для проверки
        to_period (datetime.datetime): Конец временного промежутка для проверки

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, VinteoParticipantsLimitOut]
    """

    return sync_detailed(
        client=client,
        from_period=from_period,
        to_period=to_period,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    from_period: datetime.datetime,
    to_period: datetime.datetime,
) -> Response[Union[Any, HTTPValidationError, VinteoParticipantsLimitOut]]:
    """Get Vinteo Meeting Participants Limits

     Получение информации о нагруженности vinteo сервера на конкретный период времени.

    Args:
        from_period (datetime.datetime): Начало временного промежутка для проверки
        to_period (datetime.datetime): Конец временного промежутка для проверки

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, VinteoParticipantsLimitOut]]
    """

    kwargs = _get_kwargs(
        from_period=from_period,
        to_period=to_period,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    from_period: datetime.datetime,
    to_period: datetime.datetime,
) -> Optional[Union[Any, HTTPValidationError, VinteoParticipantsLimitOut]]:
    """Get Vinteo Meeting Participants Limits

     Получение информации о нагруженности vinteo сервера на конкретный период времени.

    Args:
        from_period (datetime.datetime): Начало временного промежутка для проверки
        to_period (datetime.datetime): Конец временного промежутка для проверки

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, VinteoParticipantsLimitOut]
    """

    return (
        await asyncio_detailed(
            client=client,
            from_period=from_period,
            to_period=to_period,
        )
    ).parsed
