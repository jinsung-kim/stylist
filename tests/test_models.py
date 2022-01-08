import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from models.models import User, Pet, Species, Coordinate

class TestUser(unittest.TestCase):

    def setUp(self):
        '''
        Objects that are initialized in here are created 
        when we create the class and run the tests.
        '''
        # self.c = Coordinate(40.714270, -74.005970)
        # self.user1 = User("jinlikescats", "fakepassword1", "Jin", self.c)
        # self.user2 = User("jinlikesdogs", "fakepassword2", "Jin", self.c)

        # self.pet1 = Pet("Garfield", Species.CAT, "Orange Tabby")
        # self.pet2 = Pet("Snoopy", Species.DOG, "Beagle")

        # self.user1.add_pet(self.pet1)
        # self.user2.add_pet(self.pet2)

    def tearDown(self):
        '''
        Objects to be destroyed are put here when the tests are over
        '''
        pass

    def test_user_comp(self):
    #     self.assertNotEqual(self.user1, self.user2)

    #     # Both have one pet
    #     self.assertEqual(len(self.user1.pets), len(self.user2.pets))

    #     self.assertEqual(self.user1.location, self.user2.location)

    # def test_pet_comp(self):
    #     self.assertNotEqual(self.pet1, self.pet2)

    #     self.assertNotEqual(self.pet1.breed, self.pet2.breed)
    #     self.assertNotEqual(self.pet1.owner, self.pet2.owner)
    #     self.assertNotEqual(self.pet1.species, self.pet2.species)


# Running the unit tests above
if __name__ == '__main__':
    unittest.main()