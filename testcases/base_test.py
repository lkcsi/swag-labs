from pages import InventoryPage, CartPage, CheckoutOnePage, CheckoutTwoPage, CompletePage


class BaseTest:
    login_page = None
    header = None
    driver = None
    base_url = None
    username = None
    password = None

    def login(self):
        return self.login_page.login(self.username, self.password)

    def go_to_inventory(self, add_all=False, *select_items):
        inventory = self.login()
        self.check_title(InventoryPage.TITLE)
        if add_all:
            inventory.add_all_items()
            return inventory
        for key in select_items:
            inventory.add_item(key)
        return inventory

    def go_to_details(self, item_key):
        inventory = self.login()
        details = inventory[item_key].click_image()
        return details

    def go_to_cart(self, add_all=False, *select_items):
        self.go_to_inventory(add_all, *select_items)
        cart_page = self.header.click_cart()
        self.check_title(CartPage.TITLE)
        return cart_page

    def go_to_checkout_one(self, add_all=False, *select_items):
        cart = self.go_to_cart(add_all, *select_items)
        checkout_one_page = cart.checkout()
        self.check_title(CheckoutOnePage.TITLE)
        return checkout_one_page

    def go_to_checkout_two(self, add_all=False, *select_items):
        checkout_one = self.go_to_checkout_one(add_all, *select_items)
        checkout_two_page = checkout_one.fill_and_continue()
        self.check_title(CheckoutTwoPage.TITLE)
        return checkout_two_page

    def go_to_finish(self, add_all=False, *select_items):
        checkout_two = self.go_to_checkout_two(add_all, *select_items)
        complete_page = checkout_two.finish()
        self.check_title(CompletePage.TITLE)
        return complete_page

    def logout(self):
        self.header.logout()

    def check_title(self, expected_title):
        current_title = self.header.get_title()
        assert current_title == expected_title, (f"expected page title was: {expected_title} "
                                                 f"but we are in: {current_title}")

    def check_counter(self, expected):
        assert expected == self.header.cart.counter(), "cart counter is not correct according to the selected items"
