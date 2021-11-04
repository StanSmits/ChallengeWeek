import csv

class Files(object):

    def csv_to_array(self, csv_file):
        with open(csv_file, newline='') as f:
            reader = csv.reader(f)
            return list(reader)

    # Krijg alle vragen uit de array

    def get_vragen(self, array):
        self.array = array
        return_array = []
        for i in self.array:
            return_array.append(i[0])
        return return_array

    def get_antwoord(self, vraag_nummer):
        return self.array[vraag_nummer][1].split(";")
    
    
    def get_afweging(self, vraag_nummer):
        # Get the 3rd indice of the array, from that get the key "afweging", split all the values with the key ";" and return them
        return self.array[vraag_nummer][3].split(";")


        
    
    def get_specialiteit(self, array):
        self.array = array
        return_array = []
        for i in self.array:
            return_array.append(i[2])
        return return_array
