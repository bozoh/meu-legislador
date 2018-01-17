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
            self.AB._get_dados(url)

        self.assertTrue(url in str(e.exception))

    def test_add_query_params_gera_error_se_nao_passar_um_list(self):
        with self.assertRaises(TypeError) as e:
            self.AB._add_query_params('teste','asas')
        self.assertEqual('O valor deve ser do tipo list', str(e.exception))

    def test_get_query_string(self):
        self.AB._add_query_param('teste',1)
        self.AB._add_query_param('teste',2)
        self.AB._add_query_param('teste',3)
        self.AB._add_query_param('prova',3)
        self.AB._add_query_param('prova',2)
        self.AB._add_query_param('prova',1)

        result = self.AB._get_query_string()
        self.assertTrue(result.count('?') == 1)
        self.assertTrue(result.count('&') == 5, result)
        self.assertTrue(result.count('=') == 6)
        self.assertTrue(result.count('teste') == 3)
        self.assertTrue(result.count('prova') == 3)
        self.assertTrue('teste=1' in result)
        self.assertTrue('teste=2' in result)
        self.assertTrue('teste=3' in result)
        self.assertTrue('prova=1' in result)
        self.assertTrue('prova=2' in result)
        self.assertTrue('prova=3' in result)

        test = [1, 2, 5]
        self.AB._clear_query_list()
        self.AB._add_query_params('testes', test)
        result = self.AB._get_query_string()
        self.assertTrue(result.count('?') == 1)
        self.assertTrue(result.count('&') == 2)
        self.assertTrue(result.count('=') == 3)
        self.assertTrue(result.count('testes') == 3)

        self.assertTrue('testes=1' in result)
        self.assertTrue('testes=2' in result)
        self.assertFalse('testes=3' in result)
        self.assertTrue('testes=5' in result)
    
