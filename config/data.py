import os

from dotenv import load_dotenv

load_dotenv()


class Data:
    """The data class."""

    USERNAME: str | None = os.getenv("PARABANK_USERNAME")
    PASSWORD: str | None = os.getenv("PARABANK_PASSWORD")

    if not USERNAME or not PASSWORD:
        msg: str = (
            "Environment variables PARABANK_USERNAME and PARABANK_PASSWORD are required. "
            "Set them either in .env file or as environment variables"
        )
        raise ValueError(msg)
