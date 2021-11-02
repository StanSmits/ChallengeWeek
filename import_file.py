import pandas as pd
from pandas.io.parsers import read_csv

class Files(object):

    def read_csv(self,csv_file):
        read_csv = pd.read_csv(csv_file)
        return read_csv

    def csv_to_dict(self, csv_file):
        dict_file = pd.DataFrame.to_json(csv_file)
        return dict_file

    def sort_vragen(self, dict):
        self.dict = dict
        # for i in self.dict:
        #    print(i)

