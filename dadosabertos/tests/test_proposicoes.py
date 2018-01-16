from unittest import TestCase
from dadosabertos import Proposicoes

class MockedProposicoes(Proposicoes):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.__mocked_url = ''
    
    # def get_url(self):
    #     return self._work_base_uri

    def _get_dados(self, url):
        self.__mocked_url = url

    def get_dados_url(self):
        return self.__mocked_url
        

class TestProposicoes(TestCase):
    def setUp(self):
        self.p = MockedProposicoes()
        self.base_url = 'https://dadosabertos.camara.leg.br/api/v2/proposicoes'

    def test_se_url_todas_proposicoes_esta_correta(self):
        self.p.get_all()
        self.assertEqual(self.p.get_dados_url(), self.base_url)
    
    def test_se_url_todas_proposicoes_com_id_esta_correta(self):
        '''
        id Número(s) identificador(es) de uma ou mais proposições no Dados Abertos
        '''
        self.p.set_ids(['12121'])
        self.p.get_all()
        self.assertEqual(self.p.get_dados_url(), self.base_url+'?id=12121')

        ids = [1, 2, 5]
        self.p.set_ids(ids=ids)
        self.p.get_all()
        resultado = self.p.get_dados_url()

        self.assertTrue('id=1' in resultado)
        self.assertTrue('id=2' in resultado)
        self.assertFalse('id=3' in resultado)
        self.assertTrue('id=5' in resultado)
    
    def test_se_url_todas_proposicoes_com_sigla_tipo_esta_correta(self):
        '''
        Uma ou mais sigla(s) separadas por vírgulas do(s) tipo(s) das proposições que se deseja obter. 
        A lista de tipos e siglas existentes pode ser obtida em /referencias/tiposProposicao
        
        '''
        siglas=['PL', 'PEC']
        self.p.set_siglas_tipo(siglas=siglas)
        self.p.get_all()
        resultado = self.p.get_dados_url()

        self.assertTrue('siglaTipo=PL' in resultado)
        self.assertTrue('siglaTipo=PEC' in resultado)
        self.assertFalse('siglaTipo=MPV' in resultado)
        
    
    def test_se_url_todas_proposicoes_com_numero_esta_correta(self):
        '''
        Um ou mais número(s), separados por vírgula, oficialmente atribuídos às proposições segundo 
        o art. 137 do Regimento Interno, como “PL **1234**/2016”
        '''
        numeros=['1234', '4543']
        self.p.set_numeros(numeros=numeros)
        self.p.get_all()
        resultado = self.p.get_dados_url()

        self.assertTrue('numero=1234' in resultado)
        self.assertTrue('numero=4543' in resultado)
        self.assertFalse('numero=4575' in resultado)
    
    def test_se_url_todas_proposicoes_com_ano_esta_correta(self):
        '''
        Um ou mais ano(s) de apresentação das proposições que serão listadas, separados por 
        vírgulas, no formato AAAA
        '''
        self.fail()

    def test_se_url_todas_proposicoes_com_autor_esta_correta(self):
        '''
        Um ou mais números identificador(es), separados por vírgula, do(s) deputado(s) autor(es) 
        das proposições que serão listadas. Cada número deve ser o identificador exclusivo de um
        parlamentar no Dados Abertos
        '''
        self.fail()
    
    def test_se_url_todas_proposicoes_com_sigla_partido_autor_esta_correta(self):
        '''
        Uma ou mais sigla(s) separadas por vírgulas do(s) partido(s) a que pertençam os autores 
        das proposições a serem listadas
        '''
        self.fail()
    
    def test_se_url_todas_proposicoes_com_id_partido_autor_esta_correta(self):
        '''
        Identificador numérico no Dados Abertos do partido a que pertençam os autores das proposições
        que serão listadas. Esses identificadores são mais precisos do que as siglas, que podem ser 
        usadas por partidos diferentes em épocas diferentes
        '''
        self.fail()
    
    def test_se_url_todas_proposicoes_com_sigla_uf_autor_esta_correta(self):
        '''
        Uma ou mais sigla(s) de unidade(s) da federação (estados e Distrito Federal) pela(s) qual(quais)
        o(s) autor(es) das proposições selecionadas tenha(m) sido eleito(s)
        '''
        self.fail()
    
    def test_se_url_todas_proposicoes_com_data_inicio_esta_correta(self):
        '''
        Data do início do intervalo de tempo em que tenha havido tramitação das proposições a serem 
        listadas, no formato AAAA-MM-DD. Se omitido, é assumido como a data de 30 dias anteriores à 
        proposição
        '''
        self.fail()
    
    def test_se_url_todas_proposicoes_com_data_fim_esta_correta(self):
        '''
        Data do fim do intervalo de tempo em que tenha havido tramitação das proposições a serem 
        listadas. Se omitido, é considerado ser o dia em que é feita a requisição
        '''
        self.fail()
    
    def test_se_url_todas_proposicoes_com_data_apresentacao_inicio_esta_correta(self):
        '''
        Data do início do intervalo de tempo em que tenham sido apresentadas as proposições a serem 
        listadas, no formato AAAA-MM-DD
        '''
        self.fail()
    
    def test_se_url_todas_proposicoes_com_data_apresentacao_fim_esta_correta(self):
        '''
        Data do fim do intervalo de tempo em que tenham sido apresentadas as proposições a serem 
        listadas
        '''
        self.fail()
    
    def test_se_url_todas_proposicoes_com_id_situacao_esta_correta(self):
        '''
        Código(s) numérico(s), separados por vírgulas, do tipo de situação em que se encontram as 
        proposições que serão listadas. As situações possíveis podem ser obtidas em 
        /referencias/situacoesProposicao
        '''
        self.fail()

    def test_se_url_todas_proposicoes_com_pagina_esta_correta(self):
        '''
        Número da página de resultados, a partir de 1, que se deseja obter com a requisição, contendo 
        o número de itens definido pelo parâmetro itens. Se omitido, assume o valor 1.
        '''
        self.fail()

    def test_se_url_todas_proposicoes_com_itens_por_pagina_esta_correta(self):
        '''
        Número máximo de itens na página que se deseja obter com esta requisição.
        '''
        self.fail()
    

    
    
        
    

