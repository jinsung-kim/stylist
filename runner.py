from __future__ import annotations
import sys
import os
import requests
from decouple import config

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.models import ClothingItem, Rule, Graph
from helpers.helpers import get_in_quote, get_piece_score
from helpers.outfit_formatter import format_outfit

API_KEY: str = config("WEATHER_KEY")


class Database:
    # Where most of the program is run
    def __init__(self) -> None:
        """
        clothing_items: dictionary{Clothing}
        rule_set: dictionary{str, Rules}
        favorites: dictionary{str, int}
        """
        self.clothing_items: dict[str, list[ClothingItem]] = {}
        self.rule_set: dict[str, Rule] = {}
        self.favorites: dict[str, int] = {}

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
        adding_clothing = True

        # Add each item in its intended category
        for line in lines:
            line = line.strip("\n")
            if line in target:
                curr = line
                self.clothing_items[curr] = []
            elif len(line) == 0:
                pass
            elif line == "END" or line == "FAVORITES":
                adding_clothing = False
            elif len(line) > 0 and not adding_clothing:
                item, score = get_piece_score(line)
                self.favorites[item] = score
            elif len(line) > 0 and adding_clothing:
                re, ind = get_in_quote(line)
                rest_of_line = line[ind + 1:]
                attributes = rest_of_line.split(" ")
                colors = attributes[0]
                brands = attributes[1]
                weather = attributes[2]
                self.clothing_items[curr].append(
                    ClothingItem(re, colors, brands, weather, curr))

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
        TODO:
        Prints the output into a text file so the user can save potential fit ideas
        NOTE: If you select a filename already taken in the directory, it may be overwritten

        :param filename: the file that will be created ("saved_fits" -> "saved_fits.txt")
        :return: whether the exporting was successful or not
        """
        pass

    def filter_outfits(
        self,
        outfits: list[list[ClothingItem]],
        top_k: int,
    ) -> list[list[ClothingItem]]:
        """
        Filters out by outfits by the rules determined by ruleset.txt

        :param outfits: the outfits generated in the graph structure
        :param top_k: the top 'n' fits calculated by the rules

        :return: top 'n' outfits
        """
        if (len(outfits) < top_k):
            return []

        check_for = ["COLOR", "BRAND"]

        scored: list[tuple[int, ClothingItem]] = []

        for fit in outfits:
            final_score = 0
            # Iterate through to check color + brand rulesets
            for check in check_for:
                score = self.rule_set[check].score_fit(fit)
                final_score += score
            # Find favorite items
            for item in fit:
                if item.item_name in self.favorites:
                    final_score += self.favorites[item.item_name]

            scored.append((final_score, fit))

        res: list[list[ClothingItem]] = []

        # Sort by the score in the tuple
        scored.sort(key=lambda y: y[0])
        scored.reverse()

        for i in range(top_k):
            fit: list[ClothingItem] = scored[i][1]
            if fit not in res:
                res.append(fit)

        return res


class Interface:

    def __init__(self) -> None:
        """
        location: str - where the user is located
        tempature_f: float - temperature in Fahrenheit
        db: Database - where the items are loaded and live
        g: Graph - the connections of the items
        fits: list[list[ClothingItem]] - all of the generated outfits
        """
        self.location: str = ""
        self.temperature_f: float = -1
        self.db: Database = Database()
        self.g: Graph = Graph()
        self.fits: list[list[ClothingItem]] = []

        # Load in
        self.db.load_from_txt()
        self.db.load_ruleset_from_txt()

        self.g.add_all(self.db.clothing_items)
        self.g.add_connections()

        self.fits = self.g.generate_fits(self.db.rule_set)

        self.print_intro()

    def print_intro(self):
        print("Your wardrobe has been loaded into the program.")

    def set_location(self):
        """
        Sets the user location based on input
        """
        loc: str = input(
            "Enter your location (address, city, lat/long, whatever you want): "
        )
        self.location = loc

    def get_weather(self):
        """
        Retrieves the weather conditions given the location
        Must be done after the location is set
        """
        WEATHER_URL: str = "http://api.weatherapi.com/v1/current.json?key=" + API_KEY + "&q=" + self.location + "&aqi=no"

        r = requests.get(WEATHER_URL)

        if (r.status_code == 200):
            self.temperature_f = float(r.json()["current"]["temp_f"])
        else:
            print(
                "The weather could not be retrieved. Please try again later.")

    def get_fits(self):
        """
        Gets the outfits - Goes from best to worst
        Asks the user how many they want
        """
        number_requested: int = int(
            input("How many would you like to retrieve for the day? "))

        filtered_res: list[list[ClothingItem]] = self.db.filter_outfits(
            self.fits, number_requested)

        for fit in filtered_res:
            print(format_outfit(fit))

        # Get more if the user is not satisfied with any of them


def main() -> None:
    """
    Where every object lives and is executed
    """
    i: Interface = Interface()
    i.set_location()
    i.get_weather()
    # i.get_fits()


if __name__ == "__main__":
    main()
