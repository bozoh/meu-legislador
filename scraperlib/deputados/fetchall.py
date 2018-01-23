import json
from console_progressbar import ProgressBar
from dadosabertos import Deputados
from scraperlib import FetchAllBase
import pandas as pd

class FetchDepudados(Deputados, FetchAllBase):
    def __init__(self, path):
        super().__init__()
        self.__id_filepath = path
        #self.__dep_ids_file = self._DATA_PATH + '/dep-ids.dat'

    def _get_id_filepath(self):
        return self.__id_filepath
    
    def _get_ids(self):
        
        ids = set()
        self.set_itens(100)
        resp = self.busca_todos()
        total = self.get_total_paginas()
        pbar = ProgressBar(total - 1, prefix='ID Deputados', suffix='obtidos')

        while self.has_next():
            for dep in resp['dados']:
                ids.add(dep['id'])
            pbar.next()
            resp = self.next()

        self.save_ids(ids)
        return ids

    def fetch_dados_deputados(self, filepath='db.json.gz'):
        d_ids = self.get_ids()
        total = len(d_ids)
        print('Obtendo dados de %i deputados' % total)
        pbar = ProgressBar(total - 1, prefix='Dados Deputados', suffix='obtidos')
        json_filename = self._create_temp_data_file(total)
        for d_id in d_ids:
            json_data = self.busca_por_id(d_id)
            self._add_data_record(json.dumps(json_data['dados']))
            pbar.next()

        print('%i dados de deputados obtidos' % total)
        print('Convertendo para pandas Dataframe')
        self.to_pandas_json_file(json_filename, filepath)
        self._clear_temp_data_file()

    def fetch_despesas_deputados(self, anos, filepath='db.json.gz'):
        d_ids = self.get_ids()
        pbar_dep = ProgressBar(len(d_ids), prefix='Total Geral', suffix='', length=100)
        self._create_temp_dataframe()

        for d_id in d_ids:
            pbar_dep.next()
            self.set_anos(anos)
            self.set_itens(100)
            json_data = self.busca_despesas(d_id)
            total = self.get_total_paginas()
            if total == 0:
                continue
            json_filename = self._create_temp_data_file(total)
            #pbar = ProgressBar(total, prefix='Despesas Deputado {}'.format(d_id), length=50)
            while True:
                json_str = json.dumps(json_data['dados'])
                self._add_data_record(json_str[1:-1])
                #pbar.next()
                if not self.has_next():
                    break
                json_data = self.next()

            df_tmp = self.to_pandas(json_filename)
            df_tmp['idDeputado'] = str(d_id)
            self._add_df_record(df_tmp)
            self._clear_temp_data_file()

        self._save_temp_dataframe(filepath)
