import pytest

from config.config import BASE_URL, OPEN_NEW_ACCOUNT_URL
from config.data import AccountType
from pages.main_page import MainPage
from pages.overview_page import OverviewPage
from tests.base.base_test import BaseTest


class TestOpenNewAccount(BaseTest):
    """The test class for the open new account page."""

    @pytest.mark.parametrize(
        "account_type",
        [
            pytest.param(AccountType.SAVINGS, id="savings_account"),
            pytest.param(AccountType.CHECKING, id="checking_account"),
        ],
    )
    def test_open_new_account(
        self,
        login: tuple[MainPage, OverviewPage],  # noqa: ARG002
        account_type: AccountType,
    ) -> None:
        """
        Test opening new account of different types.

        Args:
            login: Login fixture
            account_type: Type of account to open (SAVINGS or CHECKING)
        """
        self.overview_page.click_open_new_account()
        assert self.open_new_account_page.expect_url(
            f"{BASE_URL}{OPEN_NEW_ACCOUNT_URL}"
        )

        self.open_new_account_page.select_account_type(account_type)
        self.open_new_account_page.choose_an_existing_account()  # type: ignore
        self.open_new_account_page.click_button_open_new_account()

        assert (
            self.open_new_account_page.is_account_created()
        ), f"Failed to create {account_type.name.lower()} account"
