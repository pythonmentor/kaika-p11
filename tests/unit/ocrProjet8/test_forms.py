"""Test on ocrProjet8 forms"""
from ocrProjet8.forms import ContactForm
from tests.test_pattern import TestPattern


class TestForms(TestPattern):
    """Test ocrProjet8 forms"""

    def test_contact_form(self):
        """Test ContactForm"""
        form = ContactForm(
            data={
                "subject": "sujet",
                "message": "Message de test",
                "email": "test@test.com",
            }
        )

        assert form.is_valid()
