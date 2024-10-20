from playwright.sync_api import Page

from pages.main_page import MainPage


def test_home_page_loading(page: Page) -> None:
    """The test checks that the main page is loaded."""
    login_page = MainPage(page)
    login_page.navigate()
    assert login_page.is_page_loaded(), "Page is not loaded" # type: ignore
