from typing import TYPE_CHECKING

import allure
from playwright.sync_api import Page

from config.config import OPEN_NEW_ACCOUNT_URL

if TYPE_CHECKING:
    from playwright.sync_api._generated import ElementHandle


from config.data import AccountType
from pages.base_page import BasePage


class OpenNewAccountPage(BasePage):  # noqa: D101
    # locators
    ACCOUNT_TYPE_SELECT = "#type"
    ACCOUNT_EXISTING_SELECT = "#fromAccountId"
    OPEN_NEW_ACCOUNT_BUTTON = "Open New Account"
    OPEN_ACCOUNT_RESULT = "#openAccountResult"
    VERIFY_TEXT = "Account Opened!"

    def __init__(self, page: Page) -> None:
        """The open new account page."""
        super().__init__(page, url=OPEN_NEW_ACCOUNT_URL)

    def select_account_type(self, account_type: AccountType) -> None:
        """Select SAVINGS account type from dropdown."""
        self.select_option(self.ACCOUNT_TYPE_SELECT, account_type.value)

    @allure.step("Choose existing account")
    def choose_an_existing_account(self) -> None:
        """Select first available existing account from dropdown."""
        available_accounts: list[ElementHandle] = self.find_element(
            self.ACCOUNT_EXISTING_SELECT
        ).element_handles()
        if available_accounts:
            with allure.step("Select first available existing account {value}"):
                self.select_option(
                    self.ACCOUNT_EXISTING_SELECT,
                    available_accounts[0].get_attribute("value"),
                )
        else:
            error_message = "No existing accounts available to select from"
            raise ValueError(error_message)

    def click_button_open_new_account(self) -> None:
        """Click on Open new account button."""
        self.click_by_role("button", self.OPEN_NEW_ACCOUNT_BUTTON)

    @property
    def is_account_created(self) -> bool:
        """Check if account has been created."""
        return self.contains_text(self.OPEN_ACCOUNT_RESULT, self.VERIFY_TEXT)
