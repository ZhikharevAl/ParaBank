import shutil
from collections.abc import Generator
from pathlib import Path
from typing import Any

import allure
import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Page, sync_playwright
from playwright.sync_api._generated import Browser, BrowserContext

from config.data import Data
from pages.main_page import MainPage
from pages.overview_page import OverviewPage


@pytest.fixture(autouse=True)
def browser() -> Generator[Browser, None, None]:
    """Browser fixture."""
    with sync_playwright() as p:
        browser: Browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser: Browser, request: SubRequest) -> Generator[Page, None, None]:
    """Page fixture."""
    context: BrowserContext = browser.new_context()

    # Start tracing
    context.tracing.start(
        screenshots=True,  # Capture screenshots
        snapshots=True,  # Capture snapshots of the DOM
        sources=True,  # Capture source code
    )

    page: Page = context.new_page()
    yield page

    if request.node.rep_call.failed:  # type: ignore
        context.tracing.stop(path=f"traces/trace-{request.node.name}.zip")
        allure.attach(
            body=page.screenshot(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG,
        )

    page.close()


@pytest.fixture(autouse=True, scope="session")
def clear_traces() -> None:
    """Clear traces directory before test run."""
    traces_dir = Path("traces")
    if traces_dir.exists():
        shutil.rmtree(traces_dir)
    traces_dir.mkdir(exist_ok=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
    item: pytest.FixtureRequest,
) -> Generator[None, Any, None]:
    """Capture screenshots on test failures."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture
def login(page: Page) -> tuple[MainPage, OverviewPage]:
    """
    Fixture that performs user login.

    Args:
        page: Playwright page fixture

    Returns:
        Tuple[MainPage, OverviewPage]: Tuple containing initialized MainPage and
        OverviewPage
    """
    main_page = MainPage(page)
    overview_page = OverviewPage(page)

    main_page.navigate()
    assert main_page.is_page_loaded, "Main page is not loaded properly"  # type: ignore

    username = Data().USERNAME
    password = Data().PASSWORD

    main_page.login(username, password)  # type: ignore
    assert overview_page.is_logged_in, "Login failed"  # type: ignore

    return main_page, overview_page
