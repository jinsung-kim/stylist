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
            s += "\nFor both weathers"
        else:
            s += "\nFor Weather Condition: " + self.weather[0]

        if len(self.brand) > 1:
            s += "\nBrand(s): " + self.brand[0] + "/" + self.brand[1]
        else:
            s += "\nBrand: " + self.brand[0]

        s += "\nType: " + str(self.item_type.name)

        return s

    def __eq__(self, other):
        """
        Compares if two items are the same, this will be important later when the graph algorithm is used
        as it will help make sure the same node is not visited twice
        Might also be used to check in an item is added twice
        """
        pass
