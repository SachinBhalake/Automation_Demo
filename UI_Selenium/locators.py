from selenium.webdriver.common.by import By


class Locators:

    #static locators

    _ad_iframe = (By.XPATH, "//iframe[@id='aswift_3']")
    _ad_close_button = (By.XPATH, "//div[@id='dismiss-button']")

    _home_button = (By.XPATH, "//a[@href='/' and text()=' Home']")
    _products_button = (By.XPATH, "//a[@href='/products']")
    _cart_button = (By.XPATH, "//a[@href='/view_cart']")
    _signup_login_button = (By.XPATH, "//a[@href='/login']")
    _testcases_button = (By.XPATH, "//a[@href='/test_cases']")
    _api_testing_button = (By.XPATH, "//a[@href='/api_list']")
    _contact_us_button = (By.XPATH, "//a[@href='/contact_us']")

    _homepage_slider = (By.XPATH, "//div[@id='slider-carousel'] ")

    _signup_header1 = (By.XPATH, "//h2[text()='New User Signup!']")
    _signup_username = (By.XPATH, "//input[@data-qa='signup-name']")
    _signup_email = (By.XPATH, "//input[@data-qa='signup-email']")
    _signup_button = (By.XPATH, "//button[@data-qa='signup-button']")
    _signup_error = (By.XPATH, "//p[text()='Email Address already exist!']")
    _signup_header2 = (By.XPATH, "//b[text()='Enter Account Information']")
    _signup_title1 = (By.XPATH, "//input[@id='id_gender1']")
    _signup_title2 = (By.XPATH, "//input[@id='id_gender2']")
    _signup_password = (By.XPATH, "//input[@id='password']")
    _signup_date = (By.XPATH, "//select[@id='days']")
    _signup_month = (By.XPATH, "//select[@id='months']")
    _signup_year = (By.XPATH, "//select[@id='years']")
    _signup_newsletter = (By.XPATH, "//label[@for='newsletter']")
    _signup_offer = (By.XPATH, "//label[@for='optin']")
    _signup_firstname = (By.XPATH, "//input[@id='first_name']")
    _signup_lastname = (By.XPATH, "//input[@id='last_name']")
    _signup_company = (By.XPATH, "//input[@id='company']")
    _signup_address1 = (By.XPATH, "//input[@id='address1']")
    _signup_address2 = (By.XPATH, "//input[@id='address2']")
    _signup_country = (By.XPATH, "//select[@id='country']")
    _signup_state = (By.XPATH, "//input[@id='state']")
    _signup_city = (By.XPATH, "//input[@id='city']")
    _signup_zip = (By.XPATH, "//input[@id='zipcode']")
    _signup_mobile = (By.XPATH, "//input[@id='mobile_number']")
    _signup_create_account_button = (By.XPATH, "//button[@data-qa='create-account']")
    _signup_success = (By.XPATH, "//b[text()='Account Created!']")
    _signup_continue_button = (By.XPATH, "//a[@data-qa='continue-button']")

    _delete_account_button = (By.XPATH, "//a[@href='/delete_account']")
    _delete_account_success = (By.XPATH, "//b[text()='Account Deleted!']")
    _delete_account_continue_button = (By.XPATH, "//a[@data-qa='continue-button']")

    _login_header = (By.XPATH, "//h2[text()='Login to your account']")
    _login_username = (By.XPATH, "//input[@data-qa='login-email']")
    _login_password = (By.XPATH, "//input[@data-qa='login-password']")
    _login_button = (By.XPATH, "//button[@data-qa='login-button']")
    _login_error = (By.XPATH, "//p[text()='Your email or password is incorrect!']")
    _login_success = (By.XPATH, "//a[text()=' Logged in as ']")
    _logout_button = (By.XPATH, "//a[@href='/logout']")

    _contact_us_header = (By.XPATH, "//h2[text()='Get In Touch']")
    _contact_us_name = (By.XPATH, "//input[@data-qa='name']")
    _contact_us_email = (By.XPATH, "//input[@data-qa='email']")
    _contact_us_subject = (By.XPATH, "//input[@data-qa='subject']")
    _contact_us_message = (By.XPATH, "//textarea[@name='message']")
    _contact_us_file = (By.XPATH, "//input[@name='upload_file']")
    _contact_us_submit_button = (By.XPATH, "//input[@data-qa='submit-button']")
    _contact_us_success = (By.XPATH, "//div[text()='Success! Your details have been submitted successfully.']")

    _search_product_box = (By.XPATH, "//input[@id='search_product']")
    _search_product_button = (By.XPATH, "//button[@id='submit_search']")
    _search_product_results = (By.XPATH, "//div[@class='product-image-wrapper']")
    _search_product_results_text = (By.XPATH, "//div[contains(@class, 'productinfo')]/p")

    _view_product_button = (By.XPATH, "//a[contains(@href,'/product_details')]")
    _view_product_name = (By.XPATH, "//div[@class='product-information']/h2")
    _view_product_category = (By.XPATH, "//div[@class='product-information']/p[contains(text(),'Category:')]")
    _view_product_availability = (By.XPATH, "//div[@class='product-information']/p[contains(*,'Availability:')]")
    _view_product_condition = (By.XPATH, "//div[@class='product-information']/p[contains(*,'Condition:')]")
    _view_product_brand = (By.XPATH, "//div[@class='product-information']/p[contains(*,'Brand:')]")
    _view_product_price = (By.XPATH, "//div[@class='product-information']/span/span[contains(text(),'Rs.')]")
    _view_product_quantity = (By.XPATH, "//input[@id='quantity']")
    _add_to_cart_button = (By.XPATH, "//div[@class='product-information']/span/button")
    _add_to_cart_success = (By.XPATH, "//p[text()='Your product has been added to cart.']")
    _continue_shopping_button = (By.XPATH, "//button[text()='Continue Shopping']")

    _cart_product_name = (By.XPATH, "//td[@class='cart_description']/h4")
    _cart_product_category = (By.XPATH, "//td[@class='cart_description']/p")
    _cart_product_price = (By.XPATH, "//td[@class='cart_price']/p")
    _cart_product_quantity = (By.XPATH, "//td[@class='cart_quantity']/button")
    _cart_product_remove_button = (By.XPATH, "//a[@class='cart_quantity_delete']")
    _cart_product_remove_success = (By.XPATH, "//span[@id='empty_cart']")
    _cart_proceed_checkout_button = (By.XPATH, "//a[text()='Proceed To Checkout']")

    _place_order_message = (By.XPATH, "//textarea[@name='message']")
    _place_order_button = (By.XPATH, "//a[@href='/payment']")

    _payment_header = (By.XPATH, "//h2[text()='Payment']")
    _payment_card_name = (By.XPATH, "//input[@name='name_on_card']")
    _payment_card_number = (By.XPATH, "//input[@name='card_number']")
    _payment_cvc = (By.XPATH, "//input[@name='cvc']")
    _payment_expiry_month = (By.XPATH, "//input[@name='expiry_month']")
    _payment_expiry_year = (By.XPATH, "//input[@name='expiry_year']")
    _pay_and_confirm_button = (By.XPATH, "//button[@data-qa='pay-button']")
    _order_success = (By.XPATH, "//p[text()='Congratulations! Your order has been confirmed!']")

    #dynamic locators

    @staticmethod
    def category_button(product_category):
        return (By.XPATH, f"//a[@href='#{product_category}']")

    @staticmethod
    def subcategory_button(product_category, product_subcategory):
        return (By.XPATH, f"//div[@id='{product_category}']//a[text()='{product_subcategory} ']")

    @staticmethod
    def category_filter_results_header(product_category, product_subcategory):
        return (By.XPATH, f"//h2[text()='{product_category} - {product_subcategory} Products']")

    @staticmethod
    def brand_button(brand):
        return (By.XPATH, f"//a[@href='/brand_products/{brand}']")

    @staticmethod
    def brand_filter_results_header(brand):
        return (By.XPATH, f"//h2[text()='Brand - {brand} Products']")
