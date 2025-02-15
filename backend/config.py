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
MODEL_HIGH_REASONING = os.getenv("MODEL_HIGH_REASONING", "o3-mini-2025-01-31")
MODEL_MEDIUM_REASONING = os.getenv("MODEL_MEDIUM_REASONING", "o3-mini-2025-01-31")
MODEL_LOW_REASONING = os.getenv(
    "MODEL_LOW_REASONING", "gpt-4o"
)  # model should support markdown

# Cache configuration
CACHE_TTL_STATES_LEADERBOARD = _int_env("CACHE_TTL_STATES_LEADERBOARD", 60 * 60 * 6)

# Misc configuration
FRONTEND_URL = os.getenv("FRONTEND_URL", "https://state.sshh.io")

# Credits config
CREDITS_DEFAULT = _int_env("CREDITS_DEFAULT", 10)
CREDITS_NEW_STATE_COST = _int_env("CREDITS_NEW_STATE_COST", 1)
CREDITS_NEXT_YEAR_COST = _int_env("CREDITS_NEXT_YEAR_COST", 1)

# Stripe configuration
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")

# Email configuration
POSTMARK_API_KEY = os.environ.get("POSTMARK_API_KEY")
EMAIL_FROM = os.environ.get("EMAIL_FROM", "no-reply@state.sshh.io")
EMAIL_LOGIN_JWT_EXPIRATION_DAYS = _int_env("EMAIL_LOGIN_JWT_EXPIRATION_DAYS", 1)
