import csv

class Files(object):

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
            
            
    def get_antwoord(self, array, nummer_antwoord):
        self.array = array
        self.nummer_antwoord = nummer_antwoord
        return_array = []
        for i in self.array:
            return_array.append(i[nummer_antwoord])
        return return_array
    
    
    def get_specialiteit(self, array):
        self.array = array
        return_array = []
        for i in self.array:
            return_array.append(i[5])
        return return_array

    def get_weging(self, array):
        self.array = array
        return_array = []
        for i in self.array:
            return_array.append(i[6])
        return return_array

    
