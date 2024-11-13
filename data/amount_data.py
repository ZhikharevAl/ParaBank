from dataclasses import dataclass, field

from faker import Faker

fake = Faker()


@dataclass
class AmountData:
    """The amount data class."""

    amount: str = field(default_factory=lambda: str(fake.random_int(min=1, max=1000)))
