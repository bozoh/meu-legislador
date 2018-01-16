# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package
from unittest import TestCase
from dadosabertos.erros import NotApiUrlError
from dadosabertos import ApiBase

class TestApiBase(TestCase):
    def setUp(self):
        self.AB = ApiBase()

    def test_erro_se_usar_uma_url_fora_da_api(self):
        url = 'http://www.google.com'
        with self.assertRaises(NotApiUrlError) as e:
            self.AB.get_dados(url)

        self.assertTrue(url in str(e.exception))

    def test_erro_se_chamar_next_direto(self):
        with self.assertRaises(NotImplementedError):
            self.AB.next()
    
    def test_erro_se_chamar_has_next_direto(self):
        with self.assertRaises(NotImplementedError):
            self.AB.has_next()

        
