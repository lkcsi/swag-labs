import pages


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
        self.check_title(pages.InventoryPage.TITLE)
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

    def go_to_cart(self, *select_items, add_all=False):
        self.go_to_inventory(add_all, *select_items)
        cart_page = self.header.click_cart()
        self.check_title(pages.CartPage.TITLE)
        return cart_page

    def go_to_checkout_one(self, *select_items, add_all=False):
        cart = self.go_to_cart(add_all, *select_items)
        checkout_one_page = cart.checkout()
        self.check_title(pages.CheckoutOnePage.TITLE)
        return checkout_one_page

    def go_to_checkout_two(self, *select_items, add_all=False):
        checkout_one = self.go_to_checkout_one(*select_items, add_all)
        checkout_two_page = checkout_one.fill_and_continue()
        self.check_title(pages.CheckoutTwoPage.TITLE)
        return checkout_two_page

    def go_to_finish(self, *select_items, add_all=False):
        checkout_two = self.go_to_checkout_two(*select_items, add_all)
        complete_page = checkout_two.finish()
        self.check_title(pages.CompletePage.TITLE)
        return complete_page

    def logout(self):
        self.header.logout()

    def check_title(self, expected_title):
        current_title = self.header.get_title()
        assert current_title == expected_title, (f"expected page title was: {expected_title} "
                                                 f"but we are in: {current_title}")

    def check_counter(self, expected):
        assert expected == self.header.cart.counter(), "cart counter is not correct according to the selected items"
