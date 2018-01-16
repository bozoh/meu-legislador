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

class Proposicoes(object):
    def __init__(self):
        self._base_uri = 'https://dadosabertos.camara.leg.br/api/v2/proposicoes'
        pass
    

    

