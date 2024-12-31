import os
import secrets


def _int_env(key, default: int = 0):
    return int(os.getenv(key, str(default)))


# Database configuration
DATABASE_URL = os.environ.get("DATABASE_URL", "")
DB_POOL_SIZE = _int_env("DB_POOL_SIZE", 50)
DB_MAX_OVERFLOW = _int_env("DB_MAX_OVERFLOW", 50)
DB_POOL_RECYCLE = _int_env("DB_POOL_RECYCLE", 1800)  # 30 minutes in seconds

# Secrets configuration
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", secrets.token_urlsafe(32))
JWT_EXPIRATION_DAYS = _int_env(
    "JWT_EXPIRATION_DAYS", 10_000
)  # We don't have a sign back in feature

# OpenAI configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
