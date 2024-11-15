import allure
from playwright.sync_api import Page

from config.config import UPDATE_PROFILE_URL
from data.user_data import UserData
from pages.base_page import BasePage


class UpdateProfilePage(BasePage):
    """The update profile page."""

    def __init__(self, page: Page) -> None:
        """The update profile page."""
        super().__init__(page, url=UPDATE_PROFILE_URL)

    FIRST_NAME_INPUT = '[id="customer.firstName"]'
    LAST_NAME_INPUT = '[id="customer.lastName"]'
    STREET_INPUT = '[id="customer.address.street"]'
    CITY_INPUT = '[id="customer.address.city"]'
    STATE_INPUT = '[id="customer.address.state"]'
    ZIP_CODE_INPUT = '[id="customer.address.zipCode"]'
    PHONE_INPUT = '[id="customer.phoneNumber"]'
    UPDATE_BUTTON = "Update Profile"
    UPDATE_MESSAGE_LOCATOR = "#updateProfileResult"
    UPDATE_MESSAGE = "Profile Updated"

    @allure.step("Fill registration form")
    def update_profile(self, user_data: UserData) -> None:
        """Fill all fields in registration form."""
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.fill_text(self.FIRST_NAME_INPUT, user_data.first_name)
        self.fill_text(self.LAST_NAME_INPUT, user_data.last_name)
        self.fill_text(self.STREET_INPUT, user_data.street)
        self.fill_text(self.CITY_INPUT, user_data.city)
        self.fill_text(self.STATE_INPUT, user_data.state)
        self.fill_text(self.ZIP_CODE_INPUT, user_data.zip_code)
        self.fill_text(self.PHONE_INPUT, user_data.phone)

    def click_update_button(self) -> None:
        """Click update button."""
        self.click_by_role("button", self.UPDATE_BUTTON)  # type: ignore

    @property
    def is_updated(self) -> bool:
        """Check if profile is updated."""
        return self.contains_text(self.UPDATE_MESSAGE_LOCATOR, self.UPDATE_MESSAGE)
