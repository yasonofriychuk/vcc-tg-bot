from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.room_full import RoomFull
from ...types import Response


def _get_kwargs(
    room_id: int,
    user_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/catalogs/rooms/{room_id}/user/{user_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, RoomFull]]:
    if response.status_code == 200:
        response_200 = RoomFull.from_dict(response.json())

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
) -> Response[Union[Any, HTTPValidationError, RoomFull]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    room_id: int,
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, HTTPValidationError, RoomFull]]:
    """Set Responsible User

     Определение ответственного пользователя за площадку.

    В дальнейшем, у него будет право отмены проведения ВКС,
     если на определённой площадке невозможно провести ВКС

    Args:
        room_id (int):
        user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, RoomFull]]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    room_id: int,
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, HTTPValidationError, RoomFull]]:
    """Set Responsible User

     Определение ответственного пользователя за площадку.

    В дальнейшем, у него будет право отмены проведения ВКС,
     если на определённой площадке невозможно провести ВКС

    Args:
        room_id (int):
        user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, RoomFull]
    """

    return sync_detailed(
        room_id=room_id,
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    room_id: int,
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, HTTPValidationError, RoomFull]]:
    """Set Responsible User

     Определение ответственного пользователя за площадку.

    В дальнейшем, у него будет право отмены проведения ВКС,
     если на определённой площадке невозможно провести ВКС

    Args:
        room_id (int):
        user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, RoomFull]]
    """

    kwargs = _get_kwargs(
        room_id=room_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    room_id: int,
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, HTTPValidationError, RoomFull]]:
    """Set Responsible User

     Определение ответственного пользователя за площадку.

    В дальнейшем, у него будет право отмены проведения ВКС,
     если на определённой площадке невозможно провести ВКС

    Args:
        room_id (int):
        user_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError, RoomFull]
    """

    return (
        await asyncio_detailed(
            room_id=room_id,
            user_id=user_id,
            client=client,
        )
    ).parsed
