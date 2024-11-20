import re
from typing import Literal

import allure
from playwright.sync_api import Locator, Page, expect
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from config.config import BASE_URL

RoleType = Literal["button", "link"]


class BasePage:
    """Base class for all pages."""

    def __init__(self, page: Page, url: str = "") -> None:
        """The base class for all pages."""
        self.page: Page = page
        self.base_url = BASE_URL
        self.url: str = url

    def navigate(self) -> None:
        """Navigates to the given path."""
        with allure.step(f"Navigate to {self.base_url}{self.url}"):
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

    def clear_text(self, selector: str) -> None:
        """Clear text in element."""
        self.find_element(selector).clear()

    def fill_text(self, selector: str, text: str | None = None) -> None:
        """Fill text in element.

        Args:
            selector (str): Element selector
            text (str): Text to fill
        """
        if text is None:
            text = ""
        element: Locator = self.find_element(selector)
        self.page.on("dialog", lambda dialog: dialog.accept())
        element.clear()
        element.fill(text)

    @allure.step("Click element by role {role} with name {name}")
    def click_by_role(self, role: RoleType, name: str | None = None) -> None:
        """Click element by role and name.

        Args:
            role (str or None): Element role (button, link, etc.)
            name (str or None): Element name or text
        """
        self.page.get_by_role(role, name=name).click()

    def get_by_role_to_be_visible(
        self, role: RoleType, name: str | None = None
    ) -> bool:
        """Checks that the element is visible."""
        try:
            element: Locator = self.page.get_by_role(role, name=name)
        except PlaywrightTimeoutError:
            return False
        else:
            visible: bool = element.is_visible()
            return visible

    @allure.step("Select option {value} in dropdown {selector}")
    def select_option(self, selector: str, value: str | None) -> None:
        """Select option from dropdown by value.

        Args:
            selector (str): Dropdown selector
            value (str): Option value to select
        """
        self.find_element(selector).select_option(value)
