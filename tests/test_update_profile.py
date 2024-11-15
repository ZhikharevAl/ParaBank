import allure

from config.config import BASE_URL, UPDATE_PROFILE_URL
from data.user_data import UserData
from pages.main_page import MainPage
from pages.overview_page import OverviewPage
from tests.base.base_test import BaseTest


@allure.epic("Banking Application")
@allure.feature("Update Profile")
@allure.description_html("""
<h2>Testing Update Profile Functionality</h2>
<p>This test verifies the ability to update a user's profile information:</p>
<ul>
    <li>Update profile information with new data</li>
    <li>Confirm the profile update is completed successfully</li>
</ul>
<p>The test performs the following operations:</p>
<ul>
    <li>Navigate to the Update Profile page</li>
    <li>Enter the new profile information</li>
    <li>Click the Update button</li>
    <li>Verify the profile update is marked as complete</li>
</ul>
<p>Expected Results:</p>
<ul>
    <li>User can access the Update Profile page</li>
    <li>Profile information is successfully updated</li>
    <li>Update completion is confirmed on the page</li>
</ul>
""")
class TestUpdateProfile(BaseTest):
    """Test update profile."""

    def test_update_profile(
        self,
        login: tuple[MainPage, OverviewPage],  # noqa: ARG002
        random_user_data: UserData,
    ) -> None:
        """Test update profile."""
        self.overview_page.click_update_profile()
        assert self.update_profile_page.expect_url(
            f"{BASE_URL}{UPDATE_PROFILE_URL}"
        ), "URL does not match expected value"
        self.update_profile_page.update_profile(random_user_data)  # type: ignore
        self.update_profile_page.click_update_button()
        assert self.update_profile_page.is_updated, "Profile is not updated"
