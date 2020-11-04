"""Test pattern for other test"""
from uuid import uuid4

from django.test import TestCase

from catalog.models import Product
from accounts.models import CustomUser
from scrapping import NUTELLA


class TestPattern(TestCase):
    """Global set up"""

    def setUp(self) -> None:
        """Environment for tests"""
        self.user = CustomUser.objects.create_user(username="test1", password="test1@1234")

        self.client.login(username="test1", password="test1@1234")

        self.product_1 = Product(
            id=uuid4(),
            product_name_fr="produit bon",
            nutrition_grade_fr="A",
            categories_tags=["Pâte à tartiner"],
        )
        self.product_2 = Product(**NUTELLA)

        self.product_1.save()
        self.product_2.save()
