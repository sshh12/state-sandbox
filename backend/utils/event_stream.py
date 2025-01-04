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
    operation: Callable[[], T]
) -> AsyncGenerator[HeartbeatResult | T, None]:
    """
    Wrapper to run an async operation with heartbeat events.
    Yields heartbeat events while the operation is running.

    Args:
        operation: Async operation to run while sending heartbeats

    Yields:
        HeartbeatResult: Heartbeat events while operation is running
        T: Final result of the operation
    """
    heartbeat_task = asyncio.create_task(heartbeat().__anext__())
    operation_task = asyncio.create_task(operation())

    try:
        while not operation_task.done():
            done, _ = await asyncio.wait(
                [heartbeat_task, operation_task], return_when=asyncio.FIRST_COMPLETED
            )

            if heartbeat_task in done:
                yield HeartbeatResult(event=await heartbeat_task)
                heartbeat_task = asyncio.create_task(heartbeat().__anext__())

        yield await operation_task
    finally:
        heartbeat_task.cancel()
        try:
            await heartbeat_task
        except asyncio.CancelledError:
            pass


def event_stream_response(stream: AsyncGenerator[str, None]) -> Any:
    """
    Helper to create a StreamingResponse with proper media type.

    Args:
        stream: Async generator yielding event strings

    Returns:
        StreamingResponse configured for server-sent events
    """
    return StreamingResponse(stream, media_type="text/event-stream")
