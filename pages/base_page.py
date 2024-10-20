import allure
from playwright.sync_api import Locator, Page, expect

from config.config import BASE_URL


class BasePage:
    """Base class for all pages."""
    def __init__(self, page: Page) -> None:
        """The base class for all pages."""
        self.page: Page = page
        self.base_url = BASE_URL

    def navigate(self, path: str = "") -> None:
        """Navigates to the given path."""
        with allure.step(f"Navigate to {self.base_url}{path}"): # type: ignore
            self.page.goto(f"{self.base_url}{path}")

    def find_element(self, selector: str) -> Locator:
        """Finds an element by selector."""
        return self.page.locator(selector)

    def should_have_text(self, selector: str, text: str) -> None:
        """Checks that the element contains the text."""
        expect(self.find_element(selector)).to_have_text(text)
