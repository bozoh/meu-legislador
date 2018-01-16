# -*- coding: utf-8 -*-
'''
Lib em pyhton para a API dados aberto da câmara dos deputados, para as Proposições
:seealso: https://dadosabertos.camara.leg.br/swagger/api.html
'''
import json
import requests
import pickle
from jsonmerge import Merger
from jsonpath_ng.ext import parse
#from console_progressbar import ProgressBar
from dadosabertos.api_base import ApiBase

class Proposicoes(ApiBase):
    def __init__(self):
        super().__init__()
        self.__proposicao_base_uri = self._base_uri + '/proposicoes'

    def get_all(self):
        url = self.__proposicao_base_uri + self._get_query_string()
        return self._get_dados(url)

    def set_ids(self, ids):
        """
        Números identificadores das proposições no Dados Abertos,
            :param ids: uma array com os ids das proposições
        """
        self._add_query_params('id', ids)
    
    def set_siglas_tipo(self, siglas):
        """
        Siglas dos tipos das proposições que se deseja obter. 
        A lista de tipos e siglas existentes pode ser obtida em /referencias/tiposProposicao
            :param siglas: siglas dos tipos de proposicões
        """
        self._add_query_params('siglaTipo', siglas)
    
    def set_numeros(self, numeros):
        self._add_query_params('numero', numeros)
    
    def set_anos(self, anos):
        self._add_query_params('ano', anos)
    
    def set_ids_autores(self, ids_autores):
        self._add_query_params('idAutor', ids_autores)
    
    def set_autor(self, autor):
        self._add_query_param('autor', autor)
    
    def set_siglas_partidos_autores(self, siglas_partidos_autores):
        self._add_query_params('siglaPartidoAutor', siglas_partidos_autores)
    
    def set_id_partido_autor(self, id_partido_autor):
        self._add_query_param('idPartidoAutor', id_partido_autor)
    
    def set_siglas_ufs_autores(self, siglas_ufs_autores):
        self._add_query_params('siglaUfAutor', siglas_ufs_autores)
    
    def set_data_inicio(self, data_inicio):
        self._add_query_param('dataInicio', data_inicio)
    
    def set_data_fim(self, data_fim):
        self._add_query_param('dataFim', data_fim)
    
    def set_data_apresentacao_inicio(self, data_apresentacao_inicio):
        self._add_query_param('dataInicio', data_apresentacao_inicio)
    
    def set_data_apresentacao_fim(self, data_apresentacao_fim):
        self._add_query_param('dataFim', data_apresentacao_fim)

    def set_ids_situacao(self, ids_situacao):
        self._add_query_params('idSituacao', ids_situacao)

    def set_pagina(self, pagina):
        self._add_query_param('pagina', pagina)
    
    def set_itens(self, itens):
        self._add_query_param('itens', itens)
    


