# -*- coding: utf-8 -*-
'''
Lib em pyhton para a API dados aberto da câmara dos deputados
:seealso: https://dadosabertos.camara.leg.br/swagger/api.html
'''
import sys
from dadosabertos.Proposicoes import Proposicoes
from dadosabertos.api_base import ApiBase

__author__ = 'Carlos Alexandre S. da Fonseca'
__version__ = '1.0.0'
__date__ = '2017-11-16'  # YYYY-MM-DD

_DEBUG_MODE = False

if _DEBUG_MODE: # pragma: no cover
    print("Python " + ".".join(map(str, sys.version_info[:3])))
