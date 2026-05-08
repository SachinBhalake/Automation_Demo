from selenium import webdriver


def get_driver(browser, headless=False, grid=False, grid_url=None):

    browser = browser.lower()

    # -------------------------
    # CHROME
    # -------------------------
    if browser == "chrome":
        options = webdriver.ChromeOptions()

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.page_load_strategy = "eager"

        if headless:
            options.add_argument("--headless=new")

        if grid:
            driver = webdriver.Remote(
                command_executor=grid_url,
                options=options
            )

            driver.maximize_window()
            return driver

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        return driver
    # -------------------------
    # FIREFOX
    # -------------------------
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.page_load_strategy = "eager"
        if headless:
            options.add_argument("--headless")

        if grid:
            driver = webdriver.Remote(
                command_executor=grid_url,
                options=options
                )

            driver.maximize_window()
            return driver

        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
        return driver
    else:
        raise ValueError(f"Unsupported browser: {browser}")