
import pytest
from pages.main_page import MainPage
from pages.overview_page import OverviewPage


class BaseTest:
    """The base class for all tests."""

    main_page: MainPage
    overview_page: OverviewPage

    @pytest.fixture(autouse=True)
    def setup(cls, request, page) -> None:
        request.cls.page = page

        request.cls.main_page = MainPage(page)
        request.cls.overview_page = OverviewPage(page)
