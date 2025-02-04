from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy.orm import Session
import stripe
import logging

from config import STRIPE_SECRET_KEY, STRIPE_WEBHOOK_SECRET
from db.database import get_db
from db.models import User


router = APIRouter(prefix="/api/stripe", tags=["stripe"])


stripe.api_key = STRIPE_SECRET_KEY

CREDITS_PER_PURCHASE = 60


async def on_session_completed(session: stripe.checkout.Session, db: Session):
    """Handle successful checkout session completion"""
    try:
        if "statesandbox" not in session.client_reference_id:
            print(f"stripe: Skipping purchase for {session.client_reference_id}")
            return

        user_id = int(
            session.client_reference_id.split("___")[1].replace("ssuser_", "")
        )

        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        # Update user credits
        user.credits += CREDITS_PER_PURCHASE
        db.commit()

        print(f"stripe: Successfully processed purchase for user {user_id}")

    except Exception as e:
        db.rollback()
        print(f"stripe: Error processing session completion: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/stripe-hook")
async def stripe_webhook(request: Request, db: Session = Depends(get_db)):
    stripe_signature = request.headers.get("stripe-signature")
    if not stripe_signature:
        raise HTTPException(status_code=400, detail="No stripe signature")

    body = await request.body()

    try:
        event = stripe.Webhook.construct_event(
            payload=body,
            sig_header=stripe_signature,
            secret=STRIPE_WEBHOOK_SECRET,
        )
    except stripe.error.SignatureVerificationError as e:
        print(f"stripe: Invalid signature: {str(e)}")
        raise HTTPException(status_code=400, detail="Invalid signature")
    except Exception as e:
        print(f"stripe: Error constructing webhook event: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

    try:
        if event.type == "checkout.session.completed":
            await on_session_completed(event.data.object, db)
        elif event.type == "payment_intent.succeeded":
            logging.info(f"stripe: Payment intent succeeded: {event.data.object.id}")
        else:
            logging.info(f"stripe: Unhandled event type {event.type}")

        return {"success": True}

    except Exception as e:
        error_msg = f"stripe: Error processing webhook event: {str(e)}"
        print(error_msg)
        return {"success": False, "error": error_msg}
