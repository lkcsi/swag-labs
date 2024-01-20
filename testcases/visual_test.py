from base import BaseTest
import pytest
import os
from utilities import compare_images, params_from_json as params

ACTUAL = "actual"
CORRECT = "correct"
RESULT = "result"


class TestVisual(BaseTest):

    @pytest.mark.visualtest(RESULT)
    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("username,password", params("testdata/valid_credentials.json"))
    def test_inventory_visual(self, username, password):

        self.capture_correct_env(self.go_to_inventory)
        self.capture_tested_env(self.go_to_inventory, username, password)
        self.compare()

    @pytest.mark.visualtest(RESULT)
    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("username,password", params("testdata/valid_credentials.json"))
    def test_details_visual(self, username, password):
        self.capture_correct_env(self.go_to_details)
        self.capture_tested_env(self.go_to_details, username, password)
        self.compare()

    @pytest.mark.visualtest(RESULT)
    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("username,password", params("testdata/valid_credentials.json"))
    def test_cart_visual(self, username, password):
        self.capture_correct_env(self.go_to_cart)
        self.capture_tested_env(self.go_to_cart, username, password)
        self.compare()

    @pytest.mark.visualtest(RESULT)
    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("username,password", params("testdata/valid_credentials.json"))
    def test_checkout_one_visual(self, username, password):
        self.capture_correct_env(self.go_to_checkout_one)
        self.capture_tested_env(self.go_to_checkout_one, username, password)
        self.compare()

    @pytest.mark.visualtest(RESULT)
    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("username,password", params("testdata/valid_credentials.json"))
    def test_checkout_two_visual(self, username, password):
        self.capture_correct_env(self.go_to_checkout_two)
        self.capture_tested_env(self.go_to_checkout_two, username, password)
        self.compare()

    @pytest.mark.visualtest(RESULT)
    @pytest.mark.usefixtures("setup")
    @pytest.mark.parametrize("username,password", params("testdata/valid_credentials.json"))
    def test_finish_visual(self, username, password):
        self.capture_correct_env(self.go_to_finish)
        self.capture_tested_env(self.go_to_finish, username, password)
        self.compare()

    def go_to_inventory(self, username, password):
        inventory = self.login_page.login(username, password)
        inventory.add_item(0)

    def go_to_details(self, username, password):
        inventory = self.login_page.login(username, password)
        inventory[0].click_image()

    def go_to_cart(self, username, password):
        inventory = self.login_page.login(username, password)
        inventory.add_item(0)
        return self.header.click_cart()

    def go_to_checkout_one(self, username, password):
        cart = self.go_to_cart(username, password)
        return cart.checkout()

    def go_to_checkout_two(self, username, password):
        checkout_one = self.go_to_checkout_one(username, password)
        return checkout_one.fill_and_continue()

    def go_to_finish(self, username, password):
        checkout_two = self.go_to_checkout_two(username, password)
        checkout_two.finish()

    def compare(self):
        assert compare_images(CORRECT, ACTUAL, RESULT) is True, "images are different in the tested environment"

    def capture_correct_env(self, navigate):
        navigate("standard_user", "secret_sauce")
        self.take_screenshot(CORRECT)

        self.header.logout()
        self.driver.execute_script("window.localStorage.clear();")

    def capture_tested_env(self, navigate, username, password):
        navigate(username, password)
        self.take_screenshot(ACTUAL)

    def take_screenshot(self, file_name):
        file_path = os.path.join("screenshots", f"{file_name}.png")
        self.driver.save_screenshot(file_path)
