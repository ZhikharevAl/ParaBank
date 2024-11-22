import allure
from playwright.sync_api import Page

from config.config import OVERVIEW_URL
from pages.base_page import BasePage


class OverviewPage(BasePage):
    """Overview page."""

    # locators
    ACCOUNT_OVERVIEW_HEADER = "#showOverview"
    ACCOUNT_OVERVIEW_HEADER_TEXT = "Accounts Overview"
    TRANSFER_FUNDS_BUTTON = "Transfer Funds"
    OPEN_NEW_ACCOUNT_BUTTON = "Open New Account"
    UPDATE_CONTACT_INFO_BUTTON = "Update Contact Info"

    def __init__(self, page: Page) -> None:
        """The overview page."""
        super().__init__(page, url=OVERVIEW_URL)

    @property
    def is_logged_in(self) -> bool:
        """Check if user is logged in by verifying Account Overview header."""
        with allure.step("Check if user is logged in"):
            return self.contains_text(
                self.ACCOUNT_OVERVIEW_HEADER, self.ACCOUNT_OVERVIEW_HEADER_TEXT
            )

    @property
    def is_transfer_button_visible(self) -> bool:
        """Checks that the transfer funds button is visible."""
        return self.get_by_role_to_be_visible("link", self.TRANSFER_FUNDS_BUTTON)

    @property
    def is_update_contact_info_visible(self) -> bool:
        """Checks that the update contact info button is visible."""
        return self.get_by_role_to_be_visible("link", self.UPDATE_CONTACT_INFO_BUTTON)

    def click_open_new_account(self) -> None:
        """Click on Open new account button."""
        self.click_by_role("link", self.OPEN_NEW_ACCOUNT_BUTTON)

    def click_transfer_funds(self) -> None:
        """Click transfer funds button."""
        self.click_by_role("link", self.TRANSFER_FUNDS_BUTTON)

    def click_update_profile(self) -> None:
        """Click update profile button."""
        self.click_by_role("link", self.UPDATE_CONTACT_INFO_BUTTON)
