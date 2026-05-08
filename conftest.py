import os
from datetime import datetime
import shutil
import pytest
import pytest_html
from pytest_html import extras
from Utilities.get_config import ConfigReader
from Utilities.logger import get_logger
from UI_Selenium.webdriver import get_driver
from playwright.sync_api import sync_playwright
from API_Requests.api_client import APIClient
from API_Requests.auth_service import AuthService
from API_Requests.user_api import UserAPI


#####=====Common=====#####

def pytest_configure(config):
    if not hasattr(config, "workerinput"):
        report_dir = "Reports"
        if os.path.exists(report_dir):
            shutil.rmtree(report_dir)
    os.makedirs("Reports/Allure_Report/Allure_Raw_Data", exist_ok=True)
    os.makedirs("Reports/Allure_Report/Allure_HTML", exist_ok=True)
    os.makedirs("Reports/HTML_Report", exist_ok=True)
    os.makedirs("Reports/Logs", exist_ok=True)
    os.makedirs("Reports/Screenshots", exist_ok=True)
    os.makedirs("Reports/Videos", exist_ok=True)


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--sel_browser", action="store", default="chrome")
    parser.addoption("--sel_grid", action="store_true")
    parser.addoption("--plw_browser", action="store", default="chromium")
    parser.addoption("--plw_slowmo", action="store", default=0)


@pytest.fixture(scope="session")
def config(request):
    return ConfigReader(
        env=request.config.getoption("--env"),
        headless=request.config.getoption("--headless"),
        sel_browser=request.config.getoption("--sel_browser"),
        plw_browser=request.config.getoption("--plw_browser"),
        plw_slowmo=request.config.getoption("--plw_slowmo")
    )


@pytest.fixture
def logger(request):
    test_name = request.node.name
    logger, log_file = get_logger(test_name)
    request.node.log_file = log_file
    return logger


#####=====API=====#####

@pytest.fixture
def api_client(config, logger):
    return APIClient(
        base_url=config.get_api_base_url(),
        logger=logger
    )


@pytest.fixture
def auth_service(api_client, logger):
    return AuthService(api_client, logger)


@pytest.fixture
def user_api(api_client, logger):
    return UserAPI(api_client, logger)


#####=====Selenium=====#####

@pytest.fixture
def driver(request, config):
    marker = request.node.get_closest_marker("ui_selenium")
    if marker is None:
        pytest.skip("Skipping: not a ui_selenium test")
    driver = None
    try:
        driver = get_driver(
            browser=config.get_sel_browser(),
            headless=config.is_headless(),
            grid=request.config.getoption("--sel_grid"),
            grid_url=config.get_grid_url()
        )
        driver.get(config.get_ui_base_url())
        yield driver
    finally:
        if driver:
            driver.quit()


#####=====Playwright=====#####

@pytest.fixture(scope="session")
def browser(config):
    with sync_playwright() as p:
        browser = getattr(p, config.get_plw_browser()).launch(
            headless=config.is_headless(),
            slow_mo = config.get_slowmo()
        )
        yield browser
        browser.close()


@pytest.fixture
def context(browser, config, request):
    test_name = request.node.name
    context = browser.new_context(
        base_url=config.get_ui_base_url(),
        viewport=None,
        record_video_dir=f"Reports/Videos/{test_name}/"
    )
    context.tracing.start(screenshots=True, snapshots=True)
    yield context
    context.tracing.stop(path=f"Reports/Logs/{test_name}_trace.zip")
    context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    page.goto("/", wait_until="networkidle", timeout=60000)
    yield page
    page.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    rep.log_file = getattr(item, "log_file", None)

    if rep.when == "call" and rep.failed:

        if not hasattr(rep, "extras"):
            rep.extras = []

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = item.name.replace("::", "_").replace("/", "_")
        screenshot_dir = "Reports/Screenshots"

        driver = item.funcargs.get("driver", None)
        if driver:
            file_path = f"{screenshot_dir}/{test_name}_{timestamp}_selenium.png"
            driver.save_screenshot(file_path)
            rep.extras.append(extras.image(file_path))

        page = item.funcargs.get("page", None)
        if page:
            file_path = f"{screenshot_dir}/{test_name}_{timestamp}_playwright.png"
            page.screenshot(path=file_path, full_page=True)
            rep.extras.append(extras.image(file_path))

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_extra(report, outcome, extra):
    if report.when == "call":

        log_file = getattr(report, "log_file", None)

        if log_file and os.path.exists(log_file):
            rel_path = os.path.relpath(log_file)

            extra.append(extras.url(rel_path, name="Log File"))
