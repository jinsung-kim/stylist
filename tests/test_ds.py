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

        self.color_rule.add_combo("White,Black,White")
        self.color_rule.add_combo("White,LightBlue")
        self.color_rule.add_combo("White,Grey")

        self.assertEqual(
            self.color_rule.combo_exists(["White", "Black", "White"]), True
        )
        self.assertEqual(
            self.color_rule.combo_exists(["White", "Grey", "White"]), False
        )
        self.assertEqual(self.color_rule.combo_exists([]), False)


if __name__ == "__main__":
    unittest.main()
