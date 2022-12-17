import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from dotenv import load_dotenv
from vpoxod_tests.utils import attach


def pytest_addoption(parser: pytest.Parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )
    parser.addoption(
        '--window_size',
        default='1920x1080'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    window_size = request.config.getoption('--window_size')

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    driver.set_window_size(window_size[:4], window_size[5:])
    base_url = os.getenv('BASE_URL')
    browser = Browser(Config(driver, base_url=base_url))

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()







