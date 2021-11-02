from os import read

from pandas.io.parsers import read_csv
from database import Database
from import_file import Files
import pyrebase

db = Database()
file = Files()

csv = 'Vragen.csv'

firebase_config = {
    "apiKey": "AIzaSyDOgtw11XJT7X3Kv4JJG96pVL0d_F7tYws",
    "authDomain": "challengeweek-6a91e.firebaseapp.com",
    "databaseURL": "https://challengeweek-6a91e-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "challengeweek-6a91e",
    "storageBucket": "challengeweek-6a91e.appspot.com",
    "messagingSenderId": "1012250981140",
    "appId": "1:1012250981140:web:8f4fc6f9419ec9acdec801"
}

db.connection_database(firebase_config)

file_array = file.csv_to_array(csv)

print(file.get_vragen(file_array))