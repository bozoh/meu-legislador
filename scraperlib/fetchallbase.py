import os
import pickle
import tempfile
from scraperlib.dataframe_json import DataFrameJson
import pandas as pd

class FetchAllBase(object):

    def __exit__(self, *exc_info):
        if self._json_file:
            os.unlink(self._json_file.name)

    def _get_id_filepath(self):
        raise NotImplementedError('Esse método deve ser sobrescrito')
    
    def _get_ids(self):
        raise NotImplementedError('Esse método deve ser sobrescrito')

    def _create_temp_data_file(self, total_records, init='[', end=']'):
        self._json_file = tempfile.NamedTemporaryFile(mode='a', encoding='utf-8', delete=False)
        self.__file_init = init
        self.__file_end = end
        self._json_file.write(init)
        self._total_records = total_records
        self._record_count = 0
        return self._json_file.name
    
    def _clear_temp_data_file(self):
        if self._json_file:
            os.unlink(self._json_file.name)
            self._json_file.name = ''

    def _add_data_record(self, data):
        self._json_file.write(data)
        self._record_count += 1

        if self._record_count < self._total_records:
            self._json_file.write(",\n")
        else:
            self._json_file.write(self.__file_end)
            self._json_file.flush()
            self._json_file.close()
            self._record_count = 0
            self._total_records = 0

        if self._record_count % 50:
            self._json_file.flush()

    def save_ids(self, dados):
        with open(self._get_id_filepath(), 'wb') as fp:
            pickle.dump(dados, fp)

    def has_ids_file(self):
        return os.path.isfile(self._get_id_filepath())

    def load_ids(self):
        if not self.has_ids_file():
            raise FileNotFoundError('Arquivo inexistente: ' + self._get_id_filepath())

        fp = open(self._get_id_filepath(), 'rb')
        return pickle.load(fp)

    def get_ids(self):
        if self.has_ids_file():
            return self.load_ids()
        return self._get_ids()

    def to_pandas(self, in_file):
        df_json = DataFrameJson(in_file)
        return df_json.get_dataframe()

    def _create_temp_dataframe(self):
        self.__df_tmp_file = tempfile.NamedTemporaryFile(mode='a', encoding='utf-8', delete=False)
        self.__get_header = True

    def _add_df_record(self, df):
        tmp_file = self.__df_tmp_file
        if self.__get_header:
            df.to_csv(tmp_file, index=False,  mode='a', encoding='utf-8') 
            self.__get_header = False
        else:
            df.to_csv(tmp_file, header=False, index=False,  mode='a', encoding='utf-8')

    def _save_temp_dataframe(self, filepath):
        filename = self.__df_tmp_file.name
        self.__df_tmp_file.flush()
        self.__df_tmp_file.close()
        tmp_df = pd.read_csv(filename)
        tmp_df.to_json(filepath, orient='split', compression='gzip')
        os.unlink(filename)

    def to_pandas_json_file(self, in_file, out_file):
        df_json = self.to_pandas(in_file)

        if not out_file.endswith('.gz'):
            out_file += '.gz'

        df_json.to_json(out_file, orient='split', compression='gzip')
