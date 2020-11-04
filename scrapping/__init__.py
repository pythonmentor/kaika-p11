"""Init from scrapping"""
from uuid import uuid4

ID_PRODUCT = uuid4()
# Find products for this categories
GIVEN_CATEGORIES = ["Fromages", "Snacks", "Boissons", "Charcuteries", "Desserts"]
OPENFOODFACT_URL = "https://fr.openfoodfacts.org/"
CATEGORIES_JSON = OPENFOODFACT_URL + "categories"  # url of categories
SEARCH_URL = OPENFOODFACT_URL + "cgi/search.pl"
BASE_SEARCH_PARAMS = {
    "action": "process",
    "tagtype_0": "categories",
    "tagcontains_0": "contains",
    "limit": 5000,
    "tag_0": "test",
    "page_size": 1000,
    "sort_by": "unique_scans_n",
    "json": 1,
}
NUTELLA = {
    "id": ID_PRODUCT,
    "brands": "Ferrero",
    "categories_tags": ["Pâte à tartiner"],
    "nutrition_grade_fr": "E",
    "nutriments": [
        {"sugars_100g": 12.8},
        {"fat_100g": 8.97},
        {"saturated-fat_100g": 1.28},
        {"salt_100g": 2.05},
    ],
    "product_name_fr": "Nutella",
    "image_url": "http://nutella-images.fr",
    "url": "http://off-nutella-link.fr",
}
