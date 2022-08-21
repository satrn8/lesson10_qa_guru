from selene.support.shared import browser
import pytest
browser.config.timeout = 20


@pytest.fixture(scope="function", autouse=True)
def browser_open():
    browser.config.base_url = "https://demoqa.com"
    browser.config.browser_name = "chrome"