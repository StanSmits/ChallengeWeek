import PySimpleGUI as simple_gui
import firebase_admin
import vlc
from PIL import Image, ImageTk, ImageSequence
from pathlib import Path
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("challengeweek-6a91e-firebase-adminsdk-kbjl6-215cfa83d2.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://challengeweek-6a91e-default-rtdb.europe-west1.firebasedatabase.app/'})
ref = db.reference('/')

data=ref.get()

richtingen_kliks = {"SE":0, "FICT":0, "BDAM":0, "IAT":0}

#sjors

main_menu_layout = [[simple_gui.Image("zweinstein.png", size=(900, 600))],
                    [simple_gui.Button("Start", size=(20, 5), expand_x=True)],
                    [simple_gui.Button("Cheat sheet", size=(20, 5), expand_x=False, expand_y=True, button_color='blue on green', border_width=0)]]
                    

main_menu = simple_gui.Window(title='Codefuse Site',
                              layout=main_menu_layout,
                              size=(900, 700),
                              element_justification="c", finalize=True, margins=(0,0), element_padding=(0,0)
                            )

#freek, stijn en perry


def scherm_3(vraagnummer):
    vraag_layout = [[simple_gui.Text('Vraag: ' + data[vraagnummer]['vraag'], font='Courier 15', text_color='white', background_color='#283b5b', size=(75,2),justification='center')],
                    [simple_gui.Image("imageedit_1_4801288964.png", size=(900, 550))],
                    [[simple_gui.Button(antwoord, size=(0, 2), expand_x=True)] for antwoord in data[vraagnummer]['antwoorden']]
                    ]
                    

    vraag = simple_gui.Window(title='Vraag ' + str(vraagnummer),
                              layout=vraag_layout,
                              background_color="black",
                              size=(900, 800),
                              element_justification="c", finalize=True, margins=(1,0), element_padding=(2,2)
                            )
                              


    while True:
        event, values = vraag.read()
        if event == simple_gui.WIN_CLOSED or event == 'Cancel':
            break
        for antwoord in data[vraagnummer]['antwoorden']:
            if event == antwoord:
                vraag.Close()
                eindscherm()
                print(antwoord)
                print(vraagnummer)
                


def video(bestand): #bron: https://github.com/PySimpleGUI/PySimpleGUI/issues/4132#issuecomment-812893875
    main_menu.Hide()
    Instance = vlc.Instance()
    player = Instance.media_player_new()


    layout = [
        [simple_gui.Graph((870, 636), (0, 0), (870, 636), key='-CANVAS-')],     # OK if use [simple_gui.Canvas(size=(640, 480), key='-CANVAS-')],
        [simple_gui.Button("Volgende", size=(20, 2))]
    ]
    window = simple_gui.Window('Filmpje', layout, element_justification="c", finalize=True)

    video_panel = window['-CANVAS-'].Widget.master
    # set the window id where to render VLC's video output
    h = video_panel.winfo_id()  # .winfo_visualid()?
    player.set_hwnd(h)

    m = Instance.media_new(str(bestand))  # Path, unicode
    player.set_media(m)
    player.play()
    
    while True:

        event, values = window.read()
        if event == simple_gui.WINDOW_CLOSED:
            break
        if event == "Volgende":
            player.stop()
            window.Close()
            scherm_3(0)
        

    player.stop()
    window.close()

#roy
def eindscherm():
    eind_layout = [[simple_gui.Image(r"applaudissement-clap.gif", key = '_IMAGE_' , size=(900, 600), enable_events=True)],
                    [simple_gui.Button("Beëindig", size=(20, 5), expand_x=True)]]
                    
    eind = simple_gui.Window(title='Codefuse Site',
                              layout=eind_layout,
                              size=(900, 700),
                              element_justification="c", finalize=True, margins=(0,0), element_padding=(0,0)
                              
                            )
    while True:
        event, values = eind.read(timeout = 100)
    
        if event == simple_gui.WIN_CLOSED or event == 'Beëindig':
            exit()
        for frame in ImageSequence.Iterator(Image.open("applaudissement-clap.gif")):
            event, values = eind.read(timeout=100)
            eind['_IMAGE_'].update(data=ImageTk.PhotoImage(frame))
    eind.close()

while True:
    event, values = main_menu.read()
    if event == "Start":
        video("Harry.mp4")
    if event == simple_gui.WIN_CLOSED or event == 'Cancel' or event == 'Cheat sheet':
        break

main_menu.close()


