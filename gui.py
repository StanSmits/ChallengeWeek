import PySimpleGUI as simple_gui
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("challengeweek-6a91e-firebase-adminsdk-kbjl6-215cfa83d2.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://challengeweek-6a91e-default-rtdb.europe-west1.firebasedatabase.app/'})
ref = db.reference('/')

data=ref.get()

main_menu_layout = [[simple_gui.Image("zweinstein.png", size=(900, 600))],
                    [simple_gui.Button("Start", size=(20, 5), expand_x=True)]]
                    

main_menu = simple_gui.Window(title='Codefuse Site',
                              layout=main_menu_layout,
                              size=(900, 700),
                              element_justification="c", finalize=True, margins=(0,0), element_padding=(0,0)
                            )

#freek

def scherm_2(vraagnummer):
    main_menu.Hide()
    vraag_layout = [    [simple_gui.Text(data[vraagnummer]['vraag'])],
                        #for antwoord in data[vraagnummer]['antwoorden']:
                        [simple_gui.Button(antwoord) for antwoord in data[vraagnummer]['antwoorden']]]

    vraag = simple_gui.Window(title="test",
                              layout=vraag_layout,
                              size=(400, 400),
                              element_justification="c", finalize=True, margins=(0,0), element_padding=(0,0)
                              )

    while True:
        event, values = vraag.read()
        if event == simple_gui.WIN_CLOSED or event == 'Next':
            vraag.close()
            break
        
while True:
    event, values = main_menu.read()
    if event == "Start":
        scherm_2(1)
    if event == simple_gui.WIN_CLOSED or event == 'Cancel':
        break

main_menu.close()
