"""Test on catalog commands"""
from io import StringIO

from django.core.management import call_command

from tests.test_pattern import TestPattern


class DjangoCommandTest(TestPattern):
    """Test django commands."""

    def test_empty_database(self):
        """Verify if database correctly emptied"""
        out = StringIO()
        call_command("empty_database", True, stdout=out)
        self.assertIn("Database correctly emptied", out.getvalue())
