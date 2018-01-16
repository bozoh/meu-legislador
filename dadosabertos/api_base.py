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
        self.__query_list = dict()

    def _add_query_param(self, nome, valor):
        if not nome in self.__query_list:
            self.__query_list[nome] = list()

        self.__query_list[nome].append(str(valor))

    def _add_query_params(self, nome, valor):
        if not isinstance(valor, list):
            raise TypeError('O valor deve ser do tipo list')
        
        val = list(map(str, valor))
        if not nome in self.__query_list:
            self.__query_list[nome] = val
        else:
            self.__query_list[nome].extend(val)

    def _clear_query_list(self):
        self.__query_list.clear()

    def _get_query_string(self):
        if len(self.__query_list) == 0:
            return ''

        query_str = ''
        for key in self.__query_list.keys():
            values = self.__query_list[key]
            join_str = "&" + key + "="
            query_str +=  join_str + join_str.join(values)
        return '?' + query_str[1:]

    def _get_dados(self, url):
        """
        Obtém dados da API
            :param url: url da api
        """
        if not url.startswith(self._base_uri):
            raise NotApiUrlError(error_args=url)

        resp = requests.get(url, headers={'accept': 'application/json'})
        self._clear_query_list()
        return resp.json()

    def next(self):
        """
        Método abstrato, que retorna a próxima página de dados
        """
        raise NotImplementedError()
    
    # def get_base_url(self):
    #     """
    #     Método abstrato, que retorna a url base, sem query strings
    #     """
    #     raise NotImplementedError()

    def has_next(self):
        """
        Método abstrato, que retorna True se tiver próxima página de dados
        """
        raise NotImplementedError()

