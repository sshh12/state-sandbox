from typing import TypeVar, Callable, AsyncGenerator, Any
import asyncio
from fastapi.responses import StreamingResponse
from dataclasses import dataclass

from routers.schemas import HeartbeatEvent

T = TypeVar("T")


@dataclass
class HeartbeatResult:
    event: str


async def heartbeat() -> AsyncGenerator[str, None]:
    """Generate heartbeat events every 2 seconds."""
    while True:
        await asyncio.sleep(2)
        yield HeartbeatEvent().json_line()


async def with_heartbeat(
    stream: AsyncGenerator[str, None]
) -> AsyncGenerator[str, None]:
    """
    Wrapper to add heartbeat events to a stream.

    Args:
        stream: Original event stream

    Yields:
        str: Events from original stream interspersed with heartbeat events
    """
    heartbeat_task = asyncio.create_task(heartbeat().__anext__())
    stream_task = asyncio.create_task(stream.__anext__())

    try:
        while True:
            done, _ = await asyncio.wait(
                [heartbeat_task, stream_task], return_when=asyncio.FIRST_COMPLETED
            )

            if stream_task in done:
                try:
                    yield await stream_task
                    stream_task = asyncio.create_task(stream.__anext__())
                except StopAsyncIteration:
                    break

            if heartbeat_task in done:
                yield await heartbeat_task
                heartbeat_task = asyncio.create_task(heartbeat().__anext__())

    finally:
        heartbeat_task.cancel()
        stream_task.cancel()
        try:
            await heartbeat_task
            await stream_task
        except (asyncio.CancelledError, StopAsyncIteration):
            pass


def event_stream_response(stream: AsyncGenerator[str, None]) -> StreamingResponse:
    """
    Helper to create a StreamingResponse with proper media type and heartbeat events.

    Args:
        stream: Async generator yielding event strings

    Returns:
        StreamingResponse configured for server-sent events with heartbeat
    """
    return StreamingResponse(with_heartbeat(stream), media_type="text/event-stream")
