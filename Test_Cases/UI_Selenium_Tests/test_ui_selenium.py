import pytest
from UI_Selenium.steps import Steps
from Utilities.get_test_data import get_test_data

test_data = get_test_data("Test_Data/ui_test_data.yaml")

@pytest.mark.ui_selenium
class TestUISelenium:

    def test_01_verify_valid_signup(self, driver, logger):
        logger.info("Test Started: Verify valid signup")
        s = Steps(driver, logger)
        test_result = s.verify_signup(test_data["valid_user_data"])
        assert test_result["nav_result"]["status"] == "success", "Test Failed: " + test_result["nav_result"]["message"]
        assert test_result["signup_result"]["status"] == "success", "Test Failed: " + test_result["signup_result"]["message"]
        assert test_result["delete_result"]["status"] == "success", "Test Failed: " + test_result["delete_result"]["message"]
        logger.info("Test Passed: Verified valid signup")

    def test_02_verify_invalid_signup(self, driver, logger):
        logger.info("Test Started: Verify invalid signup")
        s = Steps(driver, logger)
        test_result = s.verify_signup(test_data["invalid_user_data"])
        assert test_result["nav_result"]["status"] == "success", "Test Failed: " + test_result["nav_result"]["message"]
        assert test_result["signup_result"]["status"] == "failure", "Test Failed: " + test_result["signup_result"]["message"]
        assert test_result["delete_result"]["status"] == "skipped", "Test Failed: " + test_result["delete_result"]["message"]
        logger.info("Test Passed: Verified invalid signup")

    def test_03_verify_valid_login(self, driver, logger):
        logger.info("Test Started: Verify valid login")
        s = Steps(driver, logger)
        test_result = s.verify_login(test_data["valid_user_data"])
        assert test_result["nav_result"]["status"] == "success", "Test Failed: " + test_result["nav_result"]["message"]
        assert test_result["login_result"]["status"] == "success", "Test Failed: " + test_result["login_result"]["message"]
        assert test_result["logout_result"]["status"] == "success", "Test Failed: " + test_result["logout_result"]["message"]
        logger.info("Test Passed: Verified valid login")

    def test_04_verify_invalid_login(self, driver, logger):
        logger.info("Test Started: Verify invalid login")
        s = Steps(driver, logger)
        test_result = s.verify_login(test_data["invalid_user_data"])
        assert test_result["nav_result"]["status"] == "success", "Test Failed: " + test_result["nav_result"]["message"]
        assert test_result["login_result"]["status"] == "failure", "Test Failed: " + test_result["login_result"]["message"]
        assert test_result["logout_result"]["status"] == "skipped", "Test Failed: " + test_result["logout_result"]["message"]
        logger.info("Test Passed: Verified invalid login")

    def test_05_verify_contact_us(self, driver, logger):
        logger.info("Test Started: Verify contact us")
        s = Steps(driver, logger)
        test_result = s.verify_contact_us(test_data["contact_us_data"])
        assert test_result["nav_result"]["status"] == "success", "Test Failed: " + test_result["nav_result"]["message"]
        assert test_result["contact_us_result"]["status"] == "success", "Test Failed: " + test_result["contact_us_result"]["message"]
        logger.info("Test Passed: Verified contact us")

    def test_06_verify_search_product(self, driver, logger):
        logger.info("Test Started: Verify search product")
        s = Steps(driver, logger)
        test_result = s.verify_search_product(test_data["product_data"])
        assert test_result["nav_result"]["status"] == "success", "Test Failed: " + test_result["nav_result"]["message"]
        assert test_result["search_result"]["status"] == "success", "Test Failed: " + test_result["search_result"]["message"]
        logger.info("Test Passed: Verified search product")

    def test_07_verify_cart_details(self, driver, logger):
        logger.info("Test Started: Verify cart details")
        s = Steps(driver, logger)
        test_result = s.verify_cart_details(test_data["product_data"])
        assert test_result["products_nav_result"]["status"] == "success", "Test Failed: " + test_result["products_nav_result"]["message"]
        assert test_result["search_result"]["status"] == "success", "Test Failed: " + test_result["search_result"]["message"]
        assert test_result["open_product_result"]["status"] == "success", "Test Failed: " + test_result["open_product_result"]["message"]
        assert test_result["view_product_result"]["status"] == "success", "Test Failed: " + test_result["view_product_result"]["message"]
        assert test_result["add_result"]["status"] == "success", "Test Failed: " + test_result["add_result"]["message"]
        assert test_result["cart_nav_result"]["status"] == "success", "Test Failed: " + test_result["cart_nav_result"]["message"]
        assert test_result["cart_result"]["status"] == "success", "Test Failed: " + test_result["cart_result"]["message"]
        assert test_result["remove_result"]["status"] == "success", "Test Failed: " + test_result["remove_result"]["message"]
        logger.info("Test Passed: Verified cart details")

    def test_08_verify_place_order(self, driver, logger):
        logger.info("Test Started: Verify place order")
        s = Steps(driver, logger)
        test_result = s.verify_place_order(test_data["valid_user_data"], test_data["product_data"], test_data["order_data"])
        assert test_result["login_nav_result"]["status"] == "success", "Test Failed: " + test_result["login_nav_result"]["message"]
        assert test_result["login_result"]["status"] == "success", "Test Failed: " + test_result["login_result"]["message"]
        assert test_result["products_nav_result"]["status"] == "success", "Test Failed: " + test_result["products_nav_result"]["message"]
        assert test_result["search_result"]["status"] == "success", "Test Failed: " + test_result["search_result"]["message"]
        assert test_result["open_product_result"]["status"] == "success", "Test Failed: " + test_result["open_product_result"]["message"]
        assert test_result["view_product_result"]["status"] == "success", "Test Failed: " + test_result["view_product_result"]["message"]
        assert test_result["add_result"]["status"] == "success", "Test Failed: " + test_result["add_result"]["message"]
        assert test_result["cart_nav_result"]["status"] == "success", "Test Failed: " + test_result["cart_nav_result"]["message"]
        assert test_result["cart_result"]["status"] == "success", "Test Failed: " + test_result["cart_result"]["message"]
        assert test_result["order_result"]["status"] == "success", "Test Failed: " + test_result["order_result"]["message"]
        assert test_result["logout_result"]["status"] == "success", "Test Failed: " + test_result["logout_result"]["message"]
        logger.info("Test Passed: Verified place order")

    def test_09_verify_product_filters(self, driver, logger):
        logger.info("Test Started: Verify product filters")
        s = Steps(driver, logger)
        test_result = s.verify_product_filters(test_data["product_data"])
        assert test_result["nav_result"]["status"] == "success", "Test Failed: " + test_result["nav_result"]["message"]
        assert test_result["category_result"]["status"] == "success", "Test Failed: " + test_result["category_result"]["message"]
        assert test_result["brand_result"]["status"] == "success", "Test Failed: " + test_result["brand_result"]["message"]
        logger.info("Test Passed: Verified product filters")

    def test_10_verify_navigations(self, driver, logger):
        logger.info("Test Started: Verify navigations")
        s = Steps(driver, logger)
        test_result = s.verify_navigations()
        assert test_result["home_nav_result"]["status"] == "success", "Test Failed: " + test_result["home_nav_result"]["message"]
        assert test_result["products_nav_result"]["status"] == "success", "Test Failed: " + test_result["products_nav_result"]["message"]
        assert test_result["cart_nav_result"]["status"] == "success", "Test Failed: " + test_result["cart_nav_result"]["message"]
        assert test_result["login_nav_result"]["status"] == "success", "Test Failed: " + test_result["login_nav_result"]["message"]
        assert test_result["signup_nav_result"]["status"] == "success", "Test Failed: " + test_result["signup_nav_result"]["message"]
        assert test_result["testcases_nav_result"]["status"] == "success", "Test Failed: " + test_result["testcases_nav_result"]["message"]
        assert test_result["apitesting_nav_result"]["status"] == "success", "Test Failed: " + test_result["apitesting_nav_result"]["message"]
        assert test_result["contactus_nav_result"]["status"] == "success", "Test Failed: " + test_result["contactus_nav_result"]["message"]
        logger.info("Test Passed: Verified navigations")
