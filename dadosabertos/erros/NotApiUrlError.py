# -*- coding: utf-8 -*-
'''
Lib em pyhton para a API dados aberto da câmara dos deputados
:seealso: https://dadosabertos.camara.leg.br/swagger/api.html


'''
class NotApiUrlError(Exception):
    """
    Error quando uma URL não faz parte da API dados abertos
        :param Exception:
    """
    def __init__(self, error_args=''):
        """
        Error quando uma URL não faz parte da API dados abertos
            :param error_args: Url chamada
        """
        self.error_args = error_args
        Exception.__init__(self, "A Url não faz parte a API {0}".format(self.error_args))
