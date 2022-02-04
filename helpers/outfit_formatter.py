from __future__ import annotations
from models.models import ClothingItem


def format_outfit(fit: list[ClothingItem]) -> str:
    """
    TODO: Add reasons why the fit was selected - potentially score as well
    Format the outfit into a readable string
    :param fit: outfit generated

    :return: string of formatted
    """
    res: str = ""

    for item in fit:
        res += item.item_name + " "

    return res


# Evaluate whether item is weather appropriate
def weather_appropriate(item: ClothingItem, weather: float) -> bool:
    """
    :param item: The item we are checking for
    :param weather: The current weather as a float

    NOTE: The threshold is currently set to 45 degrees Fahrenheit

    :return: boolean whether acceptable or not
    """
    if (len(item.weather) == 2):
        return True
    else:
        item_weather: str = item.weather[0]
        if (weather <= 45 and item_weather == "Cold"):
            return True
        elif (weather >= 45 and item_weather == "Warm"):
            return True
        else:
            return False