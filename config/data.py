import os
from enum import Enum

from dotenv import load_dotenv

load_dotenv()


class Data:
    """The data class."""

    def __init__(self) -> None:
        """Initialize data class with credentials from environment variables."""
        self.USERNAME: str | None = os.getenv("PARABANK_USERNAME")
        self.PASSWORD: str | None = os.getenv("PARABANK_PASSWORD")


class AccountType(Enum):
    """Available account types."""

    SAVINGS = "SAVINGS"
    CHECKING = "CHECKING"
