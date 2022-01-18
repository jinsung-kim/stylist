import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.models import ClothingItem, Rule, Graph

# Helper
def get_in_quote(item: str) -> "tuple[str, int]":
    """
    Takes in a string and finds the item name in quotation, and returns an index
    of where the item stops so that the rest of the item can be dealt with

    :param item: str of the entire line in the txt file with the \n stripped
    :return: str of the name in quotes, index which it ends to be sliced outside
    """
    res = ""
    quotes = 0

    for i in range(len(item)):
        if quotes == 2:
            return (res, i)
        elif item[i] == '"':
            quotes += 1
        elif quotes == 1:
            res += item[i]
    return (res, len(item))


class Database:
    # Where most of the program is run
    def __init__(self) -> None:
        """
        clothing_items: dictionary{Clothing}
        rule_set: dictionary{Rules}
        """
        self.clothing_items: dict[str, list[ClothingItem]] = {}
        self.rule_set: dict[str, Rule] = {}

    def load_from_txt(self, filename: str = "rotation.txt") -> bool:
        """
        Reads in a txt file formatted (default rotation.txt) and applies the clothing items and rules
        into the RAM to be processed

        Note: It is important that any operations done should be logged or saved into another txt file
        which will serve as the database

        :param filename: name of the file to look through, must be in the same directory
        :return: whether the function was successful or not
        """
        txt_file = open(filename, "r")

        lines = txt_file.readlines()

        curr = ""

        # target = ["HAT", "TOP", "OUTERWEAR", "PANTS", "SHOES"]
        target = ["TOP", "PANTS", "SHOES"]

        # Add each item in its intended category
        for line in lines:
            line = line.strip("\n")
            if line in target:
                curr = line
                self.clothing_items[curr] = []
            elif len(line) == 0:
                pass
            else:
                re, ind = get_in_quote(line)
                rest_of_line = line[ind + 1 :]
                attributes = rest_of_line.split(" ")
                colors = attributes[0]
                brands = attributes[1]
                weather = attributes[2]
                self.clothing_items[curr].append(
                    ClothingItem(re, colors, brands, weather, curr)
                )

        txt_file.close()

    def load_ruleset_from_txt(self, filename: str = "ruleset.txt") -> bool:
        """
        Reads in a txt file formatted (default ruleset.txt) and applies the clothing items and rules
        into the RAM to be processed

        Note: It is important that any operations done should be logged or saved into another txt file
        which will serve as the database

        :param filename: name of the file to look through, must be in the same directory
        :return: whether the function was successful or not
        """
        txt_file = open(filename, "r")

        lines = txt_file.readlines()

        curr = ""
        curr_weight = 0

        target = ["COLOR", "BRAND"]
        weight = ["GOOD", "BAD"]

        for line in lines:
            line = line.strip("\n")
            if line in target:
                curr = line
                self.rule_set[curr] = Rule(curr)
            elif len(line) > 0 and line in weight:
                curr_weight = 1 if (line == "GOOD") else -1
            elif len(line) > 0:
                self.rule_set[curr].add_combo(line, curr_weight)

        txt_file.close()

    def output_to_txt(self, filename: str) -> bool:
        """
        Prints the output into a text file so the user can save potential fit ideas
        NOTE: If you select a filename already taken in the directory, it may be overwritten

        :param filename: the file that will be created ("saved_fits" -> "saved_fits.txt")
        :return: whether the exporting was successful or not
        """
        pass


def main() -> None:
    """
    Where every object lives and is executed

    TODO: Make this an interactive shell
    """
    db = Database()

    db.load_from_txt()
    db.load_ruleset_from_txt()

    g = Graph()
    g.add_all(db.clothing_items)
    g.add_connections()

    g.generate_fits(db.rule_set)


if __name__ == "__main__":
    main()
