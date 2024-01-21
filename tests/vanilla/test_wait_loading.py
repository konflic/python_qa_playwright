from playwright.async_api import Page
from playwright.sync_api import expect


def test_get_started_link(page: Page):
    page.goto("https://konflic.github.io/examples/pages/slowlyloading.html")
    expect(page.locator(".box1")).to_be_visible() # 5 сек.


def test_get_started_link_without_expect(page: Page):
    page.goto("https://konflic.github.io/examples/pages/slowlyloading.html")
    page.locator(".box1").click() # 30 сек.
