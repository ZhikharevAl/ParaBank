import allure

from config.config import BASE_URL, MAIN_URL
from tests.base.base_test import BaseTest


@allure.epic("Main Application")
@allure.feature("Home Page")
@allure.description_html("""
<h2>Testing Home Page Loading Functionality</h2>
<p>Test verifies basic functionality of the main page loading process, including:</p>
<ul>
    <li>Navigation to the home page</li>
    <li>URL verification</li>
    <li>Page content loading validation</li>
</ul>
<p>The test performs the following checks:</p>
<ul>
    <li>Confirms that the current URL matches the expected base URL</li>
    <li>Verifies that all essential page elements are properly loaded and visible</li>
</ul>
<p>Expected Results:</p>
<ul>
    <li>The page should successfully navigate to the specified URL</li>
    <li>All page components should be properly rendered and accessible</li>
</ul>
""")
class TestHomePage(BaseTest):
    """The test class for the home page."""

    @allure.story("Home Page Loading")
    @allure.severity(severity_level="CRITICAL")
    def test_home_page_loading(self) -> None:
        """The test checks that the main page is loaded."""
        self.main_page.navigate()
        assert self.main_page.expect_url(
            f"{BASE_URL}{MAIN_URL}"
        ), "URL does not match expected value"
        assert self.main_page.is_page_loaded, "Page content is not loaded correctly"
