from UI_Playwright.locators import Locators
import os
import time

class Page:

    def __init__(self, page):
        self.page = page

    # -------- Navigation --------
    def navigate_to(self, page_name):
        mapping = {
            "home": (Locators.home_button, "/"),
            "products": (Locators.products_button, "/products"),
            "cart": (Locators.cart_button, "/view_cart"),
            "login": (Locators.signup_login_button, "/login"),
            "signup": (Locators.signup_login_button, "/login"),
            "testcases": (Locators.testcases_button, "/test_cases"),
            "apitesting": (Locators.api_testing_button, "/api_list"),
            "contactus": (Locators.contact_us_button, "/contact_us"),
        }
        if page_name.lower() not in mapping:
            raise ValueError(f"Invalid page: {page_name}")
        if "#google_vignette" in self.page.url:
            self.close_ad()
        locator, expected_url = mapping[page_name.lower()]
        self.page.locator(locator).click()
        self.page.wait_for_url(lambda url: expected_url in url or "#google_vignette" in url, timeout=5000)
        if "#google_vignette" in self.page.url:
            self.close_ad()
            self.page.wait_for_load_state("domcontentloaded")
            self.page.locator(locator).click()
            self.page.wait_for_url(lambda url: expected_url in url, timeout=5000)
        assert expected_url in self.page.url
        assert "#google_vignette" not in self.page.url

    # -------- Advertisement --------
    def close_ad(self):
        frame = self.page.frame_locator(Locators.ad_iframe)
        close_btn = frame.locator(Locators.ad_close_button)
        if close_btn.is_visible():
            close_btn.click()

    # -------- Signup --------
    def signup(self, data):
        self.page.fill(Locators.signup_username, data["signup_name"])

        email = data["signup_email"]
        if email == "demo_tester@gmail.com":
            email = "demo_tester"+str(time.time())+ "@gmail.com"
        self.page.fill(Locators.signup_email, email)

        self.page.click(Locators.signup_button)
        if self.page.locator(Locators.signup_error).is_visible():
            return
        if data["signup_title"] == "Mr":
            self.page.click(Locators.signup_title1)
        elif data["signup_title"] == "Mrs":
            self.page.click(Locators.signup_title2)
        self.page.fill(Locators.signup_password, data["signup_password"])
        self.page.select_option(Locators.signup_date, str(data["signup_day"]))
        self.page.select_option(Locators.signup_month, str(data["signup_month"]))
        self.page.select_option(Locators.signup_year, str(data["signup_year"]))
        if data.get("signup_news"):
            self.page.check(Locators.signup_newsletter)
        if data.get("signup_offer"):
            self.page.check(Locators.signup_offer)
        self.page.fill(Locators.signup_firstname, data["signup_firstname"])
        self.page.fill(Locators.signup_lastname, data["signup_lastname"])
        self.page.fill(Locators.signup_company, data["signup_company"])
        self.page.fill(Locators.signup_address1, data["signup_address1"])
        self.page.fill(Locators.signup_address2, data["signup_address2"])
        self.page.select_option(Locators.signup_country, str(data["signup_country"]))
        self.page.fill(Locators.signup_state, data["signup_state"])
        self.page.fill(Locators.signup_city, data["signup_city"])
        self.page.fill(Locators.signup_zip, data["signup_zipcode"])
        self.page.fill(Locators.signup_mobile, str(data["signup_mobile"]))
        self.page.click(Locators.signup_create_account_button)
        assert self.page.locator(Locators.signup_success).is_visible()
        self.page.click(Locators.signup_continue_button)

    def delete_account(self):
        self.page.click(Locators.delete_account_button)
        self.page.locator(Locators.delete_account_success).wait_for(timeout=3000)

    # -------- Login --------
    def login(self, data):
        self.page.fill(Locators.login_username, data["login_email"])
        self.page.fill(Locators.login_password, data["login_password"])
        self.page.click(Locators.login_button)

    # -------- Logout --------
    def logout(self):
        self.page.click(Locators.logout_button)
        self.page.locator(Locators.login_success).wait_for(state="hidden")
        self.page.locator(Locators.logout_button).wait_for(state="hidden")

    # -------- Contact Us --------
    def contact_us(self, data):
        self.page.fill(Locators.contact_us_name, data["contact_us_name"])
        self.page.fill(Locators.contact_us_email, data["contact_us_email"])
        self.page.fill(Locators.contact_us_subject, data["contact_us_subject"])
        self.page.fill(Locators.contact_us_message, data["contact_us_message"])
        self.page.set_input_files(Locators.contact_us_file,os.path.abspath(data["contact_us_file"]))
        self.page.once("dialog", lambda d: d.accept())
        self.page.click(Locators.contact_us_submit_button)
        self.page.locator(Locators.contact_us_success).first.wait_for(timeout=3000)

    # -------- Search --------
    def search_product(self, data):
        self.page.fill(Locators.search_product_box, data["product_name"])
        self.page.click(Locators.search_product_button)

    # -------- Product --------
    def view_product(self):
        self.page.click(Locators.view_product_button)
        self.page.locator(Locators.view_product_name).wait_for(timeout=3000)

    def add_to_cart(self, data):
        self.page.fill(Locators.view_product_quantity, str(data["product_quantity"]))
        self.page.click(Locators.add_to_cart_button)
        self.page.locator(Locators.add_to_cart_success).wait_for(timeout=3000)
        assert self.page.locator(Locators.add_to_cart_success).is_visible()
        self.page.click(Locators.continue_shopping_button)

    # -------- Cart --------
    def remove_from_cart(self):
        self.page.click(Locators.cart_product_remove_button)
        self.page.locator(Locators.cart_product_remove_success).wait_for(timeout=3000)

    # -------- Checkout --------
    def checkout(self, data):
        self.page.click(Locators.cart_proceed_checkout_button)
        self.page.fill(Locators.place_order_message, data["order_comment"])
        self.page.click(Locators.place_order_button)
        self.page.fill(Locators.payment_card_name, data["card_name"])
        self.page.fill(Locators.payment_card_number, data["card_number"])
        self.page.fill(Locators.payment_cvc, data["card_cvc"])
        self.page.fill(Locators.payment_expiry_month, data["card_month"])
        self.page.fill(Locators.payment_expiry_year, data["card_year"])
        self.page.click(Locators.pay_and_confirm_button)
        self.page.locator(Locators.order_success).wait_for(timeout=3000)

    # -------- Filters --------
    def product_category_filter(self, data):
        self.page.click(Locators.category_button(data["product_category"]))
        self.page.click(Locators.subcategory_button(data["product_category"], data["product_subcategory"]))
        self.page.locator(Locators.category_filter_results_header(data["product_category"], data["product_subcategory"])).wait_for(timeout=3000)

    def product_brand_filter(self, data):
        self.page.click(Locators.brand_button(data["product_brand"]))
        self.page.locator(Locators.brand_filter_results_header(data["product_brand"])).wait_for(timeout=3000)
