"""Selenium based tests"""
from datetime import datetime
from uuid import uuid4

from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from pytest import raises
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

from catalog.models import Favorite, Product
from scrapping import NUTELLA


class SeleniumBasedTestCase(LiveServerTestCase):
    """Test based on Selenium."""

    def setUp(self) -> None:
        """Set up tets environment"""
        caps = DesiredCapabilities().FIREFOX.copy()
        caps["marionette"] = True

        self.user = User.objects.create_user(username="test1", password="test1@1234")

        self.driver = webdriver.Firefox(
            capabilities=caps,
            firefox_binary="/Applications/Applications/Firefox.app/Contents"
            "/MacOS/firefox-bin",
        )

        self.driver.implicitly_wait(10)

        self.product_1 = Product(
            id=uuid4(),
            product_name_fr="produit bon",
            nutrition_grade_fr="A",
            categories_tags=["Pâte à tartiner"],
        )
        self.product_2 = Product(**NUTELLA)

        self.product_1.save()
        self.product_2.save()

    def tearDown(self) -> None:
        """Method to call at teardown."""
        self.driver.close()

    def test_save_favorite(self):
        """An authenticated user should be able to save favorites."""
        self.driver.get(self.live_server_url + "/accounts/login")

        # login
        self.driver.find_element_by_id("id_login").send_keys(self.user.username)
        self.driver.find_element_by_id("id_password").send_keys("test1@1234")
        self.driver.find_element_by_id("login-button").click()

        # go to home page
        self.driver.find_element_by_id("pur-beurre").click()

        self.assertEqual(self.driver.title, "Pur beurre")
        # select search form
        self.driver.find_element_by_class_name("select2-selection").click()

        # search for a product
        self.driver.find_element_by_class_name("select2-search__field").send_keys(
            Keys.ENTER
        )

        # click on "chercher" button
        self.driver.find_element_by_id("search-button").click()

        self.assertEqual(self.driver.title, "Résultats")

        self.assertEqual(len(Favorite.objects.all().filter(user=self.user)), 0)

        # save first product
        self.driver.find_element_by_xpath("//figure/form/button").click()

        # go to favorites
        self.driver.find_element_by_id("carrot-logo").click()

        self.assertEqual(len(Favorite.objects.all().filter(user=self.user)), 1)

        self.assertEqual(self.driver.title, "Favoris")

    def test_delete_favorite(self):
        """An authenticated user should be able to delete favorites."""
        Favorite(
            substitute=self.product_1,
            substitued=self.product_2,
            user=self.user,
            date=datetime.now(),
        ).save()

        self.driver.get(self.live_server_url + "/accounts/login")

        # login
        self.driver.find_element_by_id("id_login").send_keys(self.user.username)
        self.driver.find_element_by_id("id_password").send_keys("test1@1234")
        self.driver.find_element_by_id("login-button").click()

        # go to favorites
        self.driver.find_element_by_id("carrot-logo").click()

        self.assertEqual(self.driver.title, "Favoris")

        self.assertEqual(len(Favorite.objects.all().filter(user=self.user)), 1)

        # delete first product
        self.driver.find_element_by_xpath("//figure/form/button").click()

        self.assertEqual(len(Favorite.objects.all().filter(user=self.user)), 0)

    def test_fail_access_favorite(self):
        """An user non authenticated shouldn't access to favorites."""
        self.driver.get(self.live_server_url)

        # cannot find favorites
        with raises(NoSuchElementException):
            self.driver.find_element_by_id("navbar_favorites")

    def test_fail_access_user_account(self):
        """An user non authenticated shouldn't access to user_account."""
        self.driver.get(self.live_server_url)

        # click on user accounts
        self.driver.find_element_by_id("navbar_account").click()

        self.assertEqual(self.driver.title, "Login")
