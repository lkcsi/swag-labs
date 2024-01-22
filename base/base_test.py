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

    def go_to_inventory(self):
        inventory = self.login()
        inventory.add_item(0)
        self.check_title(pages.InventoryPage.TITLE)
        return inventory

    def go_to_details(self):
        inventory = self.login()
        details = inventory[0].click_image()
        return details

    def go_to_cart(self):
        inventory = self.login()
        inventory.add_item(0)
        cart_page = self.header.click_cart()
        self.check_title(pages.CartPage.TITLE)
        return cart_page

    def go_to_checkout_one(self):
        cart = self.go_to_cart()
        checkout_one_page = cart.checkout()
        self.check_title(pages.CheckoutOnePage.TITLE)
        return checkout_one_page

    def go_to_checkout_two(self):
        checkout_one = self.go_to_checkout_one()
        checkout_two_page = checkout_one.fill_and_continue()
        self.check_title(pages.CheckoutTwoPage.TITLE)
        return checkout_two_page

    def go_to_finish(self):
        checkout_two = self.go_to_checkout_two()
        complete_page = checkout_two.finish()
        self.check_title(pages.CompletePage.TITLE)
        return complete_page

    def check_title(self, expected_title):
        current_title = self.header.get_title()
        assert current_title == expected_title, (f"expected page title was: {expected_title} "
                                                 f"but we are in: {current_title}")

    def check_counter(self, expected):
        assert expected == self.header.cart.counter(), "cart counter is not correct according to the selected items"
