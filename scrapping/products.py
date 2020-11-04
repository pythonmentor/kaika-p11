"""Scrapp Products on off"""

from typing import List

import requests

from . import BASE_SEARCH_PARAMS, SEARCH_URL


def get_products(categories: List) -> List:
    """Get products from off based on a list of category.

    :param List categories: Categorie to filter results.

    :return List
    """
    products = list()
    params = BASE_SEARCH_PARAMS
    for category in categories:
        params["tag_0"] = category
        products += requests.get(SEARCH_URL, params).json()["products"]

    return products
