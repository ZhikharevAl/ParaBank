from tests.base.base_test import BaseTest


class TestUIElements(BaseTest):
    """The test class for the UI elements."""

    def test_register_button(self) -> None:
        """The test checks that the register button is visible."""
        self.main_page.navigate()
        assert self.main_page.is_register_button_visible()
