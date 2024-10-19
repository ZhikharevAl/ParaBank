from collections.abc import Generator

import pytest
from playwright.sync_api import Page, sync_playwright
from playwright.sync_api._generated import Browser, BrowserContext


@pytest.fixture(autouse=True)
def browser() -> Generator[Browser, None, None]:
    """A fixture for starting and closing the browser."""
    with sync_playwright() as p:
        browser: Browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser: Browser) -> Generator[Page, None, None]:
    """A fixture for opening and closing a new page in the browser."""
    context: BrowserContext = browser.new_context()
    page: Page = context.new_page()
    yield page
    page.close()
