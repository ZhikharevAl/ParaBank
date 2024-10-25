import os

from dotenv import load_dotenv

load_dotenv()


class Data:
    """The data class."""

    USERNAME: str | None = os.getenv("PARABANK_USERNAME")
    PASSWORD: str | None = os.getenv("PARABANK_PASSWORD")

    if not USERNAME or not PASSWORD:
        msg: str = "Please set PARABANK_USERNAME and PARABANK_PASSWORD in .env file"
        raise ValueError(msg)
