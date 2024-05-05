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

print(Ressource_Path("Pictures/AddFile.png"))

def IconsDeclaration():
    
    Icon_Add_File = PhotoImage(file=Ressource_Path("Pictures/AddFile.png"))
    Icon_Reset = PhotoImage(file=Ressource_Path("Pictures/Reset.png"))
    Icon_Convert_To_Pdf = PhotoImage(file=Ressource_Path("Pictures/ConvertInPdf.png"))
    Icon_Exit = PhotoImage(file=Ressource_Path("Pictures/Exit.png"))
    Icon_Test = PhotoImage(file=Ressource_Path("Pictures/test.png"))
    Icon_Validate = PhotoImage(file=Ressource_Path("Pictures/Valider.png"))

    Icon_Zoom_More = PhotoImage(file=Ressource_Path("Pictures/zoomPlus.png"))
    Icon_Zoom_Less = PhotoImage(file=Ressource_Path("Pictures/zoomMoins.png"))

    Icon_Arrow_Up = PhotoImage(file=Ressource_Path("Pictures/Icon_Arrow_Up.png"))
    Icon_Arrow_Down = PhotoImage(file=Ressource_Path("Pictures/Icon_Arrow_Down.png"))
    Icon_Delete_Selected_Line = PhotoImage(file=Ressource_Path("Pictures/Reset.png"))

    return Icon_Add_File, Icon_Reset, Icon_Convert_To_Pdf, Icon_Exit, Icon_Test, Icon_Validate, Icon_Zoom_More, Icon_Zoom_Less, Icon_Arrow_Up, Icon_Arrow_Down, Icon_Delete_Selected_Line
#---------------Calcul de la position des boutons ----------------------#
def ControlsButtonsInitPositionCalculation(Liste_Boutons_De_Control,TableForYourTab,offset):
    
    global  Control_Button_Width, Control_Button_Height,Space_Between_Button,Control_Button_Init_x_Position,Control_Button_Init_y_Position,Window_Width
    #Tous les boutons vont être collés et centré sur le tableau
    Number_Of_Buttons = len(Liste_Boutons_De_Control)
    Buttons_Total_Lenght = Number_Of_Buttons * (Control_Button_Width+Space_Between_Button)
    Free_Space = TableForYourTab[2] - (Buttons_Total_Lenght)
    if(Free_Space>0):
        Control_Button_Init_x_Position = TableForYourTab[0] + (Free_Space / 2)

        Window_Width = TableForYourTab[2] + TableForYourTab[0] *2

    else:
        Extra_Buttons_Space = Buttons_Total_Lenght - TableForYourTab[2]
        Control_Button_Init_x_Position = TableForYourTab[0] - (Extra_Buttons_Space / 2)
        Window_Width = TableForYourTab[2] + Extra_Buttons_Space

    # Calcul de Control_Button_Init_y_Position
    Control_Button_Init_y_Position = TableForYourTab[1] - Control_Button_Height - offset

    return Control_Button_Init_x_Position,Control_Button_Init_y_Position
