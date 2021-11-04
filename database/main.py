import os
from dotenv import load_dotenv
from database import Database
from file import Files
import pyrebase

firebase_config = {
   "apiKey": "AIzaSyDOgtw11XJT7X3Kv4JJG96pVL0d_F7tYws",
   "authDomain": "challengeweek-6a91e.firebaseapp.com",
   "databaseURL": "https://challengeweek-6a91e-default-rtdb.europe-west1.firebasedatabase.app",
   "projectId": "challengeweek-6a91e",
   "storageBucket": "challengeweek-6a91e.appspot.com",
   "messagingSenderId": "1012250981140",
   "appId": "1:1012250981140:web:8f4fc6f9419ec9acdec801",
   "DEFAULT_TOKEN": "7igGn3usI1vfEr7uItZdLcdqr12mz5iDviu3HBRt"
 }

db = Database()
file_i = Files()

csv = 'Vragen.csv'

file_array = file_i.csv_to_array(csv)

db.connection_database(firebase_config)

# print(db.push_csv_to_db(file_array))
