import allure
from playwright.sync_api import Page

from config.config import TRANSFER_FUNDS_URL
from data.amount_data import AmountData
from pages.base_page import BasePage


class TransferPage(BasePage):
    """The transfer page."""

    AMOUNT_INPUT = "#amount"
    TRANSFER_BUTTON = "Transfer"
    SHOW_RESULT = "#showResult"
    TRANSFER_COMPLETE_TEXT = "Transfer Complete!"

    def __init__(self, page: Page) -> None:
        """The transfer page."""
        super().__init__(page, url=TRANSFER_FUNDS_URL)

    @allure.step("Fill the amount field")
    def fill_amount(self, amount_data: AmountData) -> None:
        """Fill the amount field."""
        self.fill_text(self.AMOUNT_INPUT, amount_data.amount)

    @allure.step("Click the transfer button")
    def click_transfer(self) -> None:
        """Click the transfer button."""
        self.click_by_role("button", self.TRANSFER_BUTTON)

    @property
    def is_transfer_complete(self) -> bool:
        """Check if the transfer is complete."""
        return self.contains_text(self.SHOW_RESULT, self.TRANSFER_COMPLETE_TEXT)
