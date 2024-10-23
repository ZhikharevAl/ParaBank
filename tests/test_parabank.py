import allure
from playwright.sync_api import Page

from config.config import BASE_URL
from pages.main_page import MainPage


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
class TestHomePage:
    """The test class for the home page."""

    @allure.story("Home Page Loading")
    @allure.severity(severity_level="CRITICAL")
    def test_home_page_loading(self, page: Page) -> None:
        """The test checks that the main page is loaded."""
        self.login_page = MainPage(page)
        self.login_page.navigate()
        assert self.login_page.expect_url(BASE_URL), "URL does not match expected value"
        assert self.login_page.is_page_loaded(), "Page content is not loaded correctly"  # type: ignore
