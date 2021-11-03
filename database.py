import pyrebase
from file import Files
from pyrebase.pyrebase import Firebase, initialize_app

class Database(object):

  def connection_database(self, config):
      self.config = config
      firebase = pyrebase.initialize_app(self.config)
      self.db = firebase.database()


  def push_csv_to_db(self, array):
    files = Files()
    self.array = array
    vragen = files.get_vragen(self.array)
    antwoord1 = files.get_antwoord(self.array, 1)
    teller = 0
    print(vragen)
    
    for (vraag, antwoord) in zip(vragen, antwoord1):
      print('Vraag:', vraag,'Antwoord:', antwoord, 'Teller:', teller)
    
    teller += 1
    
      # self.db.child(teller).child(i).set(vraag, antwoord)
    
    

          
