import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.models import Graph, Node, Rule, RuleType


class TestDataStructures(unittest.TestCase):
    def setUp(self) -> None:
        """
        Objects that are initialized in here are created
        when we create the class and run the tests.
        """
        self.color_rule = Rule("COLOR")
        self.brand_rule = Rule("BRAND")

        self.node1 = Node("Stussy", 1, True)
        self.node2 = Node("CarharttWIP", 1, False)
        self.node3 = Node("Levis", 1, False)
        self.node4 = self.node1

    def tearDown(self) -> None:
        return super().tearDown()

    def test_initialization(self) -> None:
        self.assertNotEqual(self.node1, self.node2)
        self.assertEqual(self.node1, self.node4)

        self.assertNotEqual(self.color_rule, self.brand_rule)

    def test_insertion(self) -> None:

        # Adding color combinations that I like
        self.color_rule.add_combo("White,Black,White", 1)
        self.color_rule.add_combo("White,LightBlue", 2)
        self.color_rule.add_combo("White,Grey", 1)

        # Adding brand combinations that fit me with weights
        self.brand_rule.add_combo("Stussy,Levis", 2)
        self.brand_rule.add_combo("Uniqlo,Levis", 1)
        self.brand_rule.add_combo("Stussy,Nike", 1)
        self.brand_rule.add_combo("Stussy,Levis,Nike", 3)

        self.assertEqual(
            self.color_rule.combo_exists(["White", "Black", "White"])[0], True
        )
        self.assertEqual(
            self.color_rule.combo_exists(["White", "Grey", "White"])[0], False
        )

        # Combo exists check
        self.assertEqual(self.color_rule.combo_exists([])[0], False)
        self.assertEqual(self.brand_rule.combo_exists(["Stussy"])[0], False)
        self.assertEqual(self.brand_rule.combo_exists(["Stussy,Nike,Adidas"])[0], False)

        # Score checks
        self.assertEqual(self.brand_rule.combo_exists(["Stussy", "Levis"])[1], 2)
        self.assertEqual(self.brand_rule.combo_exists(["Stussy"])[1], 0)
        self.assertEqual(self.brand_rule.combo_exists(["Stussy,Levis,Adidas"])[1], -1)


if __name__ == "__main__":
    unittest.main()
