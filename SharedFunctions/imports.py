#-------------Pour_IG--------------------#
from tkinter import PhotoImage, NO, ttk,simpledialog,filedialog
import tkinter as tk

from PIL import Image
from pillow_heif import register_heif_opener

from Tabs.Tab_PdfCreator.UpdatePosition import ChangePlaceUp,ChangePlaceDown,DeleteSelectedLine

#MessageBox import
from SharedFunctions.MessageBox import Error_BadSavePath,Error_NoPicture,Error_Cancelation,Info_ProcessFinished,INfo_Reset,Info_Reset_Tab2,Info_FileSaved

#-------------Pour PYINSTALLER--------------------#
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

#Format for pictures to import
filetypes = [("Images compatibles", "*.png;*.jpg;*.heic")]

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


# Work with HEIC Picture
def ConvertHeicToPillowFormat(heic_path):
    # Enregistrement du module d'ouverture pour le format HEIC
    register_heif_opener()
    # Ouverture de l'image HEIC et conversion en mode RGB
    with Image.open(heic_path) as im:
        return im.convert("RGB")

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

def PlaceButtonsAutomaticaly(Button_List,Position_y_recalculee,Button_Width,Button_Height,Space_Between_Button,Picture_Reducer_Value,Position_x_recalculee,Police_Size,TextDisplay,Init_State):
    for i in range(0,len(Button_List)):
        Button_List[i][2] = Button_List[i][2].subsample(Picture_Reducer_Value, Picture_Reducer_Value) #Réduction de la taille de l'image
        Button_List[i][0].configure( width=Button_Width, height= Button_Height, font=("Helvetica", Police_Size),image=Button_List[i][2], command=Button_List[i][3] )
        Button_List[i][0].place(x=Position_x_recalculee, y=Position_y_recalculee)
        if(TextDisplay==1):Button_List[i][0].configure(text = Button_List[i][1],compound=tk.TOP)
        if(Init_State==1):Button_List[i][0].configure(state=Button_List[i][4])
        Position_x_recalculee = Position_x_recalculee + Button_Width + Space_Between_Button
        Button_List[i].append(Position_x_recalculee) #Sauvegarde de la valeur x du bouton à la fin de la liste
        Button_List[i].append(Position_y_recalculee) #Sauvegarde de la valeur y du bouton à la fin de la liste

#Processing information
def DisplayProcessing(Display_Window_x_position,Displa_yWindow_y_position,Display_Window_Width,Display_Window_Height,tab):
    global cadre, texte, ascenseur
    cadre = tk.Frame(tab,borderwidth=1, relief="solid")
    cadre.place(x=Display_Window_x_position, y=Displa_yWindow_y_position, width=Display_Window_Width, height=Display_Window_Height)
    texte = tk.Text(cadre, wrap=tk.WORD)
    texte.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    ascenseur = ttk.Scrollbar(cadre, orient=tk.VERTICAL, command=texte.yview)
    ascenseur.pack(side=tk.RIGHT, fill=tk.Y)
    texte.config(yscrollcommand=ascenseur.set)

def UpdateProcessing(TexteToUpdate):
        texte.insert(tk.END, "{}\n".format(TexteToUpdate))
        texte.see(tk.END)  
        cadre.update()

def HideProcessing():
    cadre.place_forget()
    texte.delete(1.0, tk.END)