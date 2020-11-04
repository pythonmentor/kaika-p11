"""Integrations tests"""
from datetime import datetime

from catalog.models import Favorite
from search.views import ProductAutocomplete
from tests.test_pattern import TestPattern


class TestFavorite(TestPattern):
    """Test on Favorites"""

    query_set = ProductAutocomplete().get_queryset()

    def test_save_favorite(self):
        """Try to save a Favorite"""
        Favorite(
            substitute=self.query_set[0],
            substitued=self.query_set[1],
            user=self.user,
            date=datetime.now(),
        ).save()

        self.assertEqual(len(Favorite.objects.all().filter(user=self.user)), 1)

    def test_delete_favorite(self):
        """Try to delete a Favorite"""

        Favorite(
            substitute=self.query_set[0],
            substitued=self.query_set[1],
            user=self.user,
            date=datetime.now(),
        ).save()

        self.assertEqual(len(Favorite.objects.all().filter(user=self.user)), 1)

        Favorite.objects.get(substitute=self.query_set[0]).delete()

        self.assertEqual(len(Favorite.objects.all().filter(user=self.user)), 0)
