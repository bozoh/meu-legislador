from os import path
import pickle
from scraperlib.dataframe_json import DataFrameJson

class FetchAllBase(object):

    def _get_id_filepath(self):
        raise NotImplementedError('Esse método deve ser sobrescrito')

    def save_ids(self, dados):
        with open(self._get_id_filepath(), 'wb') as fp:
            pickle.dump(dados, fp)

    def has_ids_file(self):
        return path.isfile(self._get_id_filepath())

    def load_ids(self):
        if not self.has_ids_file():
            raise FileNotFoundError('Arquivo inexistente: ' + self._get_id_filepath())

        fp = open(self._get_id_filepath(), 'rb')
        return pickle.load(fp)

    def to_pandas_json_file(self, in_file, out_file):
        df_json = DataFrameJson(in_file)

        if not out_file.endswith('.gz'):
            out_file += '.gz'

        df_json.to_json(out_file, orient='split', compression='gzip')
