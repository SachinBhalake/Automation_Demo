class Locators:

    # -------- Ads --------
    ad_iframe = "iframe#aswift_3"
    ad_close_button = "#dismiss-button"

    # -------- Navbar --------
    home_button = "li a[href='/']"
    products_button = "li a[href='/products']"
    cart_button = "li a[href='/view_cart']"
    signup_login_button = "li a[href='/login']"
    testcases_button = "li a[href='/test_cases']"
    api_testing_button = "li a[href='/api_list']"
    contact_us_button = "li a[href='/contact_us']"

    # -------- Signup --------
    signup_username = "[data-qa='signup-name']"
    signup_email = "[data-qa='signup-email']"
    signup_button = "[data-qa='signup-button']"
    signup_error = "text=Email Address already exist!"
    signup_title1 = "#id_gender1"
    signup_title2 = "#id_gender2"
    signup_password = "#password"
    signup_date = "#days"
    signup_month = "#months"
    signup_year = "#years"
    signup_newsletter = "label[for='newsletter']"
    signup_offer = "label[for='optin']"
    signup_firstname = "#first_name"
    signup_lastname = "#last_name"
    signup_company = "#company"
    signup_address1 = "#address1"
    signup_address2 = "#address2"
    signup_country = "#country"
    signup_state = "#state"
    signup_city = "#city"
    signup_zip = "#zipcode"
    signup_mobile = "#mobile_number"
    signup_create_account_button = "[data-qa='create-account']"
    signup_success = "text=Account Created!"
    signup_continue_button = "[data-qa='continue-button']"

    # -------- Delete Account --------
    delete_account_button = "a[href='/delete_account']"
    delete_account_success = "text=Account Deleted!"

    # -------- Login --------
    login_username = "[data-qa='login-email']"
    login_password = "[data-qa='login-password']"
    login_button = "[data-qa='login-button']"
    login_error = "text=Your email or password is incorrect!"
    login_success = "text=Logged in as"
    logout_button = "a[href='/logout']"

    # -------- Contact Us --------
    contact_us_name = "[data-qa='name']"
    contact_us_email = "[data-qa='email']"
    contact_us_subject = "[data-qa='subject']"
    contact_us_message = "textarea[name='message']"
    contact_us_file = "input[name='upload_file']"
    contact_us_submit_button = "[data-qa='submit-button']"
    contact_us_success = "text=Success! Your details have been submitted successfully."

    # -------- Search --------
    search_product_box = "#search_product"
    search_product_button = "#submit_search"
    search_product_results = ".product-image-wrapper"
    search_product_results_text = ".productinfo p"

    # -------- Product --------
    view_product_button = "a[href*='product_details']"
    view_product_name = ".product-information h2"
    view_product_category = ".product-information p:has-text('Category')"
    view_product_availability = ".product-information p:has-text('Availability')"
    view_product_condition = ".product-information p:has-text('Condition')"
    view_product_brand = ".product-information p:has-text('Brand')"
    view_product_price = ".product-information span span:has-text('Rs.')"
    view_product_quantity = "#quantity"
    add_to_cart_button = ".product-information button"
    add_to_cart_success = "text=Your product has been added to cart."
    continue_shopping_button = "text=Continue Shopping"

    # -------- Cart --------
    cart_product_name = ".cart_description h4"
    cart_product_category = ".cart_description p"
    cart_product_price = ".cart_price p"
    cart_product_quantity = ".cart_quantity button"
    cart_product_remove_button = ".cart_quantity_delete"
    cart_product_remove_success = "#empty_cart"
    cart_proceed_checkout_button = "text=Proceed To Checkout"

    # -------- Order --------
    place_order_message = "textarea[name='message']"
    place_order_button = "a[href='/payment']"

    # -------- Payment --------
    payment_card_name = "[name='name_on_card']"
    payment_card_number = "[name='card_number']"
    payment_cvc = "[name='cvc']"
    payment_expiry_month = "[name='expiry_month']"
    payment_expiry_year = "[name='expiry_year']"
    pay_and_confirm_button = "[data-qa='pay-button']"
    order_success = "text=Congratulations! Your order has been confirmed!"

    # -------- Dynamic Locators --------
    @staticmethod
    def category_button(category):
        return f"a[href='#{category}']"

    @staticmethod
    def subcategory_button(category, subcategory):
        return f"#{category} >> text={subcategory}"

    @staticmethod
    def category_filter_results_header(category, subcategory):
        return f"text={category} - {subcategory} Products"

    @staticmethod
    def brand_button(brand):
        return f"a[href='/brand_products/{brand}']"

    @staticmethod
    def brand_filter_results_header(brand):
        return f"text=Brand - {brand} Products"