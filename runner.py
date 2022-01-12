import sys
import os

# from models.models import ClothingItem

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from models.models import User, Pet, Species, Coordinate


class Database:
    # Where most of the program is run
    def __init__(self) -> None:
        """
        clothing_items: set{Clothing}
        rule_set: set{Rules}
        """
        self.clothing_items = set()
        self.rule_set = set()

    def load_from_txt(self, filename: str) -> bool:
        """
        Reads in a txt file formatted (default db.txt) and applies the clothing items and rules
        into the RAM to be processed

        Note: It is important that any operations done should be logged or saved into another txt file
        which will serve as the database
        """
        txt_file = open(filename, "r")

        lines = txt_file.readlines()

        for line in lines:
            print(line)

        txt_file.close()

    def output_to_txt(self, filename: str) -> bool:
        """
        Prints the output into a text file so the user can save potential fit ideas

        filename: the file that will be created ("saved_fits" -> "saved_fits.txt")

        NOTE: If you select a filename that is already suggested, it may be overwritten
        """
        pass


def main() -> None:
    db = Database()

    db.load_from_txt("db.txt")


if __name__ == "__main__":
    main()
