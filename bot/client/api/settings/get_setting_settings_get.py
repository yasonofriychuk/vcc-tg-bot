from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.meeting_backend import MeetingBackend
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    backend: Union[Unset, MeetingBackend] = MeetingBackend.VINTEO,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_backend: Union[Unset, str] = UNSET
    if not isinstance(backend, Unset):
        json_backend = backend.value

    params["backend"] = json_backend

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/settings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    backend: Union[Unset, MeetingBackend] = MeetingBackend.VINTEO,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get Setting

     Получение информации о глобальных настройках средства связи.

    Args:
        backend (Union[Unset, MeetingBackend]): Поддерживаемый вариант запуска ВКС.

            На данный момент на уровне API поддерживается только cisco,
            всё остальное рассматривается как внешний сервис, для которого нет интеграции Default:
            MeetingBackend.VINTEO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        backend=backend,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    backend: Union[Unset, MeetingBackend] = MeetingBackend.VINTEO,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get Setting

     Получение информации о глобальных настройках средства связи.

    Args:
        backend (Union[Unset, MeetingBackend]): Поддерживаемый вариант запуска ВКС.

            На данный момент на уровне API поддерживается только cisco,
            всё остальное рассматривается как внешний сервис, для которого нет интеграции Default:
            MeetingBackend.VINTEO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        backend=backend,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    backend: Union[Unset, MeetingBackend] = MeetingBackend.VINTEO,
) -> Response[Union[Any, HTTPValidationError]]:
    """Get Setting

     Получение информации о глобальных настройках средства связи.

    Args:
        backend (Union[Unset, MeetingBackend]): Поддерживаемый вариант запуска ВКС.

            На данный момент на уровне API поддерживается только cisco,
            всё остальное рассматривается как внешний сервис, для которого нет интеграции Default:
            MeetingBackend.VINTEO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        backend=backend,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    backend: Union[Unset, MeetingBackend] = MeetingBackend.VINTEO,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Get Setting

     Получение информации о глобальных настройках средства связи.

    Args:
        backend (Union[Unset, MeetingBackend]): Поддерживаемый вариант запуска ВКС.

            На данный момент на уровне API поддерживается только cisco,
            всё остальное рассматривается как внешний сервис, для которого нет интеграции Default:
            MeetingBackend.VINTEO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            backend=backend,
        )
    ).parsed
