from base import BaseTest
import pytest
import os
from utilities import compare_images

ACTUAL = "actual"
CORRECT = "correct"
RESULT = "compare_result"


class TestVisual(BaseTest):

    @pytest.mark.visualtest(RESULT)
    @pytest.mark.usefixtures("setup")
    def test_inventory_visual(self):

        self.capture_tested_env(self.go_to_inventory)
        self.capture_correct_env(self.go_to_inventory)
        self.compare()

    @pytest.mark.visualtest(RESULT)
    @pytest.mark.usefixtures("setup")
    def test_details_visual(self):
        self.capture_tested_env(self.go_to_details)
        self.capture_correct_env(self.go_to_details)
        self.compare()

    @pytest.mark.visualtest(RESULT)
    @pytest.mark.usefixtures("setup")
    def test_cart_visual(self):
        self.capture_tested_env(self.go_to_cart)
        self.capture_correct_env(self.go_to_cart)
        self.compare()

    @pytest.mark.visualtest(RESULT)
    @pytest.mark.usefixtures("setup")
    def test_checkout_one_visual(self):
        self.capture_tested_env(self.go_to_checkout_one)
        self.capture_correct_env(self.go_to_checkout_one)
        self.compare()

    @pytest.mark.visualtest(RESULT)
    @pytest.mark.usefixtures("setup")
    def test_checkout_two_visual(self):
        self.capture_tested_env(self.go_to_checkout_two)
        self.capture_correct_env(self.go_to_checkout_two)
        self.compare()

    @pytest.mark.visualtest(RESULT)
    @pytest.mark.usefixtures("setup")
    def test_finish_visual(self):
        self.capture_tested_env(self.go_to_finish)
        self.capture_correct_env(self.go_to_finish)
        self.compare()

    @staticmethod
    def compare():
        assert compare_images(CORRECT, ACTUAL, RESULT) is True, "images are different in the tested environment"

    def capture_correct_env(self, navigate):
        self.username = os.getenv("CORRECT_ENV_USERNAME")
        self.base_url = os.getenv("CORRECT_ENV_BASE_URL")
        self.driver.get(self.base_url)
        self.driver.fullscreen_window()
        navigate()
        self.take_screenshot(CORRECT)

    def capture_tested_env(self, navigate):
        navigate()
        self.take_screenshot(ACTUAL)
        self.header.logout()
        self.driver.execute_script("window.localStorage.clear();")

    def take_screenshot(self, file_name):
        file_path = os.path.join("screenshots", f"{file_name}.png")
        self.driver.save_screenshot(file_path)
