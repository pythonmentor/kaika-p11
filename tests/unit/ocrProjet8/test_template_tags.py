"""Test on ocrProjet8 template tags"""
from catalog import NUTRISCORE
from ocrProjet8.templatetags.dict_template import (
    get_color_for_key,
    get_nutriment,
    get_value_for_key,
)
from ocrProjet8.templatetags.navbar_search import navbar_search
from tests.test_pattern import TestPattern


class TestTemplateTags(TestPattern):
    """Test ocrProjet8's template tags"""

    def test_navbar_search(self):
        """Test form correctly created"""
        navbar_form = navbar_search(None, None)

        assert navbar_form.form.fields["produit"]

        self.assertEqual(navbar_form.form.is_valid(), False)

    def test_get_nutriment(self):
        """Test nutriments parse and return"""
        nutriments_1, category_1 = {"saturated-fat_100g": 10}, "meats"

        nutriments_2, category_2 = {"fat_100g": 15}, "bread"

        nutriments_3, category_3 = {"sugars_100g": 12}, "beverage"

        nutriments_4, category_4 = {"salt_100g": 0.2}, "fish"

        self.assertIn("🔴", get_nutriment(nutriments_1, category_1))

        self.assertIn("🟠", get_nutriment(nutriments_2, category_2))

        # Even if sugars are under limits, it souldn't pass because it's beverage (x2)
        self.assertIn("🔴", get_nutriment(nutriments_3, category_3))

        self.assertIn("🟢", get_nutriment(nutriments_4, category_4))

    def test_get_value_for_key(self):
        """Test value correctly returned"""
        self.assertEqual(get_value_for_key(NUTRISCORE, "a"), "Ⓐ")

    def test_get_color_for_key(self):
        """Test color correctly returned"""
        self.assertEqual(get_color_for_key(NUTRISCORE, "A"), "#328F00")
