import tkinter as tk
import csv

window = tk.Tk()

richting = {"B":0,"F":0,"S":0,"I":0}

with open('vragen.csv', newline='') as f: #zet csv om in list
    reader = csv.reader(f)
    data = list(reader)
    
def klik(vraag, index):
        richting[vraag[index*3+2]]+=int(vraag[index*3+3])
        #index*3+2 is de de richting

for vraag in data:
    label = tk.Label(text=vraag[0]) #vraag printen
    label.pack()
    
    for index, antwoord in enumerate(vraag[1::3]): #skipt het eerste element en doet elke drie
        button = tk.Button(text=antwoord, command= lambda vraag=vraag, index=index: klik(vraag,index)) #zet voor elk antwoord een knop neer
        button.pack()
    
    
