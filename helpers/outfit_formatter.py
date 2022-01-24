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