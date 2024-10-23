import allure
from playwright.sync_api import Page

from pages.base_page import BasePage


class MainPage(BasePage):
    """The main page."""

    # locators
    CUSTOMER_LOGIN_HEADER = "h2"
    HEADER_PANEL = "#headerPanel"
    HEADER_PANEL_TEXT = (
        "Solutions About Us Services Products Locations "
        "Admin Page home about contact"
    )

    def __init__(self, page: Page) -> None:
        """The main page."""
        super().__init__(page)

    def is_customer_login_in_page(self) -> bool:
        """Checks that the customer login header is visible."""
        return self.find_element(self.CUSTOMER_LOGIN_HEADER).is_visible()

    def verify_header_panel_loaded(self) -> None:
        """Verifies that the header panel is loaded."""
        self.should_have_text(self.HEADER_PANEL, self.HEADER_PANEL_TEXT)

    @allure.step("The checks page content is loaded correctly")
    def is_page_loaded(self) -> bool:
        """The main page is loaded."""
        is_login_visible: bool = self.is_customer_login_in_page()
        try:
            self.verify_header_panel_loaded()
            is_header_text_correct = True
        except AssertionError:
            is_header_text_correct = False

        return is_login_visible and is_header_text_correct
