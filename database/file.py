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
            
            
    def get_antwoord(self, vraag_nummer):
        return self.array[vraag_nummer][1].split(";")
        
    
    def get_specialiteit(self, array):
        self.array = array
        return_array = []
        for i in self.array:
            return_array.append(i[2])
        return return_array
