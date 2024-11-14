import allure

from config.config import BASE_URL, TRANSFER_FUNDS_URL
from data.amount_data import AmountData
from pages.main_page import MainPage
from pages.overview_page import OverviewPage
from tests.base.base_test import BaseTest


@allure.epic("Banking Application")
@allure.feature("Funds Transfer")
@allure.description_html("""
<h2>Testing Transfer Funds Functionality</h2>
<p>This test verifies the ability to transfer funds between accounts:</p>
<ul>
    <li>Transfer funds from one account to another</li>
    <li>Confirm the transfer is completed successfully</li>
</ul>
<p>The test performs the following operations:</p>
<ul>
    <li>Navigate to the Transfer Funds page</li>
    <li>Enter the transfer amount</li>
    <li>Click the Transfer button</li>
    <li>Verify the transfer is marked as complete</li>
</ul>
<p>Expected Results:</p>
<ul>
    <li>User can access the Transfer Funds page</li>
    <li>Funds are successfully transferred between accounts</li>
    <li>Transfer completion is confirmed on the page</li>
</ul>
""")
class TestTransferFunds(BaseTest):
    """The test class for transfer funds."""

    def test_transfer_funds(
        self,
        login: tuple[MainPage, OverviewPage],  # noqa: ARG002
        amount_data: AmountData,
    ) -> None:
        """Test transfer funds."""
        self.overview_page.click_transfer_funds()
        assert self.transfer_page.expect_url(
            f"{BASE_URL}{TRANSFER_FUNDS_URL}"
        ), "URL does not match expected value"
        self.transfer_page.fill_amount(amount_data)  # type: ignore
        self.transfer_page.click_transfer()  # type: ignore
        assert self.transfer_page.is_transfer_complete, "Transfer is not complete"
