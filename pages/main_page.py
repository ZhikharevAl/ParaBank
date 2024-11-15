import allure
from playwright.sync_api import Page

from config.config import MAIN_URL
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
    USERNAME_INPUT = 'input[name="username"]'
    PASSWORD_INPUT = 'input[name="password"]'  # nosec

    def __init__(self, page: Page) -> None:
        """The main page."""
        super().__init__(page, url=MAIN_URL)

    @property
    def is_customer_login_in_page(self) -> bool:
        """Checks that the customer login header is visible."""
        return self.find_element(self.CUSTOMER_LOGIN_HEADER).is_visible()

    def verify_header_panel_loaded(self) -> None:
        """Verifies that the header panel is loaded."""
        self.should_have_text(self.HEADER_PANEL, self.HEADER_PANEL_TEXT)

    @property
    def is_page_loaded(self) -> bool:
        """The main page is loaded."""
        with allure.step("The checks page content is loaded correctly"):  # type: ignore
            is_login_visible: bool = self.is_customer_login_in_page
            try:
                self.verify_header_panel_loaded()
                is_header_text_correct = True
            except AssertionError:
                is_header_text_correct = False

            return is_login_visible and is_header_text_correct

    def fill_login_form(self, username: str, password: str) -> None:
        """Fill login form with credentials."""
        self.fill_text(self.USERNAME_INPUT, username)  # type: ignore
        self.fill_text(self.PASSWORD_INPUT, password)  # type: ignore

    @allure.step("Click login button")
    def click_login_button(self) -> None:
        """Click login button."""
        self.click_by_role("button", "Log In")  # type: ignore

    @allure.step("Login with credentials")
    def login(self, username: str, password: str) -> None:
        """Login with provided credentials."""
        self.fill_login_form(username, password)  # type: ignore
        self.click_login_button()  # type: ignore

    @property
    def is_register_button_visible(self) -> bool:
        """Checks that the register button is visible."""
        return self.get_by_role_to_be_visible("link", "Register")
