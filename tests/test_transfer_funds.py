from config.config import BASE_URL, TRANSFER_FUNDS_URL
from data.amount_data import AmountData
from pages.main_page import MainPage
from pages.overview_page import OverviewPage
from tests.base.base_test import BaseTest


class TestTransferFunds(BaseTest):
    """The test class for transfer funds."""

    def test_transfer_funds(
        self,
        login: tuple[MainPage, OverviewPage],  # noqa: ARG002
        amount_data: AmountData,
    ) -> None:
        """Test transfer funds."""
        self.overview_page.click_transfer_funds()
        assert self.transfer_page.expect_url(f"{BASE_URL}{TRANSFER_FUNDS_URL}")
        self.transfer_page.fill_amount(amount_data)
        self.transfer_page.click_transfer()
        assert self.transfer_page.is_transfer_complete()
