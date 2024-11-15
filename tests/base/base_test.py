import pytest
from playwright.sync_api import Page

from config.data import Data
from pages.main_page import MainPage
from pages.open_new_account_page import OpenNewAccountPage
from pages.overview_page import OverviewPage
from pages.register_page import RegisterPage
from pages.transfer_page import TransferPage
from pages.update_profile_page import UpdateProfilePage


class PageFactory:
    """Factory for creating pages."""

    def __init__(self, page: Page) -> None:
        """Constructor."""
        self.page: Page = page

    def create_main_page(self) -> MainPage:
        """Create main page."""
        return MainPage(self.page)

    def create_overview_page(self) -> OverviewPage:
        """Create overview page."""
        return OverviewPage(self.page)

    def create_register_page(self) -> RegisterPage:
        """Create register page."""
        return RegisterPage(self.page)

    def create_open_new_account_page(self) -> OpenNewAccountPage:
        """Create open new account page."""
        return OpenNewAccountPage(self.page)

    def create_transfer_page(self) -> TransferPage:
        """Create transfer page."""
        return TransferPage(self.page)

    def create_update_profile_page(self) -> UpdateProfilePage:
        """Create update profile page."""
        return UpdateProfilePage(self.page)


class BaseTest:
    """The base class for all tests."""

    data: Data
    page: Page

    @pytest.fixture(autouse=True)
    def setup(cls, page: Page) -> None:
        """Function that is called before each test."""
        cls.page = page
        cls.data = Data()

        factory = PageFactory(page)

        # Initialize pages using the factory
        cls._main_page: MainPage = factory.create_main_page()
        cls._overview_page: OverviewPage = factory.create_overview_page()
        cls._register_page: RegisterPage = factory.create_register_page()
        cls._open_new_account_page: OpenNewAccountPage = (
            factory.create_open_new_account_page()
        )
        cls._transfer_page: TransferPage = factory.create_transfer_page()
        cls._update_profile_page: UpdateProfilePage = (
            factory.create_update_profile_page()
        )

    @property
    def main_page(self) -> MainPage:
        """Get the main page instance."""
        return self._main_page

    @property
    def overview_page(self) -> OverviewPage:
        """Get the overview page instance."""
        return self._overview_page

    @property
    def register_page(self) -> RegisterPage:
        """Get the register page instance."""
        return self._register_page

    @property
    def open_new_account_page(self) -> OpenNewAccountPage:
        """Get the open new account page instance."""
        return self._open_new_account_page

    @property
    def transfer_page(self) -> TransferPage:
        """Get the transfer page instance."""
        return self._transfer_page

    @property
    def update_profile_page(self) -> UpdateProfilePage:
        """Get the update profile page instance."""
        return self._update_profile_page
