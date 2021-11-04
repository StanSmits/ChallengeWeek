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
    data = []
    
    for vraag_nummer in range(len(vragen)):
      data_vraag = {
        "vraag": vragen[vraag_nummer],
        "antwoorden": files.get_antwoord(vraag_nummer),
        "richting": files.get_specialiteit(array),
        "afweging": files.get_afweging(vraag_nummer)
      }
      data.append(data_vraag)

    print(data)
    self.db.set(data)

  def get_data(self):
    data = self.db.child("0").get()
    return data.val()

  def get_vraag(self, vraag_nummer):
    data = self.db.child(vraag_nummer).get()
    return data.val().get("vraag")

  def get_antwoord(self, vraag_nummer):
    data = self.db.child(vraag_nummer).get()
    return data.val().get("antwoorden")
  
  def get_richting(self, vraag_nummer):
    data = self.db.child(vraag_nummer).get()
    return data.val().get("richting")
  