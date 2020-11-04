"""Commands for catalog"""
import ast
from datetime import datetime
from typing import List, Tuple
from uuid import UUID

from django.contrib.auth.models import User

from catalog.models import Favorite, Product


def get_better_products(base_product: Product) -> Tuple[List[Product], Product]:
    """
    Get a list of products with better nutriscore from a base product.

    :param Product base_product: product to compare
    :return: List[Product] list of better products
    """
    base_product = Product.objects.get(id=base_product)
    categories: List = ast.literal_eval(base_product.categories_tags)
    nutrition_grade: str = base_product.nutrition_grade_fr
    products: List[Product] = []

    # Find products with better nutrition grade for each category
    for category in categories:
        # pylint: disable=expression-not-assigned
        [
            products.append(product)
            for product in Product.objects.filter(
                categories_tags__contains=category,
                nutrition_grade_fr__cn=nutrition_grade,
            )
        ]

    products.sort(key=lambda x: x.nutrition_grade_fr)

    return products, base_product


def get_favorite_info(
    base_product: UUID, substitute_product: UUID, user: User
) -> Tuple[Favorite, Product]:
    """
    Get information on favorite.

    :param UUID base_product: product which needed to be replaced
    :param UUID substitute_product: replacement product
    :param User user: user who make the compare
    :return: Tuple[Favorite, Product]
    """

    base = Product.objects.get(id=base_product)
    substitute = Product.objects.get(id=substitute_product)

    return (
        Favorite(
            substitued=base, substitute=substitute, date=datetime.now(), user=user
        ),
        substitute,
    )


def get_delete_info(product_id: UUID, user: User) -> Tuple[Favorite, str]:
    """
    Get information to delete product in favorite.

    :param UUID product_id: product to delete
    :param User user: user owning the Favorite
    :return: Tuple[Favorite, product_name]
    """
    to_delete = Favorite.objects.get(substitute=product_id, user=user)

    product_name = Product.objects.get(id=product_id).product_name_fr

    return to_delete, product_name
