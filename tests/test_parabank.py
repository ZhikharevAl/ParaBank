from playwright.sync_api import Page

from config.config import BASE_URL
from pages.main_page import MainPage


def test_home_page_loading(page: Page) -> None:
    """The test checks that the main page is loaded."""
    login_page = MainPage(page)
    login_page.navigate()
    assert login_page.expect_url(BASE_URL), "URL does not match expected value"
    assert login_page.is_page_loaded(), "Page content is not loaded correctly"  # type: ignore
