import hashlib

from django.core.exceptions import ValidationError
from django.test import TestCase

from hashing.forms import HashForm
from hashing.models import Hash


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

    def save_hash(self) -> Hash:
        """
        save the text 'hello' and its hash in db and return it
        """
        _hash = Hash()
        _hash.text = 'hello'
        _hash.hash = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
        _hash.save()
        return _hash

    def test_hash_object(self):
        """
        test that the hash model works or not
        """
        _hash = self.save_hash()

        # match class hash and database hash
        pulled_hash = Hash.objects.get(hash='2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
        self.assertEqual(_hash.hash, pulled_hash.hash)

    def test_hash_view(self):
        """
        tes if the hash view returns the right string for the given hash
        """
        _hash = self.save_hash()

        # call hash view
        response = self.client.get('/hash/2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
        self.assertContains(response, 'hello')

    def test_bad_data(self):
        """
        test if model validations work properly or not
        """
        def bad_hash():
            _hash = Hash()
            _hash.hash = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824kiyg'
            _hash.full_clean()

        self.assertRaises(ValidationError, bad_hash)
