#data = {"SE": [1, 2, 3, 4, 5, 6], "FICT": [1,2,3,4,5], "IAT": [1,2,3,4], "BDAM": [1,2,3]}

class Winnaar(object):
    # Create a fuction that loops through "data" for each key it will add up all the numbers in the value, then return the key with the highest value
    def winnaar_uitrekenen(self, data):
        winnaar = ""
        max = 0
        for key, value in data.items():
            total = sum(value)
            if total > max:
                max = total
                winnaar = key
        self.winnaar_bekendmaken(winnaar, data.get(winnaar))

    def winnaar_bekendmaken(self, winnaar, punten):    
        self.punten = punten
        self.studiewinnaar = winnaar

        if self.punten <= 0 or self.punten == None:
            print("Wij hebben geen idee wat je heb gedaan, je heb minder dan 0 punten, misschien is deze opleiding niks voor jou")
        if self.punten == 6.9:
            print("You committed the funny")
        else:
            text = "Het ziet er naar uit dat", self.studiewinnaar, "het best bij jou past!"
            print(" ".join(text))
