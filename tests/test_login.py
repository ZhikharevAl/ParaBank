import allure

from config.config import BASE_URL, MAIN_URL, OVERVIEW_URL
from tests.base.base_test import BaseTest


@allure.epic("Main Application")
@allure.feature("Authentication")
@allure.description_html("""
<h2>Testing Login Functionality</h2>
<p>Test verifies the authentication process functionality, including:</p>
<ul>
    <li>Navigation to the login page</li>
    <li>User authentication with credentials</li>
    <li>Successful redirect after login</li>
</ul>
<p>The test performs the following checks:</p>
<ul>
    <li>Confirms initial navigation to the main page</li>
    <li>Verifies successful login with valid credentials</li>
    <li>Checks redirect to overview page after login</li>
    <li>Validates user's authenticated state</li>
</ul>
<p>Expected Results:</p>
<ul>
    <li>User should successfully authenticate with valid credentials</li>
    <li>System should redirect to the overview page</li>
    <li>User should be in logged-in state</li>
</ul>
""")
class TestLogin(BaseTest):
    """Class for Login tests."""

    @allure.story("User Authentication")
    @allure.severity(severity_level="CRITICAL")
    def test_login(self) -> None:
        """Test validates the complete login workflow and successful authentication."""
        self.main_page.navigate()
        assert self.main_page.expect_url(
            f"{BASE_URL}{MAIN_URL}"
        ), "URL does not match expected value"

        self.main_page.login(self.data.USERNAME, self.data.PASSWORD)

        assert self.main_page.expect_url(
            f"{BASE_URL}{OVERVIEW_URL}"
        ), "Failed to redirect to overview page after login"

        assert self.overview_page.is_logged_in, "User is not in logged-in state"
