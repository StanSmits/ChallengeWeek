import PySimpleGUI as simple_gui

main_menu_layout = [[simple_gui.Text('Vraag 1', font='Courier 15', text_color='white', background_color='#283b5b', size=(75,2),justification='center')],
                    [simple_gui.Image("imageedit_1_4801288964.png", size=(900, 550))],
                    [simple_gui.Button("antwoord A", size=(0, 2), expand_x=True),simple_gui.Button("antwoord B", size=(0, 2), expand_x=True)],
                    [simple_gui.Button("antwoord C", size=(0, 2), expand_x=True),simple_gui.Button("antwoord D", size=(0, 2), expand_x=True)]
                    ]  

main_menu = simple_gui.Window(title='Vraag 1',
                              layout=main_menu_layout,
                              background_color="black",
                              size=(900, 700),
                              element_justification="c", finalize=True, margins=(1,0), element_padding=(2,2)
                            )
                              
while True:
    event, values = main_menu.read()
    if event == simple_gui.WIN_CLOSED or event == 'Cancel':
        break

main_menu.close()
