from os import read

from pandas.io.parsers import read_csv
from database import Database
from import_file import Files
import pyrebase

db = Database()
file = Files()

csv = 'Vragen2.csv'

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

readCsv = file.read_csv(csv)

dict = file.csv_to_dict(readCsv)
teller = 0
print(dict)


# print(readCsv)
# print("-----------------------------")
# print(dict)


# print(file.sort_vragen(dict))





# print(type(data))

# for i in data:
#     for k in i:
#         print(k)  # Hier print hij alle vragen   

