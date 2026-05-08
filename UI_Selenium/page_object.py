from UI_Selenium.ui_client import UIClient
from UI_Selenium.locators import Locators
import os
import time

class PageObject(UIClient):

    def close_advertisement(self):
        self.logger.info(f"Checking advertisement")
        if self.wait.visible(Locators._ad_iframe):
            self.switch_to_iframe(Locators._ad_iframe)
            self.logger.info(f"Inside iframe")
            if self.wait.visible(Locators._ad_close_button, 3):
                self.logger.info(f"Ad present")
                self.click(Locators._ad_close_button)
                self.logger.info(f"Closed advertisement")
            self.switch_to_default()
            return True
        return False

    def navigate_to(self, page):
        self.logger.info(f"Navigating to page: {page}")
        page=page.lower()

        if page=="home":
            self.click(Locators._home_button)
            if not self.wait.visible(Locators._homepage_slider, 5):
                self.close_advertisement()
                self.click(Locators._home_button)
                if not self.wait.visible(Locators._homepage_slider, 5):
                    return {"status": "failure", "message": f"Failed to navigate: {page}"}

        elif page == "products":
            self.click(Locators._products_button)
            if not self.wait.url_contains("products",5):
                self.close_advertisement()
                self.click(Locators._products_button)
                if not self.wait.url_contains("products", 5):
                    return {"status": "failure", "message": f"Failed to navigate: {page}"}

        elif page == "cart":
            self.click(Locators._cart_button)
            if not self.wait.url_contains("view_cart",5):
                self.close_advertisement()
                self.click(Locators._cart_button)
                if not self.wait.url_contains("view_cart", 5):
                    return {"status": "failure", "message": f"Failed to navigate: {page}"}

        elif page == "login" or page == "signup":
            self.click(Locators._signup_login_button)
            if not self.wait.url_contains("login",5):
                self.close_advertisement()
                self.click(Locators._signup_login_button)
                if not self.wait.url_contains("login", 5):
                    return {"status": "failure", "message": f"Failed to navigate: {page}"}

        elif page == "testcases":
            self.click(Locators._testcases_button)
            if not self.wait.url_contains("test_cases",5):
                self.close_advertisement()
                self.click(Locators._testcases_button)
                if not self.wait.url_contains("test_cases", 5):
                    return {"status": "failure", "message": f"Failed to navigate: {page}"}

        elif page == "apitesting":
            self.click(Locators._api_testing_button)
            if not self.wait.url_contains("api_list",5):
                self.close_advertisement()
                self.click(Locators._api_testing_button)
                if not self.wait.url_contains("api_list", 5):
                    return {"status": "failure", "message": f"Failed to navigate: {page}"}

        elif page == "contactus":
            self.click(Locators._contact_us_button)
            if not self.wait.url_contains("contact_us",5):
                self.close_advertisement()
                self.click(Locators._contact_us_button)
                if not self.wait.url_contains("contact_us", 5):
                    return {"status": "failure", "message": f"Failed to navigate: {page}"}

        elif page == "deleteaccount":
            self.click(Locators._delete_account_button)
            if not self.wait.url_contains("delete_account",5):
                self.close_advertisement()
                self.click(Locators._delete_account_button)
                if not self.wait.url_contains("delete_account", 5):
                    return {"status": "failure", "message": f"Failed to navigate: {page}"}

        elif page == "logout":
            self.click(Locators._logout_button)
            if not self.wait.url_contains("login",5):
                self.close_advertisement()
                self.click(Locators._logout_button)
                if not self.wait.url_contains("login", 5):
                    return {"status": "failure", "message": f"Failed to navigate: {page}"}

        else:
            return {"status": "failure", "message": f"Unsupported page: {page}"}

        self.wait_for_page_load()
        return {"status": "success", "message": f"Navigated successfully to page: {page}"}

    def signup(self, signup_data):
        self.logger.info(f"Signing up")

        name = signup_data["signup_name"]
        email = signup_data["signup_email"]
        password = signup_data["signup_password"]
        title = signup_data["signup_title"]
        day = signup_data["signup_day"]
        month = signup_data["signup_month"]
        year = signup_data["signup_year"]
        news = signup_data["signup_news"]
        offer = signup_data["signup_offer"]
        firstname = signup_data["signup_firstname"]
        lastname = signup_data["signup_lastname"]
        company = signup_data["signup_company"]
        address1 = signup_data["signup_address1"]
        address2 = signup_data["signup_address2"]
        country = signup_data["signup_country"]
        state = signup_data["signup_state"]
        city = signup_data["signup_city"]
        zipcode = signup_data["signup_zipcode"]
        mobile = signup_data["signup_mobile"]

        self.wait.visible(Locators._signup_header1)
        self.send_keys(Locators._signup_username, name)

        if email == "demo_tester@gmail.com":
            email = "demo_tester"+str(time.time())+ "@gmail.com"
        self.send_keys(Locators._signup_email, email)


        self.click(Locators._signup_button)

        if self.wait.visible(Locators._signup_error, 3):
            return {"status": "failure", "message": "Email Address already exist"}
        self.wait_for_page_load()
        self.wait.visible(Locators._signup_header2)

        if title:
            if title=="Mr":
                self.click(Locators._signup_title1)
            elif title=="Mrs":
                self.click(Locators._signup_title2)

        self.send_keys(Locators._signup_password, password)

        if day:
            self.select_dropdown(Locators._signup_date, str(day))
        if month:
            self.select_dropdown(Locators._signup_month, str(month))
        if year:
            self.select_dropdown(Locators._signup_year, str(year))
        if news:
            self.click(Locators._signup_newsletter)
        if offer:
            self.click(Locators._signup_offer)

        self.send_keys(Locators._signup_firstname, firstname)
        self.send_keys(Locators._signup_lastname, lastname)

        if address1:
            self.send_keys(Locators._signup_address1, address1)

        self.send_keys(Locators._signup_address2, address2)

        if company:
            self.send_keys(Locators._signup_company, company)

        self.select_dropdown(Locators._signup_country, str(country))
        self.send_keys(Locators._signup_state, state)
        self.send_keys(Locators._signup_city, city)
        self.send_keys(Locators._signup_zip, zipcode)
        self.send_keys(Locators._signup_mobile, mobile)
        self.click(Locators._signup_create_account_button)
        self.wait_for_page_load()
        if self.wait.visible(Locators._signup_success):
            self.click(Locators._signup_continue_button)
            self.wait_for_page_load()
            return {"status": "success", "message": "Account created"}
        else:
            return {"status": "failure", "message": "Account creation failed"}

    def delete_account(self):
        self.logger.info(f"Deleting account")
        if self.wait.visible(Locators._delete_account_button):
            self.navigate_to("deleteaccount")
            if self.wait.visible(Locators._delete_account_success):
                self.click(Locators._delete_account_continue_button)
                return {"status": "success", "message": "Account deleted"}
        return {"status": "failure", "message": "Account delete failed"}

    def login(self, login_data):
        self.logger.info(f"Logging in")
        username = login_data["login_email"]
        password = login_data["login_password"]
        self.wait.visible(Locators._login_header)
        self.send_keys(Locators._login_username, username)
        self.send_keys(Locators._login_password, password)
        self.click(Locators._login_button)
        self.wait_for_page_load()
        if self.wait.visible(Locators._login_error, 5):
            return {"status": "failure", "message": "Email or password is incorrect"}
        elif self.wait.visible(Locators._login_success):
            return {"status": "success", "message": "Login success"}
        else:
            return {"status": "failure", "message": "Login failed"}

    def logout(self):
        self.logger.info(f"Logging out")
        if self.wait.visible(Locators._logout_button):
            self.navigate_to("logout")
            if self.wait.invisible(Locators._login_success) and self.wait.invisible(Locators._logout_button) and self.wait.visible(Locators._signup_login_button):
                return {"status": "success", "message": "Logout success"}
        return {"status": "failure", "message": "Logout failed"}

    def contact_us(self, contact_us_data):
        self.logger.info(f"Contact us")
        name = contact_us_data["contact_us_name"]
        email = contact_us_data["contact_us_email"]
        subject = contact_us_data["contact_us_subject"]
        message = contact_us_data["contact_us_message"]
        file = contact_us_data["contact_us_file"]
        self.wait.visible(Locators._contact_us_header)
        if name:
            self.send_keys(Locators._contact_us_name, name)
        self.send_keys(Locators._contact_us_email, email)
        if subject:
            self.send_keys(Locators._contact_us_subject, subject)
        if message:
            self.send_keys(Locators._contact_us_message, message)

        if file:
            self.send_keys(Locators._contact_us_file, os.path.abspath(file))

        self.click(Locators._contact_us_submit_button)
        self.accept_alert()
        if self.wait.visible(Locators._contact_us_success):
            return {"status": "success", "message": "Contact us success"}
        else:
            return {"status": "failure", "message": "Contact us failed"}

    def search_product(self, product_data):
        self.logger.info(f"Searching product")
        name = product_data["product_name"]
        self.send_keys(Locators._search_product_box, name)
        self.click(Locators._search_product_button)
        self.wait.visible(Locators._search_product_results)
        actual_name = self.get_text(Locators._search_product_results_text)
        expected_name = name
        if actual_name == expected_name:
            return {"status": "success", "message": "Search product success"}
        else:
            return {"status": "failure", "message": "Search product failed"}

    def view_product(self, product_data):
        self.logger.info(f"View product")
        self.click(Locators._view_product_button)
        self.wait_for_page_load()
        actual_name = self.get_text(Locators._view_product_name)
        expected_name = product_data["product_name"]
        if actual_name == expected_name:
            return {"status": "success", "message": "Product view success"}
        else:
            return {"status": "failure", "message": "Product view failed"}

    def product_details(self, product_data):
        self.logger.info(f"Verifying product details")
        actual_name = self.get_text(Locators._view_product_name)
        actual_category = self.get_text(Locators._view_product_category)
        actual_subcategory = self.get_text(Locators._view_product_category)
        actual_price = self.get_text(Locators._view_product_price)
        actual_available = self.get_text(Locators._view_product_availability)
        actual_condition = self.get_text(Locators._view_product_condition)
        actual_brand = self.get_text(Locators._view_product_brand)
        expected_name = product_data["product_name"]
        expected_category = product_data["product_category"]
        expected_subcategory = product_data["product_subcategory"]
        expected_price = product_data["product_price"]
        expected_available = product_data["product_availability"]
        expected_condition = product_data["product_condition"]
        expected_brand = product_data["product_brand"]
        if (actual_name == expected_name and expected_category in actual_category
                and expected_subcategory in actual_subcategory and str(expected_price) in actual_price
                and expected_available in actual_available and expected_condition in actual_condition
                and expected_brand in actual_brand):
            return {"status": "success", "message": "Product details success"}
        else:
            return {"status": "failure", "message": "Product details failed"}

    def add_product_to_cart(self, product_data):
        self.logger.info(f"Add product to cart")
        quantity = product_data["product_quantity"]
        self.send_keys(Locators._view_product_quantity, quantity)
        self.click(Locators._add_to_cart_button)
        if self.wait.visible(Locators._add_to_cart_success):
            self.click(Locators._continue_shopping_button)
            return {"status": "success", "message": "Add product to cart success"}
        else:
            return {"status": "failure", "message": "Add product to cart failed"}

    def cart_details(self, product_data):
        self.logger.info(f"Verifying cart details")
        actual_name = self.get_text(Locators._cart_product_name)
        actual_category = self.get_text(Locators._cart_product_category)
        actual_subcategory = self.get_text(Locators._cart_product_category)
        actual_price = self.get_text(Locators._cart_product_price)
        actual_quantity = self.get_text(Locators._cart_product_quantity)
        expected_name = product_data["product_name"]
        expected_category = product_data["product_category"]
        expected_subcategory = product_data["product_subcategory"]
        expected_price = product_data["product_price"]
        expected_quantity = product_data["product_quantity"]
        if (actual_name == expected_name and expected_category in actual_category
                and expected_subcategory in actual_subcategory
                and str(expected_price) in actual_price and str(expected_quantity) == actual_quantity):
            return {"status": "success", "message": "Cart details success"}
        else:
            return {"status": "failure", "message": "Cart details failed"}

    def remove_product_from_cart(self):
        self.logger.info(f"Remove product from cart")
        self.click(Locators._cart_product_remove_button)
        if self.wait.visible(Locators._cart_product_remove_success):
            return {"status": "success", "message": "Product remove success"}
        else:
            return {"status": "failure", "message": "Product remove failed"}

    def checkout(self, order_data):
        self.logger.info(f"Checkout")
        comment = order_data["order_comment"]
        name = order_data["card_name"]
        number = order_data["card_number"]
        cvc = order_data["card_cvc"]
        month = order_data["card_month"]
        year = order_data["card_year"]
        self.click(Locators._cart_proceed_checkout_button)
        self.wait_for_page_load()
        self.send_keys(Locators._place_order_message, comment)
        self.click(Locators._place_order_button)
        self.wait.visible(Locators._payment_header)
        self.send_keys(Locators._payment_card_name, name)
        self.send_keys(Locators._payment_card_number, number)
        self.send_keys(Locators._payment_cvc, cvc)
        self.send_keys(Locators._payment_expiry_month, month)
        self.send_keys(Locators._payment_expiry_year, year)
        self.click(Locators._pay_and_confirm_button)
        if self.wait.visible(Locators._order_success):
            return {"status": "success", "message": "Checkout success"}
        else:
            return {"status": "failure", "message": "Checkout failed"}

    def product_category_filter(self, product_data):
        self.logger.info(f"Verifying product category filter")
        category = product_data["product_category"]
        subcategory = product_data["product_subcategory"]
        self.click(Locators.category_button(category))
        self.click(Locators.subcategory_button(category, subcategory))
        if self.wait.visible(Locators.category_filter_results_header(category, subcategory)):
            return {"status": "success", "message": "Product category filter success"}
        else:
            return {"status": "failure", "message": "Product category filter failed"}

    def product_brand_filter(self, product_data):
        self.logger.info(f"Verifying product brand filter")
        brand = product_data["product_brand"]
        self.click(Locators.brand_button(brand))
        if self.wait.visible(Locators.brand_filter_results_header(brand)):
            return {"status": "success", "message": "Product brand filter success"}
        else:
            return {"status": "failure", "message": "Product brand filter failed"}
