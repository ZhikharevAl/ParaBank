from collections.abc import Generator
from typing import Any

import allure
import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Page, sync_playwright
from playwright.sync_api._generated import Browser, BrowserContext


@pytest.fixture(autouse=True)
def browser() -> Generator[Browser, None, None]:
    """Browser fixture."""
    with sync_playwright() as p:
        browser: Browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture
def page(browser: Browser, request: SubRequest) -> Generator[Page, None, None]:
    """Page fixture."""
    context: BrowserContext = browser.new_context()
    page: Page = context.new_page()
    yield page

    if request.node.rep_call.failed: # type: ignore
        allure.attach(
            body=page.screenshot(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG,
        )

    page.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
    item: pytest.FixtureRequest,
) -> Generator[None, Any, None]:
    """Capture screenshots on test failures."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
