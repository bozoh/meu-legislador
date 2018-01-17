# -*- coding: utf-8 -*-
"""
Lib em pyhton para a API dados aberto da câmara dos deputados, para as Proposições
.. seealso:: https://dadosabertos.camara.leg.br/swagger/api.html
"""
import re
import requests
from dadosabertos.erros import NotApiUrlError

class ApiBase(object):
    """
        Classe base para toda API, aqui contém variáveis e métodos comuns
        .. seealso:: https://dadosabertos.camara.leg.br/swagger/api.html
    """
    def __init__(self):
        self.__version__ = 'v2'
        self._base_uri = 'https://dadosabertos.camara.leg.br/api/'+self.__version__
        self._next_url = ''
        self._work_url = ''
        self._pagina_atual = 1
        self._total_paginas = 1
        self.__max_itens_por_pagina = 100
        self.__query_list = dict()

    def _add_query_param(self, nome, valor):
        """Adiciona um parâmetro / filtro à lista de query

        Arguments:
            nome {string} -- [description]
            valor {string} -- [description]
        """
        if not nome in self.__query_list:
            self.__query_list[nome] = list()
        self.__query_list[nome].append(str(valor))

    def _add_query_params(self, nome, valores):
        """Adiciona um parâmetro / filtro, com vários valores, à lista de query

        Arguments:
            nome {string} -- nome do parâmetro / filtro
            valores {list} -- valores do parâmetro / filtro

        Raises:
            TypeError -- se o valor não for uma lista
        """
        if not isinstance(valores, list):
            raise TypeError('O valor deve ser do tipo list')

        val = list(map(str, valores))
        if not nome in self.__query_list:
            self.__query_list[nome] = val
        else:
            self.__query_list[nome].extend(val)

    def _substitui_query_param(self, nome, valor):
        """Substitui o valor de um parâmetro dentro da lista de query

        Arguments:
            nome {string} -- nome do parâmetro / filtro
            valor {string/list} -- valor(es) do parâmetro / filtro
        """
        self._clear_query_param(nome)
        if isinstance(valor, list):
            self._add_query_params(nome, valor)
        else:
            self._add_query_param(nome, valor)

    def _clear_query_param(self, nome):
        """Limpa o(s) valor(es) um parâmetro / filtro dentro da lista de query
        
        Arguments:
            nome {string} -- nome do parâmetro / filtro
        """

        if not nome in self.__query_list:
            self.__query_list[nome] = list()
        self.__query_list[nome].clear()
        
    def _clear_query_list(self):
        """Limpa a lista de query
        """
        self.__query_list.clear()

    def _get_query_string(self):
        """Transfoma a lista que query em uma string, com o forato para web (url)
        """
        if len(self.__query_list) == 0:
            return ''

        query_str = ''
        for key in self.__query_list.keys():
            values = self.__query_list[key]
            join_str = "&" + key + "="
            query_str += join_str + join_str.join(values)
        return '?' + query_str[1:]

    def _get_dados(self, url=None):
        """Faz uma requisição à API
        
        Keyword Arguments:
            url {string} -- url a ser chamada (default: {None})
        
        Raises:
            NotApiUrlError -- se a chamada não for para a API dados abertod
        
        Returns:
            dict -- Dados da API
        """
        if not url:
            url = self._work_url + self._get_query_string()

        if not url.startswith(self._base_uri):
            raise NotApiUrlError(error_args=url)

        resp = requests.get(url, headers={'accept': 'application/json'})
        resp = resp.json()
        if 'links' in resp:
            self.__get_total_paginas(resp['links'])
            self.__get_pagina_atual(resp['links'])
            self._next_url = ''
            self.__get_next_url(resp['links'])

        if not self.has_next():
            self._clear_query_list()

        return resp

    def __get_pagina(self, url):
        matchs = re.search("pagina=(\d+)", url)
        if matchs:
            if matchs.group(1):
                return matchs.group(1)
        return 1

    def __get_total_paginas(self, links):
        last = ''.join([url['href'] for url in links if url['rel'] == 'last'])
        self._total_paginas = int(self.__get_pagina(last))

    def __get_pagina_atual(self, links):
        atual = ''.join([url['href'] for url in links if url['rel'] == 'self'])
        self._pagina_atual = int(self.__get_pagina(atual))

    def __get_next_url(self, links):
        self._next_url = ''.join([url['href'] for url in links if url['rel'] == 'next'])

    def get_total_paginas(self):
        """Obtém o total de páginas da reposta
        
        Returns:
            [integer] -- total de páginas
        """
        return self._total_paginas

    def next(self):
        """Retorna os dados da próxima página
        
        Returns:
            [dict] -- Dados da API
        """
        if not self._next_url:
            self._substitui_query_param('pagina', self._pagina_atual + 1)
            self._next_url = self._work_url + self._get_query_string()

        return self._get_dados(self._next_url)

    def has_next(self):
        """Retorna *True* se tiver próxima página de dados

        Returns:
            [bool] -- `True` se tiver próxima página de dados
        """
        return self._pagina_atual < self._total_paginas
