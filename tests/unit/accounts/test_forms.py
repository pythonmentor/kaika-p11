"""Test on account module's form"""
from accounts.forms import LoginForm, SubscribeForm
from tests.test_pattern import TestPattern


class TestForms(TestPattern):
    """Test on accounts forms"""

    def test_login_form(self):
        """Test login form"""
        form = LoginForm(data={"login": "test_user", "password": "test_password"})

        assert form.is_valid()

    def test_subscribe_form(self):
        """Test subscribe form"""
        form = SubscribeForm(
            data={
                "login": "test_login",
                "last_name": "test_last_name",
                "first_name": "test_first_name",
                "email": "test@mail.com",
                "password": "test_password",
                "confirm_password": "test_password",
            }
        )

        assert form.is_valid()
