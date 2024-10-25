import os

from dotenv import load_dotenv

load_dotenv()


class Data:
    """The data class."""

    USERNAME: str | None = os.getenv("PARABANK_USERNAME")
    PASSWORD: str | None = os.getenv("PARABANK_PASSWORD")

    print(  # noqa: T201
        "Available environment variables:",
        [k for k in os.environ.keys() if "PARA" in k],  # noqa: SIM118
    )
    print("USERNAME is set:", USERNAME is not None)  # noqa: T201
    print("PASSWORD is set:", PASSWORD is not None)  # noqa: T201
