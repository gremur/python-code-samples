# -*- coding: utf-8 -*-

import hashlib
import time
from datetime import datetime
from typing import Union
import pandas as pd


def current_datetime() -> str:
    """
    Return current date and time in '2021/01/22 11:58:06' format
    Returns:
        text string with current date and time
    """
    return datetime.now().strftime("%Y/%m/%d %H:%M:%S")


def add_datetime(file_name: str) -> str:
    """
    Add current datetime to provided file name
    Args:
        file_name: file name text string like 'file.json'
    Returns:
        file name with datetime like ''file_20211201=132501.json'
    """
    name, extension = file_name.split('.')
    return f"{str(name)}_{time.strftime('%Y%m%d-%H%M%S')}.{extension}"


def to_hash(txt: str) -> Union[str, None]:
    """
    Convert txt to hash string
    Args:
        txt: text string
    Returns:
        hash string
    Note:
        if urls are unique they can be used as unique ids
    """
    if not pd.isnull(txt):
        hash_object = hashlib.sha256(f'{txt}'.encode())
        hash_str = hash_object.hexdigest()
        return hash_str
    else:
        return None


def flatten_list(lst: Union[list, tuple]) -> list:
    """
    Convert list of lists or tuples to one level list
    Args:
        lst: List of lists
    Returns:
        single level list
    """
    return [item for subitem in lst for item in subitem]


def deduplicate_list(lst: list) -> list:
    """
    Remove duplicated items from list
    Args:
        lst: list of items
    Returns:
        list with unique items
    """
    return list(set(lst))


def lowercase(txt_lst: Union[str, list]) -> Union[str, list]:
    """
    Converts string or list items to lowercase
    Args:
        txt_lst: text string of list
    Returns:
        text string of list items in lowercase format
    """
    if isinstance(txt_lst, list):
        return [lst_item.lower() for lst_item in txt_lst]
    elif isinstance(txt_lst, str):
        return txt_lst.lower()


def sort_list_by_items_length(lst: list, order: bool = True) -> list:
    """
    Sort list by length of items
    Args:
        lst: list of items
        order: set 'False' to sort list by ascending order 1-10 (default), set 'True' - for descending order 10-1
    Returns:
        sorted list
    """
    return sorted(lst, key=len, reverse=order)


def sort_list_by_alphabet(lst: list) -> list:
    """
    Sort list items by alphabetical order
    Args:
        lst: list of items
    Returns:
        sorted list
    """
    return sorted(lst)


def sort_dict_by_key_length(dct: dict) -> dict:
    """
    Sort dict items by key length
    Args:
        dct: dict
    Returns:
        sorted dict
    """
    sorted_dict = {}
    for k in sorted(dct, key=len, reverse=True):
        sorted_dict[k] = dct[k]
    return sorted_dict


def is_digit(token: any) -> bool:
    """
    Check if token is a digit (int, float)
    Args:
        token: any kind of token
    Returns:
        'True' if token is int or float type
        'False' if token is not int or not float type
    """
    if token.isdigit():
        return True
    else:
        try:
            float(token.replace(',', '.'))
            return True
        except ValueError:
            return False


def convert_to_unicode(txt: str) -> str:
    """
    Convert non latin chars including numbers and special chars to unicode codes, like "&" to "\u0026"
    Args:
        txt: text string
    Returns:
        text string with unicode codes
    """
    return str(txt.encode("unicode_escape"))
