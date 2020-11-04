"""Command to populate the default database"""
from django.core.management.base import BaseCommand, CommandError

from catalog.models import Category
from catalog.populate import populate_categories, populate_product
from scrapping.categories import get_categories
from scrapping.products import get_products


class Command(BaseCommand):
    """Command populate_database"""

    help = "Populates the database"

    def add_arguments(self, parser):
        """Add argument populate"""
        parser.add_argument("populate", nargs="+", type=bool)

    def handle(self, *args, **options):  # pylint: disable=unused-argument
        """Action when using command"""
        if options["populate"]:

            try:
                categories = get_categories()
            except Exception as error:
                raise CommandError(
                    f"Error while scrapping categories- {error}"
                ) from error

            try:
                populate_categories(categories)
            except Exception as error:
                raise CommandError(
                    f"Error while populating categories- {error}"
                ) from error

            try:
                products = get_products(
                    [category.name for category in Category.objects.all()]
                )
            except Exception as error:
                raise CommandError(
                    f"Error while scrapping products - {error}"
                ) from error

            try:
                populate_product(products)
            except Exception as error:
                raise CommandError(
                    f"Error while populating products - {error}"
                ) from error
