# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 21:22:41 2021

@author: markm
"""

import PySimpleGUI as sg
import AnimeOpsAndEndsProj as ao

def main():
    sg.theme('DarkAmber')
    layout = [  [sg.Text("Welcome to the Anime Openings Finder!")],
                [sg.Text('Enter in your MAL username. No spaces or other characters please: '), sg.InputText()],
                [sg.Button("Submit", button_color=("white", "blue"))],
                [sg.Text("", size = (45,1), key = '-LEN-')]
    ]
    cont = True
    window = sg.Window("The Anime Openings Finder").Layout(layout)
    username = ""
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Submit": # if user closes window or clicks cancel
            window['-LEN-'].Update('Generating File... May Take Me A Bit!')
            window.Refresh()
            animes,bb = ao.getOps(values[0])
            if animes == False:
                cont = False
            break
        
    window.close()        
    
    if cont == False:
        layout7 = [  [sg.Text("Username didn't work! Maybe try again and check spelling? :)")]  ]

        window7 = sg.Window("The Anime Openings Finder").Layout(layout7)
        while True:
            event, values = window7.read()
            if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
                break
        window7.close()
    else:
        x = ""
        for i,n in enumerate(animes):
            x = x + "   " + "   "+ n + ": " + bb[i] + "\n"
        #new window
        layout2 = [  [sg.Text("Done! File has been created, and contains the openings to all of your finished anime! File is named anime_openings.txt. Enjoy!")],
                    [sg.Text("   " + 'Anime the finder found openings for: ')],
                    [sg.Text(x)]
        ]
    
        window2 = sg.Window("The Anime Openings Finder").Layout(layout2)
        while True:
            event, values = window2.read()
            if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
                break
            
        window2.close()
    


if __name__ == "__main__":
    main()