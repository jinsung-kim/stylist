from __future__ import annotations


def get_in_quote(item: str) -> tuple[str, int]:
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


def get_piece_score(item: str) -> tuple[str, int]:
    """
    Used to look through favorite pieces and provide appropriate score
    :param item: piece name

    :return: tuple of string and price int
    """
    res, ind = get_in_quote(item)
    price = int(item[ind:])

    return res, price
