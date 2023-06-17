import time

from django.test import TestCase
from selenium import webdriver


class FunctionalTestCase(TestCase):
    """
    FunctionalTest describes what a user can or wants to do
    """
    def setUp(self) -> None:
        """
        call before test starts
        """
        self.browser = webdriver.Chrome()

    def test_this_is_homepage(self):
        """
        This test will check that the homepage allow user to enter some hash
        """
        self.browser.get('http://localhost:8000')

        time.sleep(5)  # Let the user actually see something!

        self.assertIn('Enter hash here:', self.browser.page_source)

        time.sleep(5)  # Let the user actually see something!

    def tearDown(self) -> None:
        """
        call after test finish
        """
        self.browser.quit()
