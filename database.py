import pyrebase
from pyrebase.pyrebase import Firebase, initialize_app

class Database(object):

  def connection_database(self, config):
      self.config = config
      firebase = pyrebase.initialize_app(self.config)
      self.db = firebase.database()

  def push_dict_to_db(self, dict):
    self.db.generate_key("Sorteerhoed")
    # for i in dict:
    #for k in dict[i]:
    #print(dict[i][k])
      # self.db.push(dict)





#   def push():
# for i in data:
#     for k in data[i]:
#         print(data[i][k])

