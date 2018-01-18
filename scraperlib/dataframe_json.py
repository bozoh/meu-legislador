import gzip
import ijson
import pandas as pd

class DataFrameJson(pd.DataFrame):
    def __init__(self, file_path='db.json.gz'):
        data_dict = self.__extract_data(file_path)
        super(DataFrameJson, self).__init__(data_dict)

    def get_pandas_version(self):
        return pd.__version__

    def __extract_data(self, file_path):
        if file_path.endswith('.gz'):
            fp = gzip.open(file_path)
        else:
            fp = open(file_path)

        parse = ijson.parse(fp)
        data = dict()
        list_level = 0
        tmp_list = list()
        current_key = ''
        for prefix, event, value in parse:
            if event == 'start_array':
                list_level += 1
            elif event == 'end_array':
                if list_level > 1:
                    data[current_key].append(','.join(tmp_list))
                    tmp_list.clear()
                    current_key = ''
                list_level -= 1
            elif event == 'map_key':
                if prefix != 'item':
                    current_key = prefix.replace('item.', '') + '.' + value
                else:
                    current_key += value
            elif event != 'end_map' and event != 'start_map':
                if current_key not in data:
                    data[current_key] = list()

                if list_level > 1:
                    tmp_list.append(value)
                else:
                    data[current_key].append(value)
                    current_key = ''

        return data
