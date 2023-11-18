import time

from playwright.async_api import Page
from playwright.sync_api import expect


def test_has_title(page: Page):
    page.goto("https://google.ru")
    expect(page).to_have_title("Google")
    time.sleep(2)


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Get started").click()
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
    time.sleep(2)
