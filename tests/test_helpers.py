import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers.outfit_formatter import format_outfit, weather_appropriate
from models.models import ClothingItem

class TestHelperFunctions(unittest.TestCase):

    def setUp(self) -> None:
        """
        Objects that are initialized in here are created
        when we create the class and run the tests.
        """
        self.hat1 = ClothingItem(
            "Stussy Beanie",
            "Black/White",
            "Stussy",
            "Warm,Cold",
            "",
        )

        self.hat2 = ClothingItem(
            "Supreme Cap",
            "Red/White",
            "Supreme/Gortex",
            "Warm",
            "",
        )

        self.top1 = ClothingItem(
            "Supreme Miles Davis T Shirt",
            "Navy Blue/Pink",
            "Supreme",
            "Warm",
            "",
        )

    def tearDown(self) -> None:
        return super().tearDown()

    def test_temperature(self) -> None:
        # Hat 1: Can be used in both
        self.assertEqual(weather_appropriate(self.hat1, 30), True)
        self.assertEqual(weather_appropriate(self.hat1, 70), True)
        # Hat 2: Only good when warm
        self.assertEqual(weather_appropriate(self.hat2, 20), False)
        self.assertEqual(weather_appropriate(self.hat2, 70), True)
        # Top 1: Only good when warm
        self.assertEqual(weather_appropriate(self.top1, 10), False)
        self.assertEqual(weather_appropriate(self.top1, 70), True)


if __name__ == "__main__":
    unittest.main()
