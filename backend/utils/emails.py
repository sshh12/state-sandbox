from datetime import datetime, timedelta
from jose import jwt
from postmarker.core import PostmarkClient

from config import (
    JWT_SECRET_KEY,
    EMAIL_LOGIN_JWT_EXPIRATION_DAYS,
    FRONTEND_URL,
    EMAIL_FROM,
    POSTMARK_API_KEY,
)


def send_login_link(email: str) -> None:
    """Send a login link to the user's email."""
    # Generate a JWT token
    token = jwt.encode(
        {
            "email": email,
            "exp": datetime.now() + timedelta(days=EMAIL_LOGIN_JWT_EXPIRATION_DAYS),
        },
        JWT_SECRET_KEY,
        algorithm="HS256",
    )

    login_link = f"{FRONTEND_URL}/email-login?token={token}"

    html_content = f"""
    <html>
        <head></head>
        <body>
            <h1>Hello!</h1>
            <p>Here's your link: <a href="{login_link}">Login Link</a></p>
        </body>
    </html>
    """

    text_content = f"Hello!\n\nHere's your link: {login_link}"
    _send_email(email, "State Sandbox AI Login Link", html_content, text_content)


def _send_email(
    recipient_email: str, subject: str, html_content: str, text_content: str
):
    postmark = PostmarkClient(server_token=POSTMARK_API_KEY)
    postmark.emails.send(
        From=EMAIL_FROM,
        To=recipient_email,
        Subject=subject,
        HtmlBody=html_content,
        TextBody=text_content,
    )
