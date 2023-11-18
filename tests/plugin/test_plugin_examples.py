import time

from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://google.ru")
    expect(page).to_have_title("Google")
    time.sleep(2)


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Get started").click()
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
    time.sleep(2)


def test_search_input(page: Page):
    page.goto("http://192.168.0.113:8081/")
    # page.locator("input[name='search']").type("iphone")
    page.locator("input[name='search']").fill("iphone")
    page.locator("//*[@id='search']//button").click()
    # expect(page.locator("//*[@class='breadcrumb']//a[text()='Search']")).to_be_hidden(timeout=1 * 1000)
    expect(page.locator("//*[@class='breadcrumb']").locator("//a[text()='Search']")).to_be_visible(timeout=1 * 1000)
    time.sleep(2)
