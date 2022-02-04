import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers.outfit_formatter import format_outfit, weather_appropriate


class TestHelperFunctions(unittest.TestCase):

    def setUp(self) -> None:
        """
        Objects that are initialized in here are created
        when we create the class and run the tests.
        """
        pass

    def tearDown(self) -> None:
        return super().tearDown()

    def test_initialization(self) -> None:
        pass

    def test_insertion(self) -> None:
        pass


if __name__ == "__main__":
    unittest.main()
