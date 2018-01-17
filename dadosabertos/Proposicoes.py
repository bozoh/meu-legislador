# -*- coding: utf-8 -*-
'''
Lib em pyhton para a API dados aberto da câmara dos deputados, para as Proposições
.. seealso:: https://dadosabertos.camara.leg.br/swagger/api.html
'''
from dadosabertos.api_base import ApiBase

class Proposicoes(ApiBase):
    """
    API para buscar proposições do Dados Abertos
    """
    def __init__(self):
        super().__init__()
        self.__proposicao_base_uri = self._base_uri + '/proposicoes'

    def busca_todas(self):
        """Busca todas as proposições dos Dados Abertos, com filtragem ou não
        dependente do que foi atribuido anteriosmente (set_ids, set_autor, ...)

        .. note:: Faz um requisição à /proposicoes
        
        Returns:
            [dict] -- Dados das proposições
        """
        self._work_url = self.__proposicao_base_uri
        return self._get_dados()

    def busca_por_id(self, id):
        """Busca uma proposicao em particular pelo identificador das proposições
        no Dados Abertos.
        Esse método retorna mais detalhes da proposição

        Arguments:
            id {string} -- Identificador das proposição no Dados Aberto

        Returns:
            [dict] -- Dados das proposições relacionadas
        """
        return self._get_dados(self.__proposicao_base_uri + '/' + str(id))

    def busca_relacionadas(self, id):
        """Busca as proposições relacionadas a proposição do id

        Arguments:
            id {string} -- Identificador das proposição no Dados Aberto

        Returns:
            [dict] -- Dados das proposições relacionadas
        """
        self._work_url = self.__proposicao_base_uri + '/' + str(id) + '/relacionadas'
        return self._get_dados()

    def busca_tramitacoes(self, id):
        """Busca as tramitações da proposição

        Arguments:
            id {string} -- Identificador das proposição no Dados Aberto

        Returns:
            [dict] -- Dados das tramitaões
        """
        self._work_url = self.__proposicao_base_uri + '/' + str(id) + '/tramitacoes'
        return self._get_dados()

    def busca_votacoes(self, id):
        """Busca as votações da proposição

        Arguments:
            id {string} -- Identificador das proposição no Dados Aberto

        Returns:
            [dict] -- Dados das votações
        """
        self._work_url = self.__proposicao_base_uri + '/' + str(id) + '/votacoes'
        return self._get_dados()

    def set_ids(self, ids):
        """Números identificadores das proposições no Dados Abertos,
        
        Arguments:
            ids {list} -- ids das proposições
        """
        self._add_query_params('id', ids)

    def set_siglas_tipo(self, siglas):
        """
        Siglas dos tipos das proposições que se deseja obter.
        A lista de tipos e siglas existentes pode ser obtida em 
        .. seealso:: /referencias/tiposProposicao

            :param list siglas: siglas dos tipos de proposicões
        """
        self._add_query_params('siglaTipo', siglas)

    def set_numeros(self, numeros):
        """
        Números oficialmente atribuídos às proposições segundo
        o art. 137 do Regimento Interno, como “PL 1234/2016” o número
        será 1234

            :param list numeros: números das proposições
        """
        self._add_query_params('numero', numeros)

    def set_anos(self, anos):
        """
        Anos de apresentação das proposições que serão listadas, no formato AAAA

            :param list anos: Anos de apresentação das proposições
        """
        self._add_query_params('ano', anos)

    def set_ids_autores(self, ids_autores):
        """
        Números identificadores, dos deputados autores das proposições que serão
        listadas. Cada número deve ser o identificador exclusivo de um
        parlamentar no Dados Abertos

            :param list ids_autores: Ids dos deputados autores
        """
        self._add_query_params('idAutor', ids_autores)

    def set_autor(self, autor):
        """
        Nome ou parte do nome do autor das proposições que se deseja obter.

            :param str autor: Nome ou parte do nome do autor
        """
        self._add_query_param('autor', autor)

    def set_siglas_partidos_autores(self, siglas_partidos_autores):
        """
        Siglas dos partidos a que pertençam os autores das proposições a serem listadas

            :param list siglas_partidos_autores: Siglas dos partidos
        """
        self._add_query_params('siglaPartidoAutor', siglas_partidos_autores)

    def set_id_partido_autor(self, id_partido_autor):
        """
        Identificador numérico no Dados Abertos do partido a que pertençam os autores
        das proposições que serão listadas. Esses identificadores são mais precisos do
        que as siglas, que podem ser usadas por partidos diferentes em épocas diferentes

            :param str id_partido_autor: id do partido do autor
        """
        self._add_query_param('idPartidoAutor', id_partido_autor)

    def set_siglas_ufs_autores(self, siglas_ufs_autores):
        """
        Siglas de unidades da federação (estados e Distrito Federal) pelas quais
        os autores das proposições selecionadas tenham sido eleitos

            :param list siglas_ufs_autores: Siglas das uf
        """
        self._add_query_params('siglaUfAutor', siglas_ufs_autores)

    def set_data_inicio(self, data_inicio):
        """
        Data do início do intervalo de tempo em que tenha havido tramitação das
        proposições a serem listadas, no formato AAAA-MM-DD.
        Se omitido, é assumido como a data de 30 dias anteriores à proposição

            :param str data_inicio: Data do início (AAAA-MM-DD)
        """
        self._add_query_param('dataInicio', data_inicio)

    def set_data_fim(self, data_fim):
        """
        Data do fim do intervalo de tempo em que tenha havido tramitação das
        proposições a serem listadas. Se omitido, é considerado ser o dia em que
        é feita a requisição

            :param str data_fim: Data do fim (AAAA-MM-DD)
        """
        self._add_query_param('dataFim', data_fim)

    def set_data_apresentacao_inicio(self, data_apresentacao_inicio):
        """
        Data do início do intervalo de tempo em que tenham sido apresentadas as
        proposições a serem listadas, no formato AAAA-MM-DD

            :param str data_apresentacao_inicio: data do início
            apresentação (AAAA-MM-DD).
        """
        self._add_query_param('dataApresentacaoInicio', data_apresentacao_inicio)

    def set_data_apresentacao_fim(self, data_apresentacao_fim):
        """
        Data do fim do intervalo de tempo em que tenham sido apresentadas as
        proposições a serem listadas

            :param str data_apresentacao_fim: Data de fim apresentação (AAAA-MM-DD).
        """
        self._add_query_param('dataApresentacaoFim', data_apresentacao_fim)

    def set_ids_situacao(self, ids_situacao):
        """
        Códigos numéricos do tipo de situação em que se encontram as proposições
        que serão listadas. As situações possíveis podem ser obtidas em
        /referencias/situacoesProposicao

            :param list ids_situacao: Ids da situação das proposições
        """
        self._add_query_params('idSituacao', ids_situacao)

    def set_pagina(self, pagina):
        """
        Número da página de resultados, a partir de 1, que se deseja obter com a
        requisição, contendo o número de itens definido pelo parâmetro itens.
        Se omitido, assume o valor 1.

            :param str pagina: Número da página
        """
        self._add_query_param('pagina', pagina)

    def set_itens(self, itens):
        """
        Número máximo de itens na página que se deseja obter com esta requisição.
        O máximo é 100

            :param str itens: Quantidade de itens (max. 100)
        """
        self._add_query_param('itens', itens)

if __name__ == "__main__":
    print(Proposicoes.__doc__)
