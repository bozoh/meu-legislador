import json
import tempfile
import os
from console_progressbar import ProgressBar
from dadosabertos import Deputados
from scraperlib import FetchAllBase

class FetchDepudados(Deputados, FetchAllBase):
    def __init__(self, path):
        super().__init__()
        self.__id_filepath = path
        #self.__dep_ids_file = self._DATA_PATH + '/dep-ids.dat'

    def _get_id_filepath(self):
        return self.__id_filepath
    
    def get_ids(self):
        if self.has_ids_file():
            return self.load_ids()

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

    def fetch_dados_deputados(self, filepath='db.json'):
        d_ids = self.get_ids()
        total = len(d_ids)
        print('Obtendo dados de %i deputados' % total)
        pbar = ProgressBar(total - 1, prefix='Dados Deputados', suffix='obtidos')
        json_file = tempfile.NamedTemporaryFile(mode='a', encoding='utf-8', delete=False)
        json_file.write('[')
        count = 0
        for d_id in d_ids:
            json_data = self.busca_por_id(d_id)
            json_file.write(json.dumps(json_data['dados']))
            pbar.next()

            if count != total -1:
                json_file.write(",\n")
            if count % 50:
                json_file.flush()
            count += 1

        json_file.write(']')
        json_file.flush()
        json_file.close()
        print('%i dados de deputados obtidos' % total)
        print('Convertendo para pandas Dataframe')
        self.to_pandas_json_file(json_file.name, filepath)
        os.remove(json_file.name)

