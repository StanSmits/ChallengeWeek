import firebase_admin
import sys
from PyQt5 import QtCore, QtWidgets

from firebase_admin import credentials
from firebase_admin import db
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

cred = credentials.Certificate("challengeweek2-firebase-adminsdk-35542-90afd2c806.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://challengeweek2-default-rtdb.europe-west1.firebasedatabase.app/'})
ref = db.reference('/')

data=ref.get()

def vraag(nummer):
    from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Vraag" + str(nummer))
    layout = QVBoxLayout()
    layout.addWidget(QLabel(data[nummer]['vraag']))
    for antwoord in data[nummer]['antwoorden']:
        layout.addWidget(QPushButton(antwoord))
    window.setLayout(layout)
    window.show()
    app.exec()


vraag(10)
