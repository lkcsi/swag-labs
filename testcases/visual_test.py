from base import BaseTest
import pytest
import os
from utilities import compare_images, params_from_json as params

ACTUAL = "actual"
CORRECT = "correct"
RESULT = "result"

class TestVisual(BaseTest):

    #@pytest.mark.parametrize("username,password", params("testdata/valid_credentials.json"))
    @pytest.mark.visualtest(RESULT)
    @pytest.mark.usefixtures("setup")
    def test_difference_inventory(self, username="visual_user", password="secret_sauce"):

        self.correct_env(self.go_to_inventory)
        self.tested_env(self.go_to_inventory, username, password)

        assert compare_images(CORRECT, ACTUAL, RESULT) is True, "images are different than expected"

    @pytest.mark.visualtest(RESULT)
    @pytest.mark.usefixtures("setup")
    #@pytest.mark.parametrize("username,password", params("testdata/valid_credentials.json"))
    def test_difference_details(self, username="visual_user", password="secret_sauce"):
        self.correct_env(self.go_to_details)
        self.tested_env(self.go_to_details, username, password)

        assert compare_images(CORRECT, ACTUAL, RESULT) is True, "images are different than expected"

    @pytest.mark.visualtest(RESULT)
    @pytest.mark.usefixtures("setup")
    #@pytest.mark.parametrize("username,password", params("testdata/valid_credentials.json"))
    def test_difference_cart(self, username="visual_user", password="secret_sauce"):
        self.correct_env(self.go_to_cart)
        self.tested_env(self.go_to_cart, username, password)

        assert compare_images(CORRECT, ACTUAL, RESULT) is True, "images are different than expected"

    @pytest.mark.visualtest(RESULT)
    @pytest.mark.usefixtures("setup")
    #@pytest.mark.parametrize("username,password", params("testdata/valid_credentials.json"))
    def test_difference_checkout_one(self, username="visual_user", password="secret_sauce"):
        self.correct_env(self.go_to_checkout_one)
        self.tested_env(self.go_to_checkout_one, username, password)

        assert compare_images(CORRECT, ACTUAL, RESULT) is True, "images are different than expected"

    @pytest.mark.visualtest(RESULT)
    @pytest.mark.usefixtures("setup")
    #@pytest.mark.parametrize("username,password", params("testdata/valid_credentials.json"))
    def test_difference_checkout_two(self, username="visual_user", password="secret_sauce"):
        self.correct_env(self.go_to_checkout_two)
        self.tested_env(self.go_to_checkout_two, username, password)

        assert compare_images(CORRECT, ACTUAL, RESULT) is True, "images are different than expected"

    @pytest.mark.visualtest(RESULT)
    @pytest.mark.usefixtures("setup")
    #@pytest.mark.parametrize("username,password", params("testdata/valid_credentials.json"))
    def test_difference_finish(self, username="visual_user", password="secret_sauce"):
        self.correct_env(self.go_to_finish)
        self.tested_env(self.go_to_finish, username, password)

        assert compare_images(CORRECT, ACTUAL, RESULT) is True, "images are different than expected"

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

    def correct_env(self, steps):
        steps("standard_user", "secret_sauce")
        self.take_screenshot(CORRECT)
        self.header.logout()
        self.driver.execute_script("window.localStorage.clear();")

    def tested_env(self, steps, username, password):
        steps(username, password)
        self.take_screenshot(ACTUAL)

    def take_screenshot(self, file_name):
        file_path = os.path.join("screenshots", f"{file_name}.png")
        self.driver.save_screenshot(file_path)

