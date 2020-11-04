"""Test on catalog populate"""
import ast

from django.test import TestCase

from catalog import populate
from catalog.models import Category, Product
from scrapping import NUTELLA


class TestPopulate(TestCase):
    """Test populate database"""

    def test_populate_category(self):
        """Test populate categories"""
        categories = [
            {"name": "boissons", "url": "http://boissons.con"},
            {"name": "snacks", "url": "http://snack.com"},
        ]

        populate.populate_categories(categories)

        assert len(Category.objects.all()) == 2

    def test_populate_product(self):
        """Test populate db with product"""
        nutella = dict(NUTELLA)
        # Nutriments are modified to be as openfoodfacts
        nutella["nutriments"] = {
            "sugars_100g": 12.8,
            "fat_100g": 8.97,
            "saturated-fat_100g": 1.28,
            "salt_100g": 2.05,
        }
        populate.populate_product([nutella])

        assert Product.objects.get(brands="Ferrero").product_name_fr == "Nutella"

        # Test that only the 100g attributes are exported to db
        for nutriment in ast.literal_eval(
            Product.objects.get(brands="Ferrero").nutriments
        ):
            for key in nutriment:
                assert key.find("100g") != -1
