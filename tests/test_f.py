import allure
from playwright.sync_api import Page, expect


@allure.feature("Search Functionality")
@allure.story("Failed Search Test")
@allure.severity(allure.severity_level.NORMAL)
def test_failing_search(page: Page) -> None:
    """Тест, который намеренно падает для проверки работы trace и allure отчетов."""
    with allure.step("Navigate to Google"): # type: ignore
        page.goto("https://www.google.com")

    with allure.step("Accept cookies if present"): # type: ignore
        try:
            page.get_by_role("button", name="Accept all").click()
        except:  # noqa: E722
            allure.attach(
                "No cookie banner found",
                name="info",
                attachment_type=allure.attachment_type.TEXT,
            )

    with allure.step("Perform search"): # type: ignore
        search_input = page.get_by_role("combobox", name="Search")
        search_input.fill("Playwright Python")
        search_input.press("Enter")

    with allure.step("Check non-existent element"): # type: ignore
        # Этот шаг гарантированно упадёт
        non_existent = page.locator("[data-test='non-existent-element']")
        allure.attach(
            page.content(),
            name="page-html",
            attachment_type=allure.attachment_type.HTML,
        )
        # Установка маленького таймаута, чтобы тест падал быстрее
        expect(non_existent).to_be_visible(timeout=2000)
