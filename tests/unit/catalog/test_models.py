"""Test on catalog's models"""
import uuid

from accounts.models import CustomUser
from catalog import populate
from catalog.models import Category, Favorite, Product
from scrapping import ID_PRODUCT, NUTELLA
from tests.test_pattern import TestPattern


class TestModels(TestPattern):
    """Tests on models."""

    def setUp(self) -> None:
        Product.objects.all().delete()

    def test_add_category_db(self):
        """Test adding category to catalog."""
        id_category = uuid.uuid4()
        category = Category(
            id_category=id_category,
            name="Charcuteries",
            url="https://fr.openfoodfacts.org/categorie/charcuteries",
        )

        # save category to db
        category.save()

        # verify Category saved on db
        assert len(Category.objects.all()) == 1

        # retrieve category name in the db
        assert Category.objects.get(id_category=id_category).name == "Charcuteries"

    def test_add_product_db(self):
        """Test adding product to db."""
        product = Product(**NUTELLA)

        # save product on db
        product.save()

        # verify Product saved on db
        assert len(Product.objects.all()) == 1

        # retrieve product name in the db
        assert Product.objects.get(id=ID_PRODUCT).product_name_fr == "Nutella"

    def test_add_favorite_db(self):
        """Add a new favorite to db"""
        product_1 = Product(product_name_fr="produit bon", nutrition_grade_fr="A")
        product_2 = Product(**NUTELLA)

        product_1.save()
        product_2.save()

        user = CustomUser(username="Utilisateur")
        user.save()

        populate.save_favorite(product_1, product_2, user)

        assert len(Favorite.objects.all()) == 1
