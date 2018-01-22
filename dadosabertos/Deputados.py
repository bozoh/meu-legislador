# -*- coding: utf-8 -*-
'''
Lib em pyhton para a API dados aberto da câmara dos deputados, para as Proposições
.. seealso:: https://dadosabertos.camara.leg.br/swagger/api.html
'''
from dadosabertos.api_base import ApiBase

class Deputados(ApiBase):
    """
    API para buscar dados dos deputados do Dados Abertos
    """
    def __init__(self):
        super().__init__()
        self.__deputados_base_uri = self._base_uri + '/deputados'
    
    def busca_todos(self):
        self._work_url = self.__deputados_base_uri
        return self._get_dados()
    
    def busca_por_id(self, id):
        self._work_url = self.__deputados_base_uri + '/' + str(id)
        return self._get_dados()
    
    def busca_despesas(self, id):
        self._work_url = self.__deputados_base_uri + '/' + str(id) +'/despesas'
        return self._get_dados()
    
    def busca_eventos(self, id):
        self._work_url = self.__deputados_base_uri + '/' + str(id) +'/eventos'
        return self._get_dados()
    
    def busca_orgaos(self, id):
        self._work_url = self.__deputados_base_uri + '/' + str(id) +'/orgaos'
        return self._get_dados()
    
    def busca_mesa(self, id):
        self._work_url = self.__deputados_base_uri + '/' + str(id) +'/mesa'
        return self._get_dados()

    def set_ids(self, ids):
        """Números identificadores dos deputados.

        Arguments:
            ids {list} -- identificadores dos deputados
        """
        self._add_query_params("id", ids)

    def set_cnpj_cpf_fornecedor(self, cnpj_cpf_fornecedor):
        """CNPJ de uma pessoa jurídica, ou CPF de uma pessoa física, fornecedora
        do produto ou serviço (apenas números)

        Arguments:
            cnpj_cpf_fornecedor {string} -- CNPJ de uma pessoa jurídica, ou CPF de uma pessoa física
                                (apenas números)
        """
        self._add_query_param('cnpjCpfFornecedor', cnpj_cpf_fornecedor)

    def set_meses(self, meses):
        """Números dos mêses de ocorrência das despesas

        Arguments:
            meses {list} -- Números dos mêses
        """
        self._add_query_params('mes', meses)

    def set_anos(self, anos):
        """Anos de ocorrência das despesas.

        Arguments:
            meses {list} -- Anos, no formato AAAA
        """
        self._add_query_params('ano', anos)

    def set_ids_legislatura(self, ids_legislatura):
        """Números identificadores de uma ou mais legislaturas de que os parlamentares
        tenham participado

        Arguments:
            ids_legislatura {list} -- identificadores das legislaturas
        """
        self._add_query_params("idLegislatura", ids_legislatura)

    def set_siglas_ufs(self, siglas_ufs):
        """Uma ou mais sigla(s) de unidades federativas (estados e Distrito Federal).
        Pode ser obtida em */referencias/uf*. Se ausente, serão retornados deputados
        de todos os estados.

        Arguments:
            siglas_ufs {list} -- siglas de unidades federativas
        """
        self._add_query_params("siglaUf", siglas_ufs)

    def set_siglas_partidos(self, siglas_partidos):
        """Uma ou mais sigla(s) de partidos aos quais sejam filiados os deputados.
        **Atenção:** partidos diferentes podem usar a mesma sigla em diferentes
        legislaturas!

        Arguments:
            siglas_partidos {list} -- siglas de partidos
        """
        self._add_query_params("siglaPartido", siglas_partidos)

    def set_sigla_sexo(self, sigla_sexo):
        """Letra que designe o gênero dos parlamentares que se deseja buscar,
        sendo M para masculino e F para feminino

        Arguments:
            sigla_sexo {char} -- M para masculino e F para feminino
        """
        self._add_query_param("siglaSexo", sigla_sexo)

    def set_pagina(self, pagina):
        """Número da página de resultados, a partir de 1, que se deseja obter
        com a requisição, contendo o número de itens definido pelo parâmetro
        itens. Se omitido, assume o valor 1.

        Arguments:
            pagina {string} -- Número da página de resultados
        """
        self._add_query_param("pagina", pagina)

    def set_itens(self, itens):
        """Número máximo de itens na página que se deseja obter com esta requisição.

        Arguments:
            itens {string} -- Número máximo de itens na página (Max. 100)
        """
        self._add_query_param("itens", itens)
