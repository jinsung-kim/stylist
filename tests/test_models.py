import unittest
import sys
import os
from models.models import ClothingItem

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from models.models import User, Pet, Species, Coordinate


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
            "Stussy New Legacy Logo T Shirt",
            "White/Black",
            "Stussy/OurLegacy",
            "Warm,Cold",
            "TOP",
        )

        # self.user1.add_pet(self.pet1)
        # self.user2.add_pet(self.pet2)
        pass

    def tearDown(self) -> None:
        """
        Objects to be destroyed are put here when the tests are over
        """
        pass

    def test_user_comp(self) -> None:
        #     self.assertNotEqual(self.user1, self.user2)

        #     # Both have one pet
        #     self.assertEqual(len(self.user1.pets), len(self.user2.pets))

        #     self.assertEqual(self.user1.location, self.user2.location)

        # def test_pet_comp(self):
        #     self.assertNotEqual(self.pet1, self.pet2)

        #     self.assertNotEqual(self.pet1.breed, self.pet2.breed)
        #     self.assertNotEqual(self.pet1.owner, self.pet2.owner)
        #     self.assertNotEqual(self.pet1.species, self.pet2.species)
        pass


# Running the unit tests above
if __name__ == "__main__":
    unittest.main()
