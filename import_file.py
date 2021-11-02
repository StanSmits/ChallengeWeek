import pandas as pd
import csv
from pandas.io.parsers import read_csv

class Files(object):

    def read_csv(self,csv_file):
        read_csv = pd.read_csv(csv_file)
        return read_csv

    def csv_to_array(self, csv_file):
        with open(csv_file, newline='') as f:
            reader = csv.reader(f)
            return list(reader)

    def get_vragen(self, array):
        self.array = array
        return_array = []
        for i in self.array:
            return_array.append(i[0])
        return return_array
            
    
