"""Scrapp Categories on Openfoodfact"""

from typing import List

import requests

from . import CATEGORIES_JSON, GIVEN_CATEGORIES


def get_categories() -> List:
    """Get categories from OpenFoodFact."""
    return [
        category
        for category in requests.get(f"{CATEGORIES_JSON}", params={"json": 1}).json()[
            "tags"
        ]
        if category["name"] in set(GIVEN_CATEGORIES)
    ]
