import allure

from tests.base.base_test import BaseTest


@allure.epic("Main Application")
@allure.feature("UI Elements")
@allure.description_html("""
<h2>Testing UI Element Visibility</h2>
<p>Test verifies the visibility and accessibility of key UI elements, including:</p>
<ul>
    <li>Navigation to main page</li>
    <li>Checking registration button presence</li>
</ul>
<p>Expected Results:</p>
<ul>
    <li>Registration button should be visible</li>
</ul>
""")
class TestUIElements(BaseTest):
    """The test class for the UI elements."""

    @allure.story("Register Button Visibility")
    @allure.severity(severity_level="MINOR")
    def test_register_button(self) -> None:
        """The test checks that the register button is visible."""
        self.main_page.navigate()
        assert self.main_page.is_register_button_visible()
