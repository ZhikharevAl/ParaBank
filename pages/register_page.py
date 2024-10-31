import allure
from playwright.sync_api import Page

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
        self.fill_text(self.USERNAME_INPUT, user_data.username)
        self.fill_text(self.PASSWORD_INPUT, user_data.password)
        self.fill_text(self.CONFIRM_PASSWORD_INPUT, user_data.password)

    @allure.step("Click register button")
    def click_register_button(self) -> None:
        """Click register button."""
        self.click_by_role("button", self.REGISTER_BUTTON)  # type: ignore

    @allure.step("Register new user")
    def register_new_user(self, user_data: UserData) -> None:
        """Complete registration process."""
        self.fill_registration_form(user_data)  # type: ignore
        self.click_register_button()  # type: ignore

    def is_registration_successful(self) -> bool:
        """Check if registration was successful."""
        return self.contains_text("h1", "Welcome")
