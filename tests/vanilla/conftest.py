import hashlib
from typing import Any, Generator

import pytest
from playwright.sync_api import (
    Browser,
    BrowserContext,
    Page,
    Playwright,
    sync_playwright,
)


@pytest.fixture(scope="session")
def playwright() -> Generator[Playwright, None, None]:
    pw = sync_playwright().start()

    yield pw

    pw.stop()


@pytest.fixture(scope="session")
def browser(pytestconfig: Any, playwright: Playwright) -> Generator[Browser, None, None]:
    launch_options = {}
    launch_options["headless"] = pytestconfig.getoption("--headed")

    browser_name = pytestconfig.getoption("--browser")
    browser = getattr(playwright, browser_name).launch(**launch_options)

    yield browser

    browser.close()


@pytest.fixture
def context(
        browser: Browser,
        request: pytest.FixtureRequest,
        pytestconfig: Any,
) -> Generator[BrowserContext, None, None]:
    context_args = {}
    video_option = pytestconfig.getoption("--screen_size").split("x")
    context_args["viewport"] = {
        "width": int(video_option[0]),
        "height": int(video_option[1])
    }
    context = browser.new_context(**context_args)
    yield context
    context.close()


@pytest.fixture
def page(context: BrowserContext) -> Generator[Page, None, None]:
    yield context.new_page()


def pytest_addoption(parser: Any) -> None:
    group = parser.getgroup("playwright", "Playwright")
    group.addoption(
        "--browser",
        action="append",
        default="chromium",
        help="Browser engine which should be used",
        choices=["chromium", "firefox", "webkit"],
    )
    group.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Run tests in headed mode.",
    )
    group.addoption(
        "--screen_size",
        default="1920x1080",
        help="Screen size manipulation",
    )
