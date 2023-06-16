import time

from django.test import TestCase
from selenium import webdriver


class FunctionalTestCase(TestCase):
    def setUp(self) -> None:
        """
        call before test starts
        """
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        """
        call after test finish
        """
        self.browser.quit()


browser = webdriver.Chrome()
browser.get('http://localhost:8000')

time.sleep(5)  # Let the user actually see something!

assert browser.page_source.find("install")

time.sleep(5)  # Let the user actually see something!

browser.quit()
