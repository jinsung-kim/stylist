import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.models import ClothingItem


class TestUser(unittest.TestCase):
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
            "HAT",
        )

        self.hat1_again = ClothingItem(
            "Stussy Beanie",
            "Black/White",
            "Stussy",
            "Warm,Cold",
            "HAT",
        )

        self.hat1_again_in_white = ClothingItem(
            "Stussy Beanie",
            "White/Black",
            "Stussy",
            "Warm,Cold",
            "HAT",
        )

        self.hat1_different_brand = ClothingItem(
            "Stussy Beanie",
            "White/Black",
            "Stussy",
            "Warm,Cold",
            "HAT",
        )

        self.hat2 = ClothingItem(
            "Supreme Cap",
            "Red/White",
            "Supreme/Gortex",
            "Warm,Cold",
            "HAT",
        )

        self.top1 = ClothingItem(
            "Supreme Miles Davis T Shirt",
            "Navy Blue/Pink",
            "Supreme",
            "Warm,Cold",
            "TOP",
        )

        self.top2 = ClothingItem(
            "Black Blank T Shirt",
            "Black",
            "NoBrand",
            "Warm,Cold",
            "TOP",
        )

        self.top3 = ClothingItem(
            "Billie Eilish Murakami Oversized T Shirt",
            "Black",
            "Uniqlo/Murakami",
            "Warm,Cold",
            "TOP",
        )

        self.pants1 = ClothingItem(
            "Dickies Black Double Knee",
            "Black",
            "Dickies",
            "Warm,Cold",
            "PANT",
        )

        self.pants2 = ClothingItem(
            "Vintage Levis 517 Orange Tab",
            "Blue",
            "Levis",
            "Warm,Cold",
            "PANT",
        )

        pass

    def tearDown(self) -> None:
        """
        Objects to be destroyed are put here when the tests are over
        """
        pass

    def test_user_comp(self) -> None:

        # Hat check
        self.assertNotEqual(self.hat1, self.hat2)  # Completely different item
        self.assertEqual(
            self.hat1, self.hat1_again
        )  # Same exact hat - just different object
        self.assertNotEqual(
            self.hat1, self.hat1_again_in_white
        )  # Different color = not equal
        self.assertNotEqual(
            self.hat1, self.hat1_different_brand
        )  # Different brand = not equal

        # Different type checks
        self.assertNotEqual(self.hat1, self.pants1)
        self.assertNotEqual(self.hat1_again, self.top1)


# Running the unit tests above
if __name__ == "__main__":
    unittest.main()
