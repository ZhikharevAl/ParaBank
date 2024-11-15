import time

from config.config import BASE_URL, UPDATE_PROFILE_URL
from data.user_data import UserData
from pages.main_page import MainPage
from pages.overview_page import OverviewPage
from tests.base.base_test import BaseTest


class TestUpdateProfile(BaseTest):
    """Test update profile."""

    def test_update_profile(
        self,
        login: tuple[MainPage, OverviewPage],  # noqa: ARG002
        random_user_data: UserData,
    ) -> None:
        """Test update profile."""
        self.overview_page.click_update_profile()
        assert self.transfer_page.expect_url(
            f"{BASE_URL}{UPDATE_PROFILE_URL}"
        ), "URL does not match expected value"
        self.update_profile_page.update_profile(random_user_data)  # type: ignore
        self.update_profile_page.click_update_button()
        assert self.update_profile_page.is_updated, "Profile is not updated"
        time.sleep(6)
