import utilities
from testcases import BaseTest
import pytest
from utilities import compare_images

ACTUAL = "actual"
CORRECT = "correct"
RESULT = "compare_result"


class TestVisual(BaseTest):

    correct_env_username = None
    correct_env_base_url = None

    @pytest.mark.visual(RESULT)
    @pytest.mark.usefixtures("setup", "correct_env")
    def test_inventory_visual(self):
        self.perform(lambda: self.go_to_inventory(add_all=True))

    @pytest.mark.visual(RESULT)
    @pytest.mark.usefixtures("setup", "correct_env")
    def test_details_visual(self):
        self.perform(lambda: self.go_to_details(item_key=0))

    @pytest.mark.visual(RESULT)
    @pytest.mark.usefixtures("setup", "correct_env")
    def test_cart_visual(self):
        self.perform(lambda: self.go_to_cart(False, 0, 1))

    @pytest.mark.visual(RESULT)
    @pytest.mark.usefixtures("setup", "correct_env")
    def test_checkout_one_visual(self):
        self.perform(lambda: self.go_to_checkout_one(False, 0, 1))

    @pytest.mark.visual(RESULT)
    @pytest.mark.usefixtures("setup", "correct_env")
    def test_checkout_two_visual(self):
        self.perform(lambda: self.go_to_checkout_two(False, 0, 1))

    @pytest.mark.visual(RESULT)
    @pytest.mark.usefixtures("setup", "correct_env")
    def test_finish_visual(self):
        self.perform(lambda: self.go_to_finish(True))

    @staticmethod
    def compare():
        assert compare_images(CORRECT, ACTUAL, RESULT) is True, "images are different in the tested environment"

    def perform(self, test_steps):

        test_steps()
        self.take_screenshot(ACTUAL)

        self.setup_correct_env()
        test_steps()
        self.take_screenshot(CORRECT)

        self.compare()

    def setup_correct_env(self):
        self.header.logout()
        self.driver.execute_script("window.localStorage.clear();")
        self.username = self.correct_env_username
        self.driver.get(self.correct_env_base_url)
        self.driver.fullscreen_window()

    def take_screenshot(self, file_name):
        utilities.take_screenshot(file_name, self.driver)

