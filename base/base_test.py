class BaseTest:
    login_page = None
    header = None
    driver = None
    base_url = None
    username = None
    password = None

    def login(self):
        inventory = self.login_page.login(self.username, self.password)
        return inventory

    def go_to_inventory(self):
        inventory = self.login()
        inventory.add_item(0)

    def go_to_details(self):
        inventory = self.login()
        inventory[0].click_image()

    def go_to_cart(self):
        inventory = self.login()
        inventory.add_item(0)
        return self.header.click_cart()

    def go_to_checkout_one(self):
        cart = self.go_to_cart()
        return cart.checkout()

    def go_to_checkout_two(self):
        checkout_one = self.go_to_checkout_one()
        return checkout_one.fill_and_continue()

    def go_to_finish(self):
        checkout_two = self.go_to_checkout_two()
        checkout_two.finish()

    def check_counter(self, expected):
        assert expected == self.header.cart.counter(), "cart counter is not correct according to the selected items"
