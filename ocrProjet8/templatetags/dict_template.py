"""Filters for dict"""
from typing import Dict

from django.template.defaulttags import register
from django.utils.safestring import mark_safe

from catalog import NUTRIMENTS


@register.filter(name="get_nutriment")
def get_nutriment(nutriment: Dict, categories: str) -> str:
    """
    Get a nutriment color and name for a given nutriment.

    :param nutriment: nutriment to parse
    :param categories: category of the product
    :return: str
    """
    # pylint: disable=unnecessary-comprehension
    key: str = [name for name in nutriment.keys()][0]

    nutriment_value = nutriment[key]

    # If product is beverage, limits are divided by two
    if "beverage" in categories or "boisson" in categories:
        nutriment_value = nutriment_value * 2

    if nutriment_value < NUTRIMENTS[key[:-5]]["value"]["low"]:
        color, quantity = "🟢  ", "faible quantité"
    elif nutriment_value > NUTRIMENTS[key[:-5]]["value"]["moderate"]:
        color, quantity = "🔴  ", "quantité élevée"
    else:
        color, quantity = "🟠  ", "quantité modérée"

    nutriment = f"{color} {nutriment[key]} g \
     <strong>{NUTRIMENTS[key[:-5]]['traduction']}</strong> en {quantity}"

    return mark_safe(nutriment)


@register.filter(name="get_value_for_key")
def get_value_for_key(dictionary: Dict, key: str) -> str:
    """
    Get a key's value in template

    :param dictionary: Dictionnary containing the table of correspondence
    :param key: key to look for
    :return: str
    """
    return dictionary.get(key.upper())[0]


@register.filter(name="get_color_for_key")
def get_color_for_key(dictionary: Dict, key: str) -> str:
    """
    Get a color for a given nutriscore.

    :param dictionary: Dictionnary containing the table of correspondence
    :param key: Key to look for
    :return: str
    """
    return dictionary.get(key.upper())[1]
