import pytest
from UI_Playwright.page import Page
from Utilities.get_test_data import get_test_data
from UI_Playwright.locators import Locators

test_data = get_test_data("Test_Data/ui_test_data.yaml")


@pytest.mark.ui_playwright
class TestUIPlaywright:

    def test_01_verify_valid_signup(self, page):
        p = Page(page)

        p.navigate_to("signup")

        p.signup(test_data["valid_user_data"])

        p.delete_account()
        assert page.locator(Locators.delete_account_success).is_visible()

    def test_02_verify_invalid_signup(self, page):
        p = Page(page)

        p.navigate_to("signup")

        p.signup(test_data["invalid_user_data"])
        assert page.locator(Locators.signup_error).is_visible()

    def test_03_verify_valid_login(self, page):
        p = Page(page)

        p.navigate_to("login")

        p.login(test_data["valid_user_data"])
        assert page.locator(Locators.login_success).is_visible()

        p.logout()
        assert page.locator(Locators.signup_login_button).is_visible()

    def test_04_verify_invalid_login(self, page):
        p = Page(page)

        p.navigate_to("login")

        p.login(test_data["invalid_user_data"])
        assert page.locator(Locators.login_error).is_visible()

    def test_05_verify_contact_us(self, page):
        p = Page(page)

        p.navigate_to("contactus")

        p.contact_us(test_data["contact_us_data"])
        assert page.locator(Locators.contact_us_success).first.is_visible()

    def test_06_verify_search_product(self, page):
        p = Page(page)

        p.navigate_to("products")

        p.search_product(test_data["product_data"])
        assert page.locator(Locators.search_product_results).count() >= 1
        assert test_data["product_data"]["product_name"] in page.locator(Locators.search_product_results_text).inner_text()

        p.search_product(test_data["invalid_product_data"])
        assert page.locator(Locators.search_product_results).count() == 0

    def test_07_verify_cart_details(self, page):
        p = Page(page)

        p.navigate_to("products")

        p.search_product(test_data["product_data"])
        assert page.locator(Locators.search_product_results).count() >= 1
        assert test_data["product_data"]["product_name"] in page.locator(Locators.search_product_results_text).inner_text()

        p.view_product()
        assert test_data["product_data"]["product_name"] in page.locator(Locators.view_product_name).inner_text()
        assert test_data["product_data"]["product_category"] in page.locator(Locators.view_product_category).inner_text()
        assert test_data["product_data"]["product_subcategory"] in page.locator(Locators.view_product_category).inner_text()
        assert test_data["product_data"]["product_availability"] in page.locator(Locators.view_product_availability).inner_text()
        assert test_data["product_data"]["product_condition"] in page.locator(Locators.view_product_condition).inner_text()
        assert test_data["product_data"]["product_brand"] in page.locator(Locators.view_product_brand).inner_text()
        assert str(test_data["product_data"]["product_price"]) in page.locator(Locators.view_product_price).inner_text()

        p.add_to_cart(test_data["product_data"])

        p.navigate_to("cart")
        assert test_data["product_data"]["product_name"] in page.locator(Locators.cart_product_name).inner_text()
        assert test_data["product_data"]["product_category"] in page.locator(Locators.cart_product_category).inner_text()
        assert test_data["product_data"]["product_subcategory"] in page.locator(Locators.cart_product_category).inner_text()
        assert str(test_data["product_data"]["product_price"]) in page.locator(Locators.cart_product_price).inner_text()
        assert str(test_data["product_data"]["product_quantity"]) in page.locator(Locators.cart_product_quantity).inner_text()

        p.remove_from_cart()
        assert page.locator(Locators.cart_product_remove_success).is_visible()

    def test_08_verify_place_order(self, page):
        p = Page(page)

        p.navigate_to("login")

        p.login(test_data["valid_user_data"])
        assert page.locator(Locators.login_success).is_visible()

        p.navigate_to("products")

        p.search_product(test_data["product_data"])
        assert page.locator(Locators.search_product_results).count() >= 1
        assert test_data["product_data"]["product_name"] in page.locator(Locators.search_product_results_text).inner_text()

        p.view_product()
        assert test_data["product_data"]["product_name"] in page.locator(Locators.view_product_name).inner_text()
        assert test_data["product_data"]["product_category"] in page.locator(Locators.view_product_category).inner_text()
        assert test_data["product_data"]["product_subcategory"] in page.locator(Locators.view_product_category).inner_text()
        assert test_data["product_data"]["product_availability"] in page.locator(Locators.view_product_availability).inner_text()
        assert test_data["product_data"]["product_condition"] in page.locator(Locators.view_product_condition).inner_text()
        assert test_data["product_data"]["product_brand"] in page.locator(Locators.view_product_brand).inner_text()
        assert str(test_data["product_data"]["product_price"]) in page.locator(Locators.view_product_price).inner_text()

        p.add_to_cart(test_data["product_data"])

        p.navigate_to("cart")
        assert test_data["product_data"]["product_name"] in page.locator(Locators.cart_product_name).inner_text()
        assert test_data["product_data"]["product_category"] in page.locator(Locators.cart_product_category).inner_text()
        assert test_data["product_data"]["product_subcategory"] in page.locator(Locators.cart_product_category).inner_text()
        assert str(test_data["product_data"]["product_price"]) in page.locator(Locators.cart_product_price).inner_text()
        assert str(test_data["product_data"]["product_quantity"]) in page.locator(Locators.cart_product_quantity).inner_text()

        p.checkout(test_data["order_data"])
        assert page.locator(Locators.order_success).is_visible()

        p.logout()
        assert page.locator(Locators.signup_login_button).is_visible()

    def test_09_verify_product_filters(self, page):
        p = Page(page)

        p.navigate_to("products")

        p.product_category_filter(test_data["product_data"])
        assert page.locator(Locators.category_filter_results_header(
            test_data["product_data"]["product_category"],
            test_data["product_data"]["product_subcategory"]
            )
        ).is_visible()

        p.product_brand_filter(test_data["product_data"])
        assert page.locator(
        Locators.brand_filter_results_header(test_data["product_data"]["product_brand"])
        ).is_visible()

    def test_10_verify_navigations(self, page):
        p = Page(page)

        p.navigate_to("home")

        p.navigate_to("products")

        p.navigate_to("cart")

        p.navigate_to("login")

        p.navigate_to("signup")

        p.navigate_to("testcases")

        p.navigate_to("apitesting")

        p.navigate_to("contactus")
