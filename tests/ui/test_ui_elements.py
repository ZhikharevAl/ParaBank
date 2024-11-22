import allure

from pages.main_page import MainPage
from pages.overview_page import OverviewPage
from tests.base.base_test import BaseTest


@allure.epic("Main Application")
@allure.feature("UI Elements")
@allure.description_html("""
<h2>Testing UI Element Visibility</h2>
<p>Test verifies the visibility and accessibility of key UI elements, including:</p>
<ul>
    <li>Navigation to main page</li>
    <li>Checking registration button presence</li>
    <li>Checking transfer funds button presence</li>
    <li>Checking update contact info button presence</li>
</ul>
<p>Expected Results:</p>
<ul>
    <li>Registration button should be visible</li>
    <li>Transfer funds button should be visible</li>
    <li>Update contact info button should be visible</li>
</ul>
""")
class TestUIElements(BaseTest):
    """The test class for the UI elements."""

    @allure.story("Register Button Visibility")
    @allure.severity(severity_level="CRITICAL")
    def test_register_button(self) -> None:
        """The test checks that the register button is visible."""
        self.main_page.navigate()
        assert (
            self.main_page.is_register_button_visible
        ), "Register button is not visible"

    @allure.story("Transfer Funds Button Visibility")
    @allure.severity(severity_level="CRITICAL")
    def test_transfer_funds(self, login: tuple[MainPage, OverviewPage]) -> None:  # noqa: ARG002
        """The test checks that the register button is visible."""
        self.overview_page.navigate()
        assert (
            self.overview_page.is_transfer_button_visible
        ), "Transfer button is not visible"

    @allure.story("Update Contact Info Button Visibility")
    @allure.severity(severity_level="CRITICAL")
    def test_update_contact_info(self, login: tuple[MainPage, OverviewPage]) -> None:  # noqa: ARG002
        """The test checks that the update contact info button is visible."""
        self.overview_page.navigate()
        assert (
            self.overview_page.is_update_contact_info_visible
        ), "Update contact info button is not visible"
