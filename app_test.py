"""Unit test file for app.py"""
from app import returnBackwardsString
import unittest

class TestApp(unittest.TestCase):
    """Unit tests defined for app.py"""

    def test_return_backwards_string(self):
        random_string = "This is my test running"
        random_string_reversed = "This is my test string"
        self.assertEqual(random_string_reversed, returnBackwardsString(random_string))

if __name__ == '__main__':
    unittest.main()
