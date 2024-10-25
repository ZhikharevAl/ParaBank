import pytest
from playwright.sync_api import Page

from config.data import Data
from pages.main_page import MainPage
from pages.overview_page import OverviewPage


class BaseTest:
    """The base class for all tests."""

    data: Data

    main_page: MainPage
    overview_page: OverviewPage
    page: Page

    @pytest.fixture(autouse=True)
    def setup(cls, page: Page) -> None:
        """The setup function."""
        cls.page = page
        cls.data = Data()
        cls.main_page = MainPage(page)
        cls.overview_page = OverviewPage(page)
