import pyrebase
from file import Files
from pyrebase.pyrebase import Firebase, initialize_app

files = Files()


class Database(object):

  def connection_database(self, config):
      self.config = config
      firebase = pyrebase.initialize_app(self.config)
      self.db = firebase.database()


  def push_csv_to_db(self, array):
    self.array = array
    vragen = files.get_vragen(self.array)
    # antwoorden = files.get_antwoord(self.array, 1)
    # afstudeer_richting = files.get_antwoord(self.array, 1)
    # print(antwoorden)
    teller = 0

    data = []
    
    for vraag_nummer in range(len(vragen)):
      data_vraag = {
        "vraag": vragen[vraag_nummer],
        "antwoorden": files.get_antwoord(vraag_nummer),
        "richting": files.get_specialiteit(array)
      }

      data.append(data_vraag)

    print(data)
    self.db.set(data)

    # for (vraag, antwoord, richting) in zip(vragen, antwoorden, afstudeer_richting):
      # if None: return
      #data = {"Vraag": vraag, "Antwoord": antwoord[0], "Antwoord2": antwoord[1], "Antwoord3": antwoord[2]}
      # self.db.child(teller).set(data)
     # teller += 1
      
    #print('Vraag:', vraag, 'Antwoord:', antwoord, "Richting", richting, 'Teller:', teller)
