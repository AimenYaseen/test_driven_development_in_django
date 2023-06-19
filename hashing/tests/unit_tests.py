import hashlib
from django.test import TestCase

from hashing.forms import HashForm


class UnitTestCase(TestCase):

    def test_home_homepage_template(self):
        """
        checks whether the home template exists
        """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'hashing/home.html')

    def test_hash_form(self):
        """
        checks two things
        1. HashForm exists
        2. accepts a text value and form is valid
        """
        form = HashForm(data={'text': 'hello'})
        self.assertTrue(form.is_valid)

    def test_hash_func_works(self):
        """
        test that hashlib function works properly
        PS:
        1. it always returns lower case hash
        2. hexdigest returns a string
        """
        hash_text = hashlib.sha256('hello'.encode('utf-8')).hexdigest()
        self.assertEqual('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', hash_text)
