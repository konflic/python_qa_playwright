import time

from playwright.async_api import Page


def test_get_started_link(page: Page):
    page.goto("https://konflic.github.io/examples/editor/index.html")
    with page.expect_file_chooser() as fc_info:
        page.locator("#insert_picture").click()
    file_chooser = fc_info.value
    file_chooser.set_files("file.png")
    time.sleep(5)
