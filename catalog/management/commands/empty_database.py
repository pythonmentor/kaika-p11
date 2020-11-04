"""Command to empty the default database"""
from django.core.management.base import BaseCommand, CommandError

from catalog.models import Category, Favorite, Product


class Command(BaseCommand):
    """Command empty_database"""

    help = "Empty the database"

    def add_arguments(self, parser):
        """Add an argument"""
        parser.add_argument("emptydb", nargs="+", type=bool)

    def handle(self, *args, **options):  # pylint: disable=unused-argument
        """Action to do when using command"""
        if options["emptydb"]:
            try:
                Category.objects.all().delete()
                Product.objects.all().delete()
                Favorite.objects.all().delete()
            except Exception as error:
                raise CommandError(
                    f"Error while emptying database - {error}"
                ) from error

            self.stdout.write("Database correctly emptied", ending="")
