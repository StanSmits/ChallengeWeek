import PySimpleGUI as simple_gui
from PIL import Image, ImageTk, ImageSequence




main_menu_layout = [[simple_gui.Image(r"applaudissement-clap.gif", key = '_IMAGE_' , size=(900, 600), enable_events=True)],
                    [simple_gui.Button("Beëindig", size=(20, 5), expand_x=True)]]
                    
main_menu = simple_gui.Window(title='Codefuse Site',
                              layout=main_menu_layout,
                              size=(900, 700),
                              element_justification="c", finalize=True, margins=(0,0), element_padding=(0,0)
                              
                            )
                              


while True:
    event, values = main_menu.read(timeout = 100)
    
    if event == simple_gui.WIN_CLOSED or event == 'Cancel':
        break
    for frame in ImageSequence.Iterator(Image.open("applaudissement-clap.gif")):
        event, values = main_menu.read(timeout=100)
        main_menu['_IMAGE_'].update(data=ImageTk.PhotoImage(frame))
main_menu.close()