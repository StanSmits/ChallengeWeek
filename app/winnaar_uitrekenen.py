class Winnaar(object):

    def winnaar_uitrekenen(self, antwoorden):
        for i in self:
            pass;
            #TODO: Hier moet een sorting algorithm komen zodat we kunnen
            #       Uitrekenen welke richting de 'winnaar' is van het spel
        
        studiewinnaar = ""
        punten = 0

        if punten <= 0 or punten == None:
            return "Wij hebben geen idee wat je heb gedaan, je heb minder dan 0 punten, misschien is deze opleiding niks voor jou"
        if punten == 69:
            return "You committed the funny"
        else:
            return "Het ziet er naar uit dat", studiewinnaar, "het best bij jou past!"