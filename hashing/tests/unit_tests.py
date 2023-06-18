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
