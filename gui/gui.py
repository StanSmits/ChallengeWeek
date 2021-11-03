import PySimpleGUI as simple_gui

main_menu_layout = [[simple_gui.Image("zweinstein.png", size=(900, 600))],
                    [simple_gui.Button("Start", size=(20, 5), expand_x=True)]]
                    

main_menu = simple_gui.Window(title='Codefuse Site',
                              layout=main_menu_layout,
                              size=(900, 700),
                              element_justification="c", finalize=True, margins=(0,0), element_padding=(0,0)
                            )
                              


while True:
    event, values = main_menu.read()
    if event == simple_gui.WIN_CLOSED or event == 'Cancel':
        break

main_menu.close()