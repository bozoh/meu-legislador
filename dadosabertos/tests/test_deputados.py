from unittest import TestCase
from dadosabertos import Deputados

class MockedDeputados(Deputados):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.__mocked_url = ''
    
    # def get_url(self):
    #     return self._work_base_uri

    def _get_dados(self, url=None):
        if not url:
            url = self._work_url + self._get_query_string()
        self.__mocked_url = url

    def get_dados_url(self):
        return self.__mocked_url
        

class TestDeputados(TestCase):
    def setUp(self):
        self.d = MockedDeputados()
        self.base_url = 'https://dadosabertos.camara.leg.br/api/v2/deputados'

    def queryTst(self, nome, valores, prefixo=''):
        resultado = self.d.get_dados_url()
        if prefixo:
            self.assertTrue(prefixo in resultado, 'URL não possui ' + prefixo + ' => ' + resultado )
        self.assertTrue(resultado.count('?') == 1, 'Query string inválida: sem ? => ' + resultado)
        
        for v in valores:
            query = nome + '=' + str(v)
            self.assertTrue(query in resultado, 'Valor não encontrado na query: ' + query + ' => ' + resultado)

        self.assertTrue(resultado.count('&') == len(valores) - 1, 'Query string inválida: => ' + resultado)
        self.assertTrue(resultado.count(nome) == len(valores), 'Valores faltando na string: => ' + resultado )

    #########################BUSCA DEPUTADO ÚNICO (DETALHADO)#################
    def test_se_url_da_deputado_esta_correta(self):
        self.d.busca_por_id(1)
        self.assertEqual(self.d.get_dados_url(), self.base_url+'/1')

    #########################DESPESAS#########################################
    def test_se_url_da_despesas_deputado_esta_correto(self):
        self.d.busca_despesas(1)
        self.assertIn(self.base_url+'/1/despesas', self.d.get_dados_url())
    
    def test_se_url_da_despesas_deputado_id_legislatura_esta_correto(self):
        valores = ['23', '24']
        self.d.set_ids_legislatura(['23', '24'])
        self.d.busca_despesas(1)
        self.queryTst('idLegislatura', valores, '/1/despesas')
    
    def test_se_url_da_despesas_deputado_ano_esta_correto(self):
        valores = ['1994', '1995']
        self.d.set_anos(valores)
        self.d.busca_despesas(1)
        self.queryTst('ano', valores, '/1/despesas')
    
    def test_se_url_da_despesas_deputado_mes_esta_correto(self):
        valores = ['01', '03']
        self.d.set_meses(valores)
        self.d.busca_despesas(1)
        self.queryTst('mes', valores, '/1/despesas')
    
    def test_se_url_da_despesas_deputado_cnpj_cpf_fornecedor_esta_correto(self):
        valores = ['123456981']
        self.d.set_cnpj_cpf_fornecedor(valores[0])
        self.d.busca_despesas(1)
        self.queryTst('cnpjCpfFornecedor', valores, '/1/despesas')

    def test_se_url_da_despesas_deputado_pagina_esta_correto(self):
        valores = [3]
        self.d.set_pagina(valores[0])
        self.d.busca_despesas(1)
        self.queryTst('pagina', valores, '/1/despesas')

    def test_se_url_da_despesas_deputado_itens_esta_correto(self):
        valores = [13]
        self.d.set_itens(valores[0])
        self.d.busca_despesas(1)
        self.queryTst('itens', valores, '/1/despesas')
    
    #########################EVENTOS#########################################
    def test_se_url_da_eventos_deputado_esta_correto(self):
        self.d.busca_eventos(1)
        self.assertIn(self.base_url+'/1/eventos', self.d.get_dados_url())
    
    #########################VOTAÇÃO#########################################
    def test_se_url_da_votacoes_da_deputado_esta_correto(self):
        self.d.busca_orgaos(1)
        self.assertIn(self.base_url+'/1/orgaos', self.d.get_dados_url())
    
    #########################MESAS#########################################
    def test_se_url_da_mesas_da_deputado_esta_correto(self):
        self.d.busca_mesa(1)
        self.assertIn(self.base_url+'/1/mesa', self.d.get_dados_url())

    ####################BUSCA GERAL DOS DEPUTADOS##############################
    def test_se_url_todos_deputados_esta_correta(self):
        self.d.busca_todos()
        self.assertEqual(self.d.get_dados_url(), self.base_url)

    def test_se_url_todas_deputados_com_id_esta_correta(self):
        '''
        id Número(s) identificador(es) de uma ou mais proposições no Dados Abertos
        '''
        self.d.set_ids(['12121'])
        self.d.busca_todos()
        self.assertEqual(self.d.get_dados_url(), self.base_url+'?id=12121')

        ids = [1, 2, 5]
        self.d.set_ids(ids=ids)
        self.d.busca_todos()
        resultado = self.d.get_dados_url()

        self.assertTrue('id=1' in resultado)
        self.assertTrue('id=2' in resultado)
        self.assertFalse('id=3' in resultado)
        self.assertTrue('id=5' in resultado)
    
    def test_se_url_todas_deputados_com_id_legislatura_esta_correta(self):
        ids=['171', '22']
        self.d.set_ids_legislatura(ids)
        self.d.busca_todos()
        resultado = self.d.get_dados_url()

        self.assertTrue('idLegislatura=171' in resultado)
        self.assertTrue('idLegislatura=22' in resultado)
        self.assertFalse('idLegislatura=1111' in resultado)
        self.assertTrue(resultado.count('idLegislatura') == 2)
    
    def test_se_url_todas_deputados_com_sigla_partido_esta_correta(self):
        siglas=['PVdoDEM', 'MDBdoPT']
        self.d.set_siglas_partidos(siglas_partidos=siglas)
        self.d.busca_todos()
        resultado = self.d.get_dados_url()

        self.assertTrue('siglaPartido=PVdoDEM' in resultado)
        self.assertTrue('siglaPartido=MDBdoPT' in resultado)
        self.assertFalse('siglaPartido=PSCdoPSOL' in resultado)
        self.assertTrue(resultado.count('siglaPartido') == 2)
    
    def test_se_url_todas_Deputados_com_id_partido_autor_esta_correta(self):
        '''
        Identificador numérico no Dados Abertos do partido a que pertençam os autores das proposições
        que serão listadas. Esses identificadores são mais precisos do que as siglas, que podem ser 
        usadas por partidos diferentes em épocas diferentes
        '''
        sigla_sexo = 'M'
        self.d.set_sigla_sexo(sigla_sexo)
        self.d.busca_todos()
        resultado = self.d.get_dados_url()

        self.assertTrue('siglaSexo=M' in resultado)
        self.assertFalse('siglaSexo=F' in resultado)
        self.assertTrue(resultado.count('siglaSexo') == 1)
    
    def test_se_url_todas_Deputados_com_sigla_uf_autor_esta_correta(self):
        '''
        Uma ou mais sigla(s) de unidade(s) da federação (estados e Distrito Federal) pela(s) qual(quais)
        o(s) autor(es) das proposições selecionadas tenha(m) sido eleito(s)
        '''
        siglas=['RJSP', 'BHPE']
        self.d.set_siglas_ufs(siglas_ufs=siglas)
        self.d.busca_todos()
        resultado = self.d.get_dados_url()

        self.assertTrue('siglaUf=RJSP' in resultado)
        self.assertTrue('siglaUf=BHPE' in resultado)
        self.assertFalse('siglaUf=RSPN' in resultado)
        self.assertTrue(resultado.count('siglaUf') == 2)
    
    def test_se_url_todas_deputados_com_pagina_esta_correta(self):
        '''
        Número da página de resultados, a partir de 1, que se deseja obter com a requisição, contendo 
        o número de itens definido pelo parâmetro itens. Se omitido, assume o valor 1.
        '''
        pagina = '22'
        self.d.set_pagina(pagina=pagina)
        self.d.busca_todos()
        resultado = self.d.get_dados_url()

        self.assertTrue('pagina=22' in resultado)
        self.assertFalse('pagina=171' in resultado)
        self.assertTrue(resultado.count('pagina') == 1)

    def test_se_url_todas_deputados_com_itens_por_pagina_esta_correta(self):
        '''
        Número máximo de itens na página que se deseja obter com esta requisição.
        '''
        itens = '171'
        self.d.set_itens(itens=itens)
        self.d.busca_todos()
        resultado = self.d.get_dados_url()

        self.assertTrue('itens=171' in resultado)
        self.assertFalse('itens=22' in resultado)
        self.assertTrue(resultado.count('itens') == 1)
