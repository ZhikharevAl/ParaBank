import allure
from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from config.config import REGISTER_URL
from data.user_data import UserData
from pages.base_page import BasePage


class RegisterPage(BasePage):
    """Register page."""

    # Locators
    FIRST_NAME_INPUT = '[id="customer.firstName"]'
    LAST_NAME_INPUT = '[id="customer.lastName"]'
    STREET_INPUT = '[id="customer.address.street"]'
    CITY_INPUT = '[id="customer.address.city"]'
    STATE_INPUT = '[id="customer.address.state"]'
    ZIP_CODE_INPUT = '[id="customer.address.zipCode"]'
    PHONE_INPUT = '[id="customer.phoneNumber"]'
    SSN_INPUT = '[id="customer.ssn"]'
    USERNAME_INPUT = '[id="customer.username"]'
    PASSWORD_INPUT = '[id="customer.password"]'
    CONFIRM_PASSWORD_INPUT = "#repeatedPassword"
    REGISTER_BUTTON = "Register"
    USERNAME_EXISTS_ERROR = "cell"
    USERNAME_EXISTS_MESSAGE = "This username already exists."

    def __init__(self, page: Page) -> None:
        """The register page."""
        super().__init__(page, url=REGISTER_URL)

    @allure.step("Fill registration form")
    def fill_registration_form(self, user_data: UserData) -> None:
        """Fill all fields in registration form."""
        self.fill_text(self.FIRST_NAME_INPUT, user_data.first_name)
        self.fill_text(self.LAST_NAME_INPUT, user_data.last_name)
        self.fill_text(self.STREET_INPUT, user_data.street)
        self.fill_text(self.CITY_INPUT, user_data.city)
        self.fill_text(self.STATE_INPUT, user_data.state)
        self.fill_text(self.ZIP_CODE_INPUT, user_data.zip_code)
        self.fill_text(self.PHONE_INPUT, user_data.phone)
        self.fill_text(self.SSN_INPUT, user_data.ssn)
        self.fill_credentials(user_data)  # type: ignore

    @allure.step("Fill user credentials")
    def fill_credentials(self, user_data: UserData) -> None:
        """Fill username and password fields."""
        self.fill_text(self.USERNAME_INPUT, user_data.username)
        self.fill_text(self.PASSWORD_INPUT, user_data.password)
        self.fill_text(self.CONFIRM_PASSWORD_INPUT, user_data.password)

    @allure.step("Click register button")
    def click_register_button(self) -> None:
        """Click register button."""
        self.click_by_role("button", self.REGISTER_BUTTON)  # type: ignore

    def check_username_exists(self) -> bool:
        """Check if username already exists error is displayed."""
        try:
            self.page.get_by_role(
                self.USERNAME_EXISTS_ERROR, name=self.USERNAME_EXISTS_MESSAGE
            ).wait_for(timeout=3000)
        except PlaywrightTimeoutError:
            return False
        else:
            return True

    @allure.step("Register new user")
    def register_new_user(self, user_data: UserData, max_attempts: int = 5) -> bool:
        """Complete registration process with username collision handling.

        Args:
            user_data: User data for registration
            max_attempts: Maximum number of attempts to try with different usernames

        Returns:
            bool: True if registration was successful, False otherwise
        """
        self.fill_registration_form(user_data)  # type: ignore

        for _ in range(max_attempts):
            self.click_register_button()  # type: ignore

            if self.check_username_exists():
                user_data.generate_new_username()
                self.fill_credentials(user_data)  # type: ignore
                continue

            return True

        return False

    def is_registration_successful(self) -> bool:
        """Check if registration was successful."""
        return self.contains_text("h1", "Welcome")
