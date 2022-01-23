# Forward declarations for type hinting
from __future__ import annotations
import enum
import copy


class Type(enum.Enum):
    """
    Starts with these five, but would probably need to change
    once additional layers are added

    Eventually accessories would need to be added
    """

    # hat = 0
    # top = 1
    # outerwear = 2
    # pants = 3
    # shoes = 4
    top = 0
    pants = 1
    shoes = 2


class ClothingItem:

    def __init__(self, item_name: str, colors: str, brand: str, weather: str,
                 item_type: str):
        """
        :param item_name: name of piece
        :param colors: primary/secondary
        :param brand: up to two (if collab)
        :param weather: up to two (warm,cold)
        :param item_type: Type of clothing (top, outerwear, pants, shoes)

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
        elif item_type == "PANTS":
            self.item_type = Type.pants
        elif item_type == "SHOES":
            self.item_type = Type.shoes

    def __hash__(self) -> int:
        return hash(self.item_name)

    # Prints out the item with a short description of its attributes
    def __str__(self) -> str:
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

        s += "\nType: " + str(self.item_type.name) + "\n"

        return s

    # Comparison checking for each attribute
    def same_for(self, other: ClothingItem, check_for: str) -> bool:
        """
        Checks if the attributes match

        Ex for brand:
        [Stussy, Nike], [Nike] -> False
        [Stussy, Nike], [Stussy, Rick Owen] -> False
        [Stussy, Nike], [Stussy, Nike] -> True
        [Nike], [Nike] -> True

        :param self: self object
        :param other: other clothing item
        :param check_for: what to check for

        :return: whether the items are the same or not
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
                    if self_arr[0] == other_arr[0] and self_arr[
                            1] == other_arr[1]:
                        return True
                else:
                    if self_arr[0] == other_arr[0] and self_arr[
                            1] == other_arr[1]:
                        return True
                    elif self_arr[0] == other_arr[1] and self_arr[
                            1] == other_arr[0]:
                        return True
                return False

    def __eq__(self, other: ClothingItem) -> bool:
        """
        Compares if two items are the same, this will be important later when the graph algorithm is used
        as it will help make sure the same node is not visited twice
        Might also be used to check in an item is added twice

        NOTE: Two items in different colors are recognized as two different items

        :param self: self object
        :param other: other Clothing object to compare with

        :return: whether the items are equal or not based on what to check for
        """
        check_for_array = ["brand", "color", "weather", "type"]

        for check_for in check_for_array:
            if self.same_for(other, check_for) == False:
                return False

        return True


class RuleType(enum.Enum):

    color = 0
    brand = 1
    weather = 2
    undefined = -1


class Node:

    def __init__(self, value: str, weight: int = 0, end: bool = False):
        """
        :param value: the value of the trie that links to other nodes
        :param weight: the weight of the value, positive indicates good,
        negative discourages the algorithm from picking

        attributes of Node:
        value: color/brand, depending on the ruleset. Looking for matches
        from the generated outfits
        weight: frequency of usage, how the combo is set in the ruleset
        end: a boolean that represents end of rule
        children: connections to other nodes
        NOTE: there can be more connected nodes even if there is an end
        """
        self.value = value
        self.weight = weight
        self.end = end
        self.children = {}

    def __eq__(self, other) -> bool:
        return (self.weight == other.weight and self.value == other.value
                and self.end == other.end and self.children == other.children)

    def __str__(self) -> str:
        res = "Value: %s Weight: %s" % (self.value, self.weight)
        return res


class Rule:

    def __init__(self, type: str):
        """
        :param type: the type of rule (color, brand)

        attributes of Rule
        type: type of rule as an enum
        start: where all the nodes live
        """
        if type == "COLOR":
            self.type = RuleType.color
        elif type == "BRAND":
            self.type = RuleType.brand
        elif type == "WEATHER":
            self.type = RuleType.weather
        else:
            self.type = RuleType.undefined

        self.start = Node("", 0, False)

    def __eq__(self, other) -> bool:
        return self.type == other.type

    def __str__(self) -> str:
        res = "Rule: %s \nStart Node: (%s)" % (self.type, self.start)
        return res

    def add_combo(self, combo: str, weight: int = 0):
        """
        :param combo: combination to be parsed and added
        :param weight: optional weight, at the end for the graph
        to determine results

        "Stussy/Nike" -> ["Stussy", "Nike"] -> Inserted as
        Node(Stussy) linked to Node(Nike) -> end
        """

        combo_array = combo.split(",")

        curr: Node = self.start
        i: int = 0
        while i < len(combo_array):
            if combo_array[i] not in curr.children:
                curr.children[combo_array[i]] = Node(combo_array[i])
            curr = curr.children[combo_array[i]]
            i += 1

        curr.weight = weight
        curr.end = True

    def combo_exists(self, combo: list[str]) -> tuple[bool, int]:
        """
        :param combo: given a list of string (brand or color)

        determines whether it exists or not in the trie structure
        :return: true / false (if found), score of combination
        """
        i: int = 0
        score: int = 0
        curr: Node = self.start
        while i < len(combo) and curr:
            if combo[i] not in curr.children:
                return (False, 0)
            curr = curr.children[combo[i]]
            score += curr.weight
            i += 1

        return ((curr.end and i == len(combo)), score)

    def score_fit(self, fit: list[ClothingItem]) -> int:
        """
        :param fit: the outfit generated

        :return: the score that the fit generates - the higher the better
        """
        fit_str = []
        score = 0

        if self.type == RuleType.brand:
            for item in fit:
                fit_str.append(item.brand[0])
        elif self.type == RuleType.color:
            for item in fit:
                fit_str.append(item.colors[0])
        else:
            pass

        for i in range(len(fit_str)):
            slice = fit_str[i:]
            exists, curr_score = self.combo_exists(slice)
            if exists:
                score += curr_score

        return score


class Graph:

    def __init__(self):
        """
        Graph structure consisting of nodes

        attributes of Graph:
        all_items: all the items stored in the list
        adj_list: all the connections drawn by pairs
        """
        # This needs to be changed back to 5 when hats and outerwear is included again
        self.all_items: list[list[ClothingItem]] = [[], [], []]

        self.adj_list: dict[ClothingItem, list[ClothingItem]] = {}

    def add_collection(self, collection: list[ClothingItem]) -> bool:
        """
        Adds a collection to the already existing graph.

        :return: whether it was successfully added or not
        """
        if len(collection) == 0:
            return False

        # index of the category
        index: int = collection[0].item_type.value

        # simply overload the category with the current collection
        self.all_items[index] = collection

        return True

    def add_all(self, collections: dict[str, list[ClothingItem]]) -> bool:
        # categories = ["HAT", "OUTERWEAR", "TOP", "PANTS", "SHOES"]
        categories = ["TOP", "PANTS", "SHOES"]

        for category in categories:
            res = self.add_collection(collections[category])
            if res == False:
                return False

        return True

    def add_connections(self) -> bool:
        """
        Given an already filled graph, connections are drawn between
        each layer. This function will not continue if one category is
        completely empty

        :return: whether the connections were added successfully
        """
        for category in self.all_items:
            if len(category) == 0:
                return False

        for i in range(len(self.all_items)):
            category = self.all_items[i]
            # above = i - 1 if i - 1 >= 0 else -1
            below = i + 1 if i + 1 < len(self.all_items) else -1

            to_connect: list[ClothingItem] = []

            # TODO: Clean this up (what am I even doing here)
            # Ideally want this to be an actual graph -> right now shaped like a trie

            # if above == -1:
            #     to_connect = self.all_items[below]
            # elif below == -1:
            #     to_connect = self.all_items[above]
            # else:
            #     to_connect = self.all_items[above] + self.all_items[below]

            if below == -1:
                pass
            else:
                to_connect = self.all_items[below]

            # For each item in the category - connect to the pieces
            # below and above
            for item in category:
                self.adj_list[item] = to_connect

        return True

    def generate_fits(self, rule_set: dict[str,
                                           Rule]) -> list[list[ClothingItem]]:
        res: list[list[ClothingItem]] = []

        for item in self.all_items[0]:
            self.dfs([], res, item)

        return res

    def dfs(
        self,
        curr_fit: list[ClothingItem],
        res: list[list[ClothingItem]],
        item: ClothingItem,
    ):
        curr_fit.append(item)

        # Last item in the outfit
        if item.item_type == Type.shoes:
            if curr_fit not in res:
                # Makes a deep copy
                res.append(copy.deepcopy(curr_fit))
        else:
            # For all items connected to the current:
            for connected_item in self.adj_list[item]:
                self.dfs(curr_fit, res, connected_item)

        curr_fit.pop()
