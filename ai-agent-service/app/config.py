from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY"
)

KAFKA_BOOTSTRAP_SERVERS = os.getenv(
    "KAFKA_BOOTSTRAP_SERVERS"
)

POSTGRES_HOST = os.getenv(
    "POSTGRES_HOST"
)

POSTGRES_PORT = os.getenv(
    "POSTGRES_PORT"
)

POSTGRES_DB = os.getenv(
    "POSTGRES_DB"
)

POSTGRES_USER = os.getenv(
    "POSTGRES_USER"
)

POSTGRES_PASSWORD = os.getenv(
    "POSTGRES_PASSWORD"
)