from UI_Selenium.page_object import PageObject


class Steps(PageObject):

    def verify_signup(self, signup_data):
        self.logger.info(f"Verifying register new user and delete it")
        nav_result = self.navigate_to("signup")
        signup_result = self.signup(signup_data)
        if signup_result["status"] == "success":
            delete_result = self.delete_account()
        else:
            delete_result = {
                "status": "skipped",
                "message": "Delete skipped due to signup failure"
            }
        return {
            "nav_result": nav_result,
            "signup_result": signup_result,
            "delete_result": delete_result
        }

    def verify_login(self, login_data):
        self.logger.info(f"Verifying login user and logout")
        nav_result = self.navigate_to("login")
        login_result = self.login(login_data)
        if login_result["status"] == "success":
            logout_result = self.logout()
        else:
            logout_result = {
                "status": "skipped",
                "message": "Logout skipped due to login failure"
            }
        return {
        "nav_result": nav_result,
        "login_result": login_result,
        "logout_result": logout_result
        }

    def verify_contact_us(self, contact_us_data):
        self.logger.info(f"Verifying contact us")
        nav_result = self.navigate_to("contactus")
        contactus_result = self.contact_us(contact_us_data)
        return {
            "nav_result": nav_result,
            "contact_us_result": contactus_result
        }

    def verify_search_product(self, product_data):
        self.logger.info(f"Verifying search product")
        nav_result = self.navigate_to("products")
        search_result = self.search_product(product_data)
        return {
            "nav_result": nav_result,
            "search_result": search_result
        }

    def verify_cart_details(self, product_data):
        self.logger.info(f"Verifying cart details")
        products_nav_result = self.navigate_to("products")
        search_result = self.search_product(product_data)
        open_product_result = self.view_product(product_data)
        view_product_result = self.product_details(product_data)
        add_result = self.add_product_to_cart(product_data)
        cart_nav_result = self.navigate_to("cart")
        cart_result = self.cart_details(product_data)
        remove_result = self.remove_product_from_cart()
        return {
            "products_nav_result": products_nav_result,
            "search_result": search_result,
            "open_product_result": open_product_result,
            "view_product_result": view_product_result,
            "add_result": add_result,
            "cart_nav_result": cart_nav_result,
            "cart_result": cart_result,
            "remove_result": remove_result
        }

    def verify_place_order(self, login_data, product_data, order_data):
        self.logger.info(f"Verifying place order")
        login_nav_result = self.navigate_to("login")
        login_result = self.login(login_data)
        products_nav_result = self.navigate_to("products")
        search_result = self.search_product(product_data)
        open_product_result = self.view_product(product_data)
        view_product_result = self.product_details(product_data)
        add_result = self.add_product_to_cart(product_data)
        cart_nav_result = self.navigate_to("cart")
        cart_result = self.cart_details(product_data)
        order_result = self.checkout(order_data)
        logout_result = self.logout()
        return {
            "login_nav_result": login_nav_result,
            "login_result": login_result,
            "products_nav_result": products_nav_result,
            "search_result": search_result,
            "open_product_result": open_product_result,
            "view_product_result": view_product_result,
            "add_result": add_result,
            "cart_nav_result": cart_nav_result,
            "cart_result": cart_result,
            "order_result": order_result,
            "logout_result": logout_result
        }

    def verify_product_filters(self, product_data):
        self.logger.info(f"Verifying product filters")
        nav_result = self.navigate_to("products")
        category_result = self.product_category_filter(product_data)
        brand_result = self.product_brand_filter(product_data)
        return {
            "nav_result": nav_result,
            "category_result": category_result,
            "brand_result": brand_result
        }

    def verify_navigations(self):
        self.logger.info(f"Verifying page navigations")
        home_nav_result = self.navigate_to("home")
        products_nav_result = self.navigate_to("products")
        cart_nav_result = self.navigate_to("cart")
        login_nav_result = self.navigate_to("login")
        signup_nav_result = self.navigate_to("signup")
        testcases_nav_result = self.navigate_to("testcases")
        apitesting_nav_result = self.navigate_to("apitesting")
        contactus_nav_result = self.navigate_to("contactus")
        return {
            "home_nav_result": home_nav_result,
            "products_nav_result": products_nav_result,
            "cart_nav_result": cart_nav_result,
            "login_nav_result": login_nav_result,
            "signup_nav_result": signup_nav_result,
            "testcases_nav_result": testcases_nav_result,
            "apitesting_nav_result": apitesting_nav_result,
            "contactus_nav_result": contactus_nav_result
        }
