from parameterized import parameterized_class
from database.database import users
import unittest

from base_test import BaseTestCase


@parameterized_class(users())
class LoginTestCase(BaseTestCase):

    def test_logout(self):
        self.login()
        self.logout()


if __name__ == "__main__":
    unittest.main()
