import os
import pandas as pd
import numpy as np 

class Csv(object):

    DATA_FOLDER = 'data'

    def __init__(self, filename, encoding, sep):
        self.encoding = encoding
        self.sep = sep
        self.filename = filename
    
    def __get_csv_path(self):
        dir_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) + '/' + self.DATA_FOLDER
        return os.path.join(dir_path, self.filename)

    def get_data(self):
        return pd.read_csv(self.__get_csv_path() + '.csv', encoding = self.encoding, sep = self.sep, low_memory=False) 