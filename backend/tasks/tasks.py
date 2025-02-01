import asyncio
from sqlalchemy import update

from db.database import SessionLocal
from db.models import State


async def reset_stuck_states():
    """Reset any states that have been stuck in progress for too long."""
    while True:
        try:
            print("Resetting stuck states")
            db = SessionLocal()
            db.execute(
                update(State)
                .where(State.turn_in_progress == True)
                .values(turn_in_progress=False)
            )
            db.commit()
        except Exception as e:
            print(f"Error resetting stuck states: {e}")
        finally:
            db.close()
        await asyncio.sleep(600)
