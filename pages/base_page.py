import re

import allure
from playwright.sync_api import Locator, Page, expect

from config.config import BASE_URL


class BasePage:
    """Base class for all pages."""

    def __init__(self, page: Page, url: str = "") -> None:
        """The base class for all pages."""
        self.page: Page = page
        self.base_url = BASE_URL
        self.url: str = url

    def navigate(self) -> None:
        """Navigates to the given path."""
        with allure.step(f"Navigate to {self.base_url}{self.url}"):  # type: ignore
            self.page.goto(f"{self.base_url}{self.url}")

    def expect_url(self, url: str) -> bool:
        """Checks that the current URL contains the given url.

        Returns:
            bool: True if the current URL matches the expected URL
        """
        with allure.step(f"Check if current URL contains {url}"):  # type: ignore
            try:
                expect(self.page).to_have_url(re.compile(f"^{re.escape(url)}(?:;|$)"))
            except AssertionError:
                return False
            else:
                return True

    def find_element(self, selector: str) -> Locator:
        """Finds an element by selector."""
        return self.page.locator(selector)

    def should_have_text(self, selector: str, text: str) -> None:
        """Checks that the element contains the text."""
        expect(self.find_element(selector)).to_have_text(text)

    def contains_text(self, selector: str, text: str) -> bool:
        """Checks that the element contains the text."""
        try:
            expect(self.page.locator(selector)).to_contain_text(text)
        except AssertionError:
            return False
        else:
            return True

    def fill_text(self, selector: str, text: str) -> None:
        """Fill text in element.

        Args:
            selector (str): Element selector
            text (str): Text to fill
        """
        self.find_element(selector).fill(text)

    @allure.step("Click element by role {role} with name {name}")
    def click_by_role(self, role: str, name: str) -> None:
        """Click element by role and name.

        Args:
            role (str): Element role (button, link, etc.)
            name (str): Element name or text
        """
        self.page.get_by_role(role, name=name).click()  # type: ignore

    def get_by_role_to_be_visible(self, role: str, name: str) -> bool:
        """Checks that the element is visible."""
        try:
            expect(self.page.get_by_role(role, name=name)).to_be_visible()  # type: ignore
        except AssertionError:
            return False
        else:
            return True

    @allure.step("Select option {value} in dropdown {selector}")
    def select_option(self, selector: str, value: str) -> None:
        """Select option from dropdown by value.

        Args:
            selector (str): Dropdown selector
            value (str): Option value to select
        """
        self.find_element(selector).select_option(value)
