import pytest
from playwright.sync_api import Page

from config.data import Data
from pages.main_page import MainPage
from pages.open_new_account_page import OpenNewAccountPage
from pages.overview_page import OverviewPage
from pages.register_page import RegisterPage
from pages.transfer_page import TransferPage
from pages.update_profile_page import UpdateProfilePage


class BaseTest:
    """The base class for all tests."""

    data: Data

    main_page: MainPage
    overview_page: OverviewPage
    register_page: RegisterPage
    open_new_account_page: OpenNewAccountPage
    transfer_page: TransferPage
    update_profile_page: UpdateProfilePage
    page: Page

    @pytest.fixture(autouse=True)
    def setup(cls, page: Page) -> None:
        """The setup function."""
        cls.page = page
        cls.data = Data()
        cls.main_page = MainPage(page)
        cls.overview_page = OverviewPage(page)
        cls.register_page = RegisterPage(page)
        cls.open_new_account_page = OpenNewAccountPage(page)
        cls.transfer_page = TransferPage(page)
        cls.update_profile_page = UpdateProfilePage(page)
