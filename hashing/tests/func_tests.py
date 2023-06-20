import time

from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


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

        self.assertIn('Enter hash here:', self.browser.page_source)

    def test_hash_of_hello(self):
        """
        simulate input as 'hello' and then check its hash
        """
        self.browser.get('http://localhost:8000')

        # find an element by its id
        text = self.browser.find_element(By.ID, 'id_text')
        # set that elements value to 'hello'
        text.send_keys('hello')
        # find an element by its name
        self.browser.find_element(By.NAME, 'submit').click()
        # assert if the hello's hash appear on homepage
        self.assertIn('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', self.browser.page_source)

    def test_hash_ajax(self):
        self.browser.get('http://localhost:8000')
        text = self.browser.find_element(By.ID, 'id_text')
        text.send_keys('hello')
        time.sleep(5)  # WAIT for AJAX
        self.assertIn('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', self.browser.page_source)

    def tearDown(self) -> None:
        """
        call after test finish
        """
        self.browser.quit()
