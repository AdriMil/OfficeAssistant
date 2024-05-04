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
Tableau_x_position = 50 ; Tableau_y_position = 200
Tableau_width = 600 ; Tableau_Height = 250
Tab1Tableau = [Tableau_x_position,Tableau_y_position,Tableau_width,Tableau_Height]

#Fenetre d'affichage Tab2
Tab2DisplayWindow_x_position = 50 ; Tab2DisplayWindow_y_position = 100
Tab2DisplayWindow_width = 600 ; Tab2DisplayWindow_Height = 400
Tab2Canvas = [Tab2DisplayWindow_x_position,Tab2DisplayWindow_y_position,Tab2DisplayWindow_width,Tab2DisplayWindow_Height]


#Bouton Controle Paramètre
Btn_controle_width = 50 ; Btn_controle_height = 50 ; Space_Between_Btn = 10
Btn_controle_x_init = 0 ; Btn_controle_y_init = Tableau_y_position - Btn_controle_height - 30
window_height = Tableau_Height + Btn_controle_y_init + Tableau_y_position
policeSize = 10

#Bouton Fleches Tab 1 PAramètres
Btn_fleche_width = 25 ; Btn_fleche_height = 25 ; Space_Between_Btn_fleche = 10
Btn_fleche_y_init = Tableau_y_position + Tableau_Height + 10

#Bouton Zoom Tab 2 PAramètres
Btn_zoom_width = 25 ; Btn_zoom_height = 25 ; Space_Between_Btn_zoom = 10
Btn_zoom_y_init = Tab2DisplayWindow_y_position + Tab2DisplayWindow_Height + 10

#image Btn Controle
ImageReducer =  1


#Gestion chemin fichier #Format adapté pour pyinstaller :
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



#---------------Calcul de la position des boutons ----------------------#
def CalculPositionInitialeBoutonsDeControl(Liste_Boutons_De_Control,TableForYourTab,offset):
    
    global  Btn_controle_width, Btn_controle_height,Space_Between_Btn,Btn_controle_x_init,Btn_controle_y_init,window_width
    #Tous les boutons vont être collés et centré sur le tableau
    NbBtn = len(Liste_Boutons_De_Control)
    EspacePrisParLesBoutons = NbBtn * (Btn_controle_width+Space_Between_Btn)
    freeSpace = TableForYourTab[2] - (EspacePrisParLesBoutons)
    if(freeSpace>0):
        Btn_controle_x_init = TableForYourTab[0] + (freeSpace / 2)

        window_width = TableForYourTab[2] + TableForYourTab[0] *2

    else:
        debord = EspacePrisParLesBoutons - TableForYourTab[2]
        Btn_controle_x_init = TableForYourTab[0] - (debord / 2)
        window_width = TableForYourTab[2] + debord

    # Calcul de Btn_controle_y_init
    Btn_controle_y_init = TableForYourTab[1] - Btn_controle_height - offset

    return Btn_controle_x_init,Btn_controle_y_init
