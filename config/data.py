import os

from dotenv import load_dotenv

load_dotenv()


class Data:
    """The data class."""

    USERNAME: str | None = os.getenv("PARABANK_USERNAME")
    PASSWORD: str | None = os.getenv("PARABANK_PASSWORD")
