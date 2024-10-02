from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test=\"error\"]")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self):
        return self.error_message.inner_text()

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.burger_menu = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")

    def add_to_cart(self, item_id: str):
        self.page.click(f"#add-to-cart-{item_id}")

    def get_cart_count(self):
        return self.cart_badge.inner_text()

    def open_burger_menu(self):
        self.burger_menu.click()

    def logout(self):
        self.open_burger_menu()
        self.logout_link.click()

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator("#checkout")

    def navigate(self):
        self.page.click(".shopping_cart_link")

    def proceed_to_checkout(self):
        self.checkout_button.click()

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.thank_you_header = page.locator(".complete-header")

    def fill_information(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()

    def complete_order(self):
        self.finish_button.click()

    def get_confirmation_message(self):
        return self.thank_you_header.inner_text()
