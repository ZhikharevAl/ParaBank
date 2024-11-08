import allure
from playwright.sync_api import Page

from config.config import OVERVIEW_URL
from pages.base_page import BasePage


class OverviewPage(BasePage):
    """Overview page."""

    # locators
    ACCOUNT_OVERVIEW_HEADER = "#showOverview"
    ACCOUNT_OVERVIEW_HEADER_TEXT = "Accounts Overview"

    def __init__(self, page: Page) -> None:
        """The overview page."""
        super().__init__(page, url=OVERVIEW_URL)

    @allure.step("Check if user is logged in")
    def is_logged_in(self) -> bool:
        """Check if user is logged in by verifying Account Overview header."""
        return self.contains_text(
            self.ACCOUNT_OVERVIEW_HEADER, self.ACCOUNT_OVERVIEW_HEADER_TEXT
        )

    def click_open_new_account(self) -> None:
        """Click on Open new account button."""
        self.click_by_role("link", "Open New Account")  # type: ignore
