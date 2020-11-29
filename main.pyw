import PySimpleGUI as sg 
from src.backend import *
melee_atk = 0

layout1 = [
    # ATTACKING ARMY
    [sg.Text("ATTACKING ARMY", size=(40, 1), font=("Helvetica", 20, "bold"))],
    [sg.Text(" " * 3), sg.Image("gfx/size16/sword.png"), sg.Text("Melee", size=(10,1)), sg.Input(default_text = '1000', size=(10, 1), key='-attacking_melee-')],
    [sg.Text(" " * 3), sg.Image("gfx/size16/crossbow.png"), sg.Text("Ranged", size=(10,1)), sg.Input(default_text = '1000', size=(10, 1), key='-attacking_ranged-')],
    [sg.Text(" " * 3), sg.Image("gfx/size16/horse.png"), sg.Text("Mounted", size=(10,1)), sg.Input(default_text = "1000", size=(10,1), key='-attacking_mounted-')],

    # DEFENDING ARMY
    [sg.Text("DEFENDING ARMY", size=(40, 1), font=("Helvetica", 20, "bold"))],
    [sg.Text(" " * 3), sg.Image("gfx/size16/sword.png"), sg.Text("Melee", size=(10,1)), sg.Input(default_text = '1000', size=(10, 1), key='-defending_melee-')],
    [sg.Text(" " * 3), sg.Image("gfx/size16/crossbow.png"), sg.Text("Ranged", size=(10,1)), sg.Input(default_text = '1000', size=(10, 1), key='-defending_ranged-')],
    [sg.Text(" " * 3), sg.Image("gfx/size16/horse.png"), sg.Text("Mounted", size=(10,1)), sg.Input(default_text = "1000", size=(10,1), key='-defending_mounted-')],
    [sg.Button("OK")]
    ]

window1 = sg.Window("Battle Simulator", layout1, size=(400, 400))




while True:
    #for i in range(200000):
        #sg.PopupAnimated('gfx/loading_screen/loading.gif', title="Loading...", background_color=None, time_between_frames=40, message="Battle Simulator", text_color='white', font=("Helvetica", 16, "bold"))
    #sg.PopupAnimated(None)

    event, values = window1.read()
    melee_atk = values['-attacking_melee-']
    ranged_atk = values['-attacking_ranged-']
    mounted_atk = values['-attacking_mounted-']

    melee_def = values['-defending_melee-']
    ranged_def = values['-defending_ranged-']
    mounted_def = values['-defending_mounted-']

    if event == "OK" or event == sg.WIN_CLOSED:
        layout2 = [
            [sg.Text("ATTACKING ARMY", size=(40, 1), font=("Helvetica", 20, "bold"))],
            [sg.Text(" " * 3), sg.Image("gfx/size16/sword.png"), sg.Text(melee_atk, size=(10,1))],
            [sg.Text(" " * 3), sg.Image("gfx/size16/crossbow.png"), sg.Text(ranged_atk, size=(10,1))],
            [sg.Text(" " * 3), sg.Image("gfx/size16/horse.png"), sg.Text(mounted_atk, size=(10,1))],
            [sg.Text(" " * 3), sg.Text("Roll: "), sg.Text("5"), sg.Image("gfx/size16/dice.png")],
            [sg.Text(" " * 3), sg.Text("Losses: "), sg.Image("gfx/size16/sword.png"), sg.Text('230', text_color='red'), sg.Image("gfx/size16/crossbow.png"), sg.Text('230', text_color='red'), sg.Image("gfx/size16/horse.png"), sg.Text('230', text_color='red'),],

            [sg.Image("gfx/size512/divider.png")],

            [sg.Text("DEFENDING ARMY", size=(40, 1), font=("Helvetica", 20, "bold"))],
            [sg.Text(" " * 3), sg.Image("gfx/size16/sword.png"), sg.Text(melee_def, size=(10,1))],
            [sg.Text(" " * 3), sg.Image("gfx/size16/crossbow.png"), sg.Text(ranged_def, size=(10,1))],
            [sg.Text(" " * 3), sg.Image("gfx/size16/horse.png"), sg.Text(mounted_def, size=(10,1))],
            [sg.Text(" " * 3), sg.Text("Roll: "), sg.Text("5"), sg.Image("gfx/size16/dice.png")],
            [sg.Text(" " * 3), sg.Text("Losses: "), sg.Image("gfx/size16/sword.png"), sg.Text('230', text_color='red'), sg.Image("gfx/size16/crossbow.png"), sg.Text('230', text_color='red'), sg.Image("gfx/size16/horse.png"), sg.Text('230', text_color='red'),]
        ]

        window2 = sg.Window("Battle Simulator", layout2, size=(400, 600))
        while True:
            event, values = window2.read()
            if event == sg.WIN_CLOSED:
                break

window1.close()
window2.close()
