# Forward declarations for type hinting
from __future__ import annotations
import enum


class Type(enum.Enum):
    """
    Starts with these five, but would probably need to change
    once additional layers are added

    Eventually accessories would need to be added
    """

    hat = 1
    top = 2
    outerwear = 3
    pants = 4
    shoes = 5


class ClothingItem:
    def __init__(
        self, item_name: str, colors: str, brand: str, weather: str, item_type: str
    ) -> None:
        """
        item_name: name of piece
        colors: primary/secondary
        brand: up to two (if collab)
        weather: up to two (warm,cold)
        item_type: Type of clothing (top, outerwear, pants, shoes)

        attributes of ClothingItem
        item_name: name of piece
        colors: [str]
        brand: [str]
        weather: [str]
        item_type: Type (enum)
        """
        self.item_name = item_name

        colors_split = colors.split("/")
        if len(colors_split) > 1:
            self.colors = [colors_split[0], colors_split[1]]
        else:
            self.colors = [colors_split[0]]

        brand_split = brand.split(",")
        if len(brand_split) > 1:
            self.brand = [brand_split[0], brand_split[1]]
        else:
            self.brand = [brand_split[0]]

        weather_split = weather.split(",")
        if len(weather_split) > 1:
            self.weather = [weather_split[0], weather_split[1]]
        else:
            self.weather = [weather_split[0]]

        if item_type == "HAT":
            self.item_type = Type.hat
        elif item_type == "OUTERWEAR":
            self.item_type = Type.outerwear
        elif item_type == "TOP":
            self.item_type = Type.top
        elif item_type == "PANT":
            self.item_type = Type.pants
        elif item_type == "SHOES":
            self.item_type = Type.shoes

    # Prints out the item with a short description of its attributes
    def __str__(self):
        s = self.item_name + " \nPrimary Color: " + self.colors[0]

        if len(self.colors) > 1:
            s += "\nSecondary Color: " + self.colors[1]

        if len(self.weather) > 1:
            s += "\nFor most weather"
        else:
            s += "\nFor " + self.weather[0] + " temperatures"

        if len(self.brand) > 1:
            s += "\nBrand(s): " + self.brand[0] + "/" + self.brand[1]
        else:
            s += "\nBrand: " + self.brand[0]

        s += "\nType: " + str(self.item_type.name)

        return s

    # Comparison checking for each attribute

    def same_for(self, other: ClothingItem, check_for: str):
        """
        Checks if the attributes match

        Ex for brand:
        [Stussy, Nike], [Nike] -> False
        [Stussy, Nike], [Stussy, Rick Owen] -> False
        [Stussy, Nike], [Stussy, Nike] -> True
        [Nike], [Nike] -> True
        """
        self_arr = []
        other_arr = []
        if check_for == "brand":
            self_arr = self.brand
            other_arr = other.brand
        elif check_for == "color":
            self_arr = self.colors
            other_arr = other.colors
        elif check_for == "weather":
            self_arr = self.weather
            other_arr = other.weather
        elif check_for == "type":
            return self.item_type == other.item_type
        else:  # Checking for something that does not exist
            return False

        if len(self_arr) != len(other_arr):
            return False
        else:
            # Both solo items
            if len(self_arr) == 1:
                return self_arr[0] == other_arr[0]
            # Both collab items
            else:
                # Color is unique because we care about the order
                # The primary color of the outfit always goes first
                if check_for == "color":
                    if self_arr[0] == other_arr[0] and self_arr[1] == other_arr[1]:
                        return True
                else:
                    if self_arr[0] == other_arr[0] and self_arr[1] == other_arr[1]:
                        return True
                    elif self_arr[0] == other_arr[1] and self_arr[1] == other_arr[0]:
                        return True
                return False

    def __eq__(self, other: ClothingItem):
        """
        Compares if two items are the same, this will be important later when the graph algorithm is used
        as it will help make sure the same node is not visited twice
        Might also be used to check in an item is added twice

        NOTE: Two items in different colors are recognized as two different items
        """
        check_for_array = ["brand", "color", "weather", "type"]

        for check_for in check_for_array:
            if self.same_for(other, check_for) == False:
                return False

        return True


class Graph:
    def __init__(self):
        pass
