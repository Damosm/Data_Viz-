import os
import pandas as pd

class Csv(object):

    DATA_FOLDER = 'data'

    def __init__(self, filename, encoding, sep):
        self.filename = filename
    
    def __get_csv_path(self):
        dir_path = os.path.dirname(os.path.realpath(__file__)) + '/' + self.DATA_FOLDER
        return os.path.join(dir_path, self.filename)

    def get_data(self):
        return pd.read_csv(self.__get_csv_path() + '.csv', encoding=encoding, sep=sep) 