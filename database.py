import pyrebase
from pyrebase.pyrebase import Firebase, initialize_app

class Database(object):

  def connection_database(self, config):
      self.config = config
      firebase = pyrebase.initialize_app(self.config)
      self.db = firebase.database()

  def push_info_to_db(self, file):
    self.db.generate_key("Sorteerhoed")
      # self.db.push(dict)
