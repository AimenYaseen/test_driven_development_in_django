from django.test import TestCase


class UnitTestCase(TestCase):

    def test_home_homepage_template(self):
        """
        checks whether the home template exists
        """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'hashing/home.html')
