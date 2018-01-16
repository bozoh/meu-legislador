# -*- coding: utf-8 -*-
'''
Lib em pyhton para a API dados aberto da câmara dos deputados, para as Proposições
:seealso: https://dadosabertos.camara.leg.br/swagger/api.html
'''
import requests
from dadosabertos.erros import NotApiUrlError

class ApiBase(object):
    '''
        Classe base para toda API, aqui contem variaceis e metodos comuns
        :seealso: https://dadosabertos.camara.leg.br/swagger/api.html
    '''
    def __init__(self):
        self.__version__ = 'v2'
        self._base_uri = 'https://dadosabertos.camara.leg.br/api/'+self.__version__
        self.__max_itens_por_pagina = 100

    def get_dados(self, url):
        """
        Obtém dados da API
            :param url: url da api
        """
        if not url.startswith(self._base_uri):
            raise NotApiUrlError(error_args=url)

        if not '&itens=' in url:
            url = url + '&itens=' + self.__max_itens_por_pagina

        resp = requests.get(url, headers={'accept': 'application/json'})
        return resp.json()

    def next(self):
        """
        Método abstrato, que retorna a próxima página de dados
        """
        raise NotImplementedError()
    
    def has_next(self):
        """
        Método abstrato, que retorna True se tiver próxima página de dados
        """
        raise NotImplementedError()

