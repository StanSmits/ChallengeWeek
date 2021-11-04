import os
from dotenv import load_dotenv
from database import Database
from file import Files
import pyrebase

# From firebase.env, import all the data and put it into the variable firebase_config
load_dotenv()
firebase_config = {
    "apiKey": os.getenv("API_KEY"),
    "authDomain": os.getenv("AUTH_DOMAIN"),
    "databaseURL": os.getenv("DATABASE_URL"),
    "projectId": os.getenv("PROJECT_ID"),
    "storageBucket": os.getenv("STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("MESSAGING_SENDER_ID"),
    "appId": os.getenv("APP_ID"),
    "measurementId": os.getenv("MEASUREMENT_ID")
}

db = Database()
file_i = Files()

csv = 'Vragen.csv'

db.connection_database(firebase_config)

file_array = file_i.csv_to_array(csv)


print(db.push_csv_to_db(file_array))

#print(file_i.get_antwoord(file_array, 1))
