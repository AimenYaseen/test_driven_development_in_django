import time

from django.test import TestCase
from selenium import webdriver


class FunctionalTestCase(TestCase):
    """
    FunctionalTest describes what a user can do
    """
    def setUp(self) -> None:
        """
        call before test starts
        """
        self.browser = webdriver.Chrome()

    def test_this_is_homepage(self):
        """
        This test will check if the homepage contains keyword 'install'
        """
        self.browser.get('http://localhost:8000')

        time.sleep(5)  # Let the user actually see something!

        self.assertIn('install', self.browser.page_source)

        time.sleep(5)  # Let the user actually see something!

    def tearDown(self) -> None:
        """
        call after test finish
        """
        self.browser.quit()
