# -*- coding: utf-8 -*-
'''
Lib em pyhton para a API dados aberto da câmara dos deputados
:seealso: https://dadosabertos.camara.leg.br/swagger/api.html


'''
class InvalidApiRequestError(Exception):
    """
    Error quando um request é invalido
    """
    def __init__(self, error_args=''):
        """
        Error quando uma URL não faz parte da API dados abertos
            :param error_args: mensagem de erro
        """
        self.error_args = error_args
        Exception.__init__(self, self.error_args)