# -*- coding: utf-8 -*-
'''
Lib em pyhton para falicitar a extração de dados da API dados aberto da 
câmara dos deputados
.. seealso:: https://dadosabertos.camara.leg.br/swagger/api.html
'''
import sys
from scraperlib.fetchallbase import FetchAllBase
from scraperlib.deputados.fetchall import FetchDepudados
from scraperlib.proposicoes.fetchall import FetchProposicoes
from scraperlib.dataframe_json import DataFrameJson

__author__ = 'Carlos Alexandre S. da Fonseca'
__version__ = '1.0.0'
__date__ = '2017-11-16'  # YYYY-MM-DD

_DEBUG_MODE = False

if _DEBUG_MODE: # pragma: no cover
    print("Python " + ".".join(map(str, sys.version_info[:3])))
