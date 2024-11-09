from dataclasses import dataclass, field

from faker import Faker

fake = Faker()


@dataclass
class UserData:
    """User data class."""

    first_name: str = field(default_factory=lambda: fake.first_name())
    last_name: str = field(default_factory=lambda: fake.last_name())
    street: str = field(default_factory=lambda: fake.street_address())
    city: str = field(default_factory=lambda: fake.city())
    state: str = field(default_factory=lambda: fake.state())
    zip_code: str = field(default_factory=lambda: fake.postcode())
    post_code: str = field(default_factory=lambda: fake.postcode())
    phone: str = field(default_factory=lambda: fake.phone_number())
    ssn: str = field(default_factory=lambda: fake.ssn())
    username: str = field(default_factory=lambda: fake.user_name())
    password: str = field(
        default_factory=lambda: fake.password(
            length=12, special_chars=True, digits=True, upper_case=True, lower_case=True
        )
    )

    @staticmethod
    def generate_random_user() -> "UserData":
        """Generate random user data."""
        return UserData(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            street=fake.street_address(),
            city=fake.city(),
            state=fake.state(),
            zip_code=fake.zipcode(),
            phone=fake.phone_number(),
            ssn=fake.ssn(),
            username=fake.user_name(),
            password=fake.password(length=12),
        )

    def generate_new_username(self) -> None:
        """Generate new username."""
        self.username = fake.user_name()
