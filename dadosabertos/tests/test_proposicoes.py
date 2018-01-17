from unittest import TestCase
from dadosabertos import Proposicoes

class MockedProposicoes(Proposicoes):
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
        

class TestProposicoes(TestCase):
    def setUp(self):
        self.p = MockedProposicoes()
        self.base_url = 'https://dadosabertos.camara.leg.br/api/v2/proposicoes'

    def test_se_url_todas_proposicoes_esta_correta(self):
        self.p.busca_todas()
        self.assertEqual(self.p.get_dados_url(), self.base_url)
    
    def test_se_url_da_proposicao_esta_correta(self):
        self.p.busca_por_id(1)
        self.assertEqual(self.p.get_dados_url(), self.base_url+'/1')
    
    def test_se_url_da_proposicao_relacionadas_esta_correto(self):
        self.p.busca_relacionadas(1)
        self.assertEqual(self.p.get_dados_url(), self.base_url+'/1/relacionadas')
    
    def test_se_url_da_tramitacoes_da_proposicao_esta_correto(self):
        self.p.busca_tramitacoes(1)
        self.assertEqual(self.p.get_dados_url(), self.base_url+'/1/tramitacoes')
    
    def test_se_url_da_votacoes_da_proposicao_esta_correto(self):
        self.p.busca_votacoes(1)
        self.assertEqual(self.p.get_dados_url(), self.base_url+'/1/votacoes')

    def test_se_url_todas_proposicoes_com_id_esta_correta(self):
        '''
        id Número(s) identificador(es) de uma ou mais proposições no Dados Abertos
        '''
        self.p.set_ids(['12121'])
        self.p.busca_todas()
        self.assertEqual(self.p.get_dados_url(), self.base_url+'?id=12121')

        ids = [1, 2, 5]
        self.p.set_ids(ids=ids)
        self.p.busca_todas()
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
        self.p.busca_todas()
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
        self.p.busca_todas()
        resultado = self.p.get_dados_url()

        self.assertTrue('numero=1234' in resultado)
        self.assertTrue('numero=4543' in resultado)
        self.assertFalse('numero=4575' in resultado)
    
    def test_se_url_todas_proposicoes_com_ano_esta_correta(self):
        '''
        Um ou mais ano(s) de apresentação das proposições que serão listadas, separados por 
        vírgulas, no formato AAAA
        '''
        anos=['1990', '2017']
        self.p.set_anos(anos=anos)
        self.p.busca_todas()
        resultado = self.p.get_dados_url()

        self.assertTrue('ano=1990' in resultado)
        self.assertTrue('ano=2017' in resultado)
        self.assertFalse('ano=4575' in resultado)
        self.assertTrue(resultado.count('ano') == 2)

    def test_se_url_todas_proposicoes_com_ids_autores_esta_correta(self):
        '''
        Um ou mais números identificador(es), separados por vírgula, do(s) deputado(s) autor(es) 
        das proposições que serão listadas. Cada número deve ser o identificador exclusivo de um
        parlamentar no Dados Abertos
        '''
        ids=['123990', '1222017']
        self.p.set_ids_autores(ids_autores=ids)
        self.p.busca_todas()
        resultado = self.p.get_dados_url()

        self.assertTrue('idAutor=123990' in resultado)
        self.assertTrue('idAutor=1222017' in resultado)
        self.assertFalse('idAutor=4575' in resultado)
        self.assertTrue(resultado.count('idAutor') == 2)
    
    def test_se_url_todas_proposicoes_com_nome_autor_esta_correta(self):
        '''
        Nome ou parte do nome do(s) autor(es) das proposições que se deseja obter. 
        '''
        autor = 'Teste da Silva'
        self.p.set_autor(autor=autor)
        self.p.busca_todas()
        resultado = self.p.get_dados_url()

        self.assertTrue('autor=Teste da Silva' in resultado)
        self.assertFalse('autor=Erro do João' in resultado)
        self.assertTrue(resultado.count('autor') == 1)
    
    def test_se_url_todas_proposicoes_com_sigla_partido_autor_esta_correta(self):
        '''
        Uma ou mais sigla(s) separadas por vírgulas do(s) partido(s) a que pertençam os autores 
        das proposições a serem listadas
        '''
        siglas=['PVdoDEM', 'MDBdoPT']
        self.p.set_siglas_partidos_autores(siglas_partidos_autores=siglas)
        self.p.busca_todas()
        resultado = self.p.get_dados_url()

        self.assertTrue('siglaPartidoAutor=PVdoDEM' in resultado)
        self.assertTrue('siglaPartidoAutor=MDBdoPT' in resultado)
        self.assertFalse('siglaPartidoAutor=PSCdoPSOL' in resultado)
        self.assertTrue(resultado.count('siglaPartidoAutor') == 2)
    
    def test_se_url_todas_proposicoes_com_id_partido_autor_esta_correta(self):
        '''
        Identificador numérico no Dados Abertos do partido a que pertençam os autores das proposições
        que serão listadas. Esses identificadores são mais precisos do que as siglas, que podem ser 
        usadas por partidos diferentes em épocas diferentes
        '''
        id = '171'
        self.p.set_id_partido_autor(id_partido_autor=id)
        self.p.busca_todas()
        resultado = self.p.get_dados_url()

        self.assertTrue('idPartidoAutor=171' in resultado)
        self.assertFalse('idPartidoAutor=22' in resultado)
        self.assertTrue(resultado.count('idPartidoAutor') == 1)
    
    def test_se_url_todas_proposicoes_com_sigla_uf_autor_esta_correta(self):
        '''
        Uma ou mais sigla(s) de unidade(s) da federação (estados e Distrito Federal) pela(s) qual(quais)
        o(s) autor(es) das proposições selecionadas tenha(m) sido eleito(s)
        '''
        siglas=['RJSP', 'BHPE']
        self.p.set_siglas_ufs_autores(siglas_ufs_autores=siglas)
        self.p.busca_todas()
        resultado = self.p.get_dados_url()

        self.assertTrue('siglaUfAutor=RJSP' in resultado)
        self.assertTrue('siglaUfAutor=BHPE' in resultado)
        self.assertFalse('siglaUfAutor=RSPN' in resultado)
        self.assertTrue(resultado.count('siglaUfAutor') == 2)
    
    def test_se_url_todas_proposicoes_com_data_inicio_esta_correta(self):
        '''
        Data do início do intervalo de tempo em que tenha havido tramitação das proposições a serem 
        listadas, no formato AAAA-MM-DD. Se omitido, é assumido como a data de 30 dias anteriores à 
        proposição
        '''
        data = '1500-04-22'
        self.p.set_data_inicio(data_inicio=data)
        self.p.busca_todas()
        resultado = self.p.get_dados_url()

        self.assertTrue('dataInicio=1500-04-22' in resultado)
        self.assertFalse('dataInicio=1792-04-21' in resultado)
        self.assertTrue(resultado.count('dataInicio') == 1)
    
    def test_se_url_todas_proposicoes_com_data_fim_esta_correta(self):
        '''
        Data do fim do intervalo de tempo em que tenha havido tramitação das proposições a serem 
        listadas. Se omitido, é considerado ser o dia em que é feita a requisição
        '''
        data = '1792-04-21'
        self.p.set_data_fim(data_fim=data)
        self.p.busca_todas()
        resultado = self.p.get_dados_url()

        self.assertTrue('dataFim=1792-04-21' in resultado)
        self.assertFalse('dataFim=1500-04-22' in resultado)
        self.assertTrue(resultado.count('dataFim') == 1)
    
    def test_se_url_todas_proposicoes_com_data_apresentacao_inicio_esta_correta(self):
        '''
        Data do início do intervalo de tempo em que tenham sido apresentadas as proposições a serem 
        listadas, no formato AAAA-MM-DD
        '''
        data = '1500-04-22'
        self.p.set_data_apresentacao_inicio(data_apresentacao_inicio=data)
        self.p.busca_todas()
        resultado = self.p.get_dados_url()

        self.assertTrue('dataApresentacaoInicio=1500-04-22' in resultado)
        self.assertFalse('dataApresentacaoInicio=1792-04-21' in resultado)
        self.assertTrue(resultado.count('dataApresentacaoInicio') == 1)
    
    def test_se_url_todas_proposicoes_com_data_apresentacao_fim_esta_correta(self):
        '''
        Data do fim do intervalo de tempo em que tenham sido apresentadas as proposições a serem 
        listadas
        '''
        data = '1792-04-21'
        self.p.set_data_apresentacao_fim(data_apresentacao_fim=data)
        self.p.busca_todas()
        resultado = self.p.get_dados_url()

        self.assertTrue('dataApresentacaoFim=1792-04-21' in resultado)
        self.assertFalse('dataApresentacaoFim=1500-04-22' in resultado)
        self.assertTrue(resultado.count('dataApresentacaoFim') == 1)
    
    def test_se_url_todas_proposicoes_com_id_situacao_esta_correta(self):
        '''
        Código(s) numérico(s), separados por vírgulas, do tipo de situação em que se encontram as 
        proposições que serão listadas. As situações possíveis podem ser obtidas em 
        /referencias/situacoesProposicao
        '''
        ids=['1', '7']
        self.p.set_ids_situacao(ids_situacao=ids)
        self.p.busca_todas()
        resultado = self.p.get_dados_url()

        self.assertTrue('idSituacao=1' in resultado)
        self.assertTrue('idSituacao=7' in resultado)
        self.assertFalse('idSituacao=RSPN' in resultado)
        self.assertTrue(resultado.count('idSituacao') == 2)

    def test_se_url_todas_proposicoes_com_pagina_esta_correta(self):
        '''
        Número da página de resultados, a partir de 1, que se deseja obter com a requisição, contendo 
        o número de itens definido pelo parâmetro itens. Se omitido, assume o valor 1.
        '''
        pagina = '22'
        self.p.set_pagina(pagina=pagina)
        self.p.busca_todas()
        resultado = self.p.get_dados_url()

        self.assertTrue('pagina=22' in resultado)
        self.assertFalse('pagina=171' in resultado)
        self.assertTrue(resultado.count('pagina') == 1)

    def test_se_url_todas_proposicoes_com_itens_por_pagina_esta_correta(self):
        '''
        Número máximo de itens na página que se deseja obter com esta requisição.
        '''
        itens = '171'
        self.p.set_itens(itens=itens)
        self.p.busca_todas()
        resultado = self.p.get_dados_url()

        self.assertTrue('itens=171' in resultado)
        self.assertFalse('itens=22' in resultado)
        self.assertTrue(resultado.count('itens') == 1)
