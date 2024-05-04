#-------------Pour_IG--------------------#
from tkinter import filedialog
from tkinter import *
from tkinter import simpledialog
import tkinter as tk
from tkinter import ttk
from PIL import Image
from pillow_heif import register_heif_opener

# from PicturesConversion import process_images
from Tabs.Tab_PdfCreator.UpdatePosition import *

#MessageBox import
from SharedFunctions.MessageBox import *

#-------------POur PYINSTALLER--------------------#
import os
import sys
#Commande pour créér un .exe : pyinstaller main.spec


#------------Design UI VARIABLE SPACE-------------#
#Tableau Tab1:
Table_x_Position = 50 ; Table_y_Position = 200
Table_Width = 600 ; Table_Height = 250
Tab1Table = [Table_x_Position,Table_y_Position,Table_Width,Table_Height]

#Fenetre d'affichage Tab2
Tab2DisplayWindow_x_position = 50 ; Tab2DisplayWindow_y_position = 100
Tab2DisplayWindow_width = 600 ; Tab2DisplayWindow_Height = 400
Tab2Canvas = [Tab2DisplayWindow_x_position,Tab2DisplayWindow_y_position,Tab2DisplayWindow_width,Tab2DisplayWindow_Height]


#Bouton Controle Paramètre
Control_Button_Width = 50 ; Control_Button_Height = 50 ; Space_Between_Button = 10
Control_Button_Init_x_Position = 0 ; Control_Button_Init_y_Position = Table_y_Position - Control_Button_Height - 30
Window_Height = Table_Height + Control_Button_Init_y_Position + Table_y_Position
Police_Size = 10

#Bouton Fleches Tab 1 PAramètres
Arrows_Buttons_Width = 25 ; Arrows_Buttons_Height = 25 ; Space_Between_Arrows_Buttons = 10
Arrows_Buttons_Init_y_Position = Table_y_Position + Table_Height + 10

#Bouton Zoom Tab 2 PAramètres
Zoom_Buttons_Width = 25 ; Zoom_Buttons_Height = 25 ; Space_Between_Zoom_Buttons = 10
Zoom_Buttons_Init_y_Position = Tab2DisplayWindow_y_position + Tab2DisplayWindow_Height + 10

#image Btn Controle
Picture_Reducer_Value =  1


#Gestion chemin fichier #Format adapté pour pyinstaller :
def Ressource_Path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



#---------------Calcul de la position des boutons ----------------------#
def ControlsButtonsInitPositionCalculation(Liste_Boutons_De_Control,TableForYourTab,offset):
    
    global  Control_Button_Width, Control_Button_Height,Space_Between_Button,Control_Button_Init_x_Position,Control_Button_Init_y_Position,Window_Width
    #Tous les boutons vont être collés et centré sur le tableau
    NbBtn = len(Liste_Boutons_De_Control)
    EspacePrisParLesBoutons = NbBtn * (Control_Button_Width+Space_Between_Button)
    freeSpace = TableForYourTab[2] - (EspacePrisParLesBoutons)
    if(freeSpace>0):
        Control_Button_Init_x_Position = TableForYourTab[0] + (freeSpace / 2)

        Window_Width = TableForYourTab[2] + TableForYourTab[0] *2

    else:
        debord = EspacePrisParLesBoutons - TableForYourTab[2]
        Control_Button_Init_x_Position = TableForYourTab[0] - (debord / 2)
        Window_Width = TableForYourTab[2] + debord

    # Calcul de Control_Button_Init_y_Position
    Control_Button_Init_y_Position = TableForYourTab[1] - Control_Button_Height - offset

    return Control_Button_Init_x_Position,Control_Button_Init_y_Position
