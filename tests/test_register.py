import allure

from data.user_data import UserData
from tests.base.base_test import BaseTest


@allure.epic("Main Application")
@allure.feature("User Registration")
@allure.description_html("""
<h2>Testing User Registration Functionality</h2>
<p>Test verifies the user registration process, including:</p>
<ul>
    <li>Navigation to registration page</li>
    <li>Generating random user data</li>
    <li>Completing registration form</li>
    <li>Verifying successful registration</li>
</ul>
<p>Expected Results:</p>
<ul>
    <li>User should be able to register with valid data</li>
    <li>Registration should complete successfully</li>
</ul>
""")
class TestRegistration(BaseTest):
    """Tests for user registration."""

    @allure.story("Successful Registration")
    @allure.severity(severity_level="CRITICAL")
    def test_successful_registration(self, random_user_data: UserData) -> None:
        """Test successful user registration with valid data."""
        self.register_page.navigate()
        registration_success = self.register_page.register_new_user(random_user_data)
        assert registration_success, "Registration was not successful"
        assert (
            self.register_page.is_registration_successful
        ), "Registration was not successful"
