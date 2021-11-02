import pyrebase
from pyrebase.pyrebase import Firebase, initialize_app

class Database(object):

  def connection_database(self, config):
      self.config = config
      firebase = pyrebase.initialize_app(self.config)
      self.db = firebase.database()

