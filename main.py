#Ce programme fonctionne trsè bien, il permet de convertir un/des PNG en PDF

#-------------Pour_IG--------------------#
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import tkinter as tk
from tkinter import ttk
from PIL import Image

from PicturesConversion import process_images
from UpdatePosition import *


#-------------POur PYINSTALLER--------------------#
import os
import sys
#Commande pour créér un .exe : pyinstaller main.spec

#-------------------INIT-----------#

Chemin=''
liste_chemin=[]
Nom_Fichier = []
chemin_init="C:\\Users\Adrie\Desktop\Convertir PNG EN PDF Python"
chemin_final=''
Images_Multiple=[]
IMG_Mult=[]
files = None
PlacementUniqueFleche = 0 #Permet de ne placer qu'une fois les boutons fleches
All_data_in_tableau = []
liste_chemin_update=[]
index_from_selected_ligne = 0 # Select first line when files are imported for 1st time 

#Gestion chemin fichier #Format adapté pour pyinstaller :
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

#-----------------------------Calcul position boutons
def CalculPositionInitialeBoutonsDeControl():
    global Tableau_width,Boutons_Controle, Btn_controle_width, Btn_controle_height,Space_Between_Btn,Btn_controle_x_init, Tableau_x_position,window_width, Tableau_Height
    #Tous les boutons vont être collés et centré sur le tableau
    NbBtn = len(Boutons_Controle)
    EspacePrisParLesBoutons = NbBtn * (Btn_controle_width+Space_Between_Btn)
    freeSpace = Tableau_width - (EspacePrisParLesBoutons)
    if(freeSpace>0):
        Btn_controle_x_init = Tableau_x_position + (freeSpace / 2)

        window_width = Tableau_width + Tableau_x_position *2

    else:
        debord = EspacePrisParLesBoutons - Tableau_width
        Btn_controle_x_init = Tableau_x_position - (debord / 2)
        window_width = Tableau_width + debord

    return Btn_controle_x_init

def CalculPositionInitialeBoutonsFleche():
    global Tableau_width,Boutons_Fleche, Btn_fleche_width,Space_Between_Btn_fleche,Position_x_recalculee_BtnsFleche, Tableau_x_position,window_width, Tableau_Height
    NbBtn = len(Boutons_Fleche)
    EspacePrisParLesBoutons = NbBtn * (Btn_fleche_width+Space_Between_Btn_fleche)
    freeSpace = Tableau_width - (EspacePrisParLesBoutons)
    if(freeSpace>0):
        Position_x_recalculee_BtnsFleche = Tableau_x_position + (freeSpace / 2)
        window_width = Tableau_width + Tableau_x_position *2

    else:
        debord = EspacePrisParLesBoutons - Tableau_width
        Position_x_recalculee_BtnsFleche = Tableau_x_position - (debord / 2)
        window_width = Tableau_width + debord

    return Position_x_recalculee_BtnsFleche

def PlaceFlecheButtons():
    global Boutons_Fleche,ImageReducer,Btn_fleche_width,Btn_fleche_height,policeSize,Position_x_recalculee_BtnsFleche,Btn_fleche_y_init,Space_Between_Btn_fleche
    for i in range(0,len(Boutons_Fleche)):
        Boutons_Fleche[i][2] = Boutons_Fleche[i][2].subsample(ImageReducer, ImageReducer) #Réduction de la taille de l'image
        Boutons_Fleche[i][0].configure( width=Btn_fleche_width, height= Btn_fleche_height,image=Boutons_Fleche[i][2], command=Boutons_Fleche[i][3])
        Boutons_Fleche[i][0].place(x=Position_x_recalculee_BtnsFleche, y=Btn_fleche_y_init)
        Position_x_recalculee_BtnsFleche = Position_x_recalculee_BtnsFleche + Btn_fleche_width + Space_Between_Btn_fleche
        Boutons_Fleche[i].append(Position_x_recalculee_BtnsFleche) #Sauvegarde de la valeur x du bouton à la fin de la liste
        Boutons_Fleche[i].append(Btn_fleche_y_init) #Sauvegarde de la valeur y du bouton à la fin de la liste

def choosemultifiles():
    global files,PlacementUniqueFleche, index_from_selected_ligne
    files = filedialog.askopenfilenames(initialdir=chemin_init, title="Sélectionner plusieurs fichiers", filetypes=(("Images PNG", "*.png"), ("Images JPEG", "*.jpg"),("Images HEIC", "*.heic")))
    if files:
        Btn_Reset.configure(state=tk.NORMAL); Btn_Convertir.configure(state=tk.NORMAL)
        for file in files:
            liste_chemin.append(file)
            # print("Liste des chemin selectionnés : ", liste_chemin)
            words = file.split('/')
            Nom_Fichier.append(words[-1]) #On prend la dernière valeur qui correspond au nom du fichier
            tableau.insert( '', 'end',values=(len(liste_chemin),words[-1],file))
            All_data_in_tableau.append([len(liste_chemin),words[-1],file]) #Give list of all data in tab -> will use do modify file order


        if (PlacementUniqueFleche == 0 ): #Bloquer la repetitiuon d'ajoute  des boutons fleches
            PlaceFlecheButtons()
            PlacementUniqueFleche = 1
        DisableButtonIfNecessery()

    else:
        Erreur_Annulation()



def open_dialog():
    user_input = simpledialog.askstring("Nommez votre fichier ", "Nom du fichier :")
    if user_input is None:
        print("L'utilisateur a cliqué sur Cancel.")
    elif user_input:
        FileName = user_input
        Convertir_pdf(FileName)
    else:
        messagebox.showinfo("Erreur", "Donnez un titre au document qui va être créé")
        open_dialog()


def gui(root):
    frame = tk.Frame(root)
    root.title("Office Assistant")

def Convertir_pdf(FileName):
    global liste_chemin_update
    if (liste_chemin_update == []):
        GetFilesPAthList()

    Save_Path()
    chemin_final = Chemin
    if(chemin_final==''):               #Verif si un chemin final est indiqué
        Erreur_Chemin_Sauvegadre()
    elif(len(liste_chemin)==0):         #Verif si au moins une image est selctionnée
        Erreur_Selection_img()

    else:                               #Si plusieurs images à convertir
        process_images(liste_chemin_update, FileName, chemin_final)
        OperationTerminee(liste_chemin_update,FileName,chemin_final)

def Erreur_Chemin_Sauvegadre():
    messagebox.showinfo("Erreur", "Chemin de sauvegarde manquant")
def Erreur_Selection_img():
    messagebox.showinfo("Erreur", "Pas d'image selectionnée")
def Erreur_Annulation():
    messagebox.showinfo("Erreur", "Vous avez annulé")
def OperationTerminee(liste_chemin,FileName,chemin_final):
    message = "Fichier pdf créé avec succès\n\nDétails:\n- Nombre d'images : "+ str(len(liste_chemin)) +"\n- Nom du fichier : "+FileName+"\n- Chemin : "+chemin_final
    messagebox.showinfo("Pdf créé ! ", message)
def RESET():
    reponse = messagebox.askquestion("Confirmation", "Voulez-vous faire un reset des images selectionnées ?")
    if reponse == 'yes':
        DeleteAlldata()


def DeleteAlldata():
    global Btn_FlecheBas,Btn_FlecheHaut,PlacementUniqueFleche,files,All_data_in_tableau,Position_x_recalculee_BtnsFleche
    global liste_chemin_update, chemin_final
        # Reset Arrows button
    PlacementUniqueFleche = 0
    for btn in Boutons_Fleche:
        btn[0].place_forget()

    # Reset btn Reset et convertir
    Btn_Reset.configure(state=tk.DISABLED); Btn_Convertir.configure(state=tk.DISABLED)
    liste_chemin.clear() #RESET de la liste liste_chemin
    Nom_Fichier.clear() #RESET de la liste Nom_Fichier
    Position_x_recalculee_BtnsFleche = CalculPositionInitialeBoutonsFleche() #Permet de reset la position des btns et donc d'éviter un décallage des btns à chaque reset

    #REset List of data
    files = []
    All_data_in_tableau = []
    liste_chemin_update=[]
    FileName= []
    chemin_final = []
    #REset displayed data in Tableau
    tableau.delete(*tableau.get_children())

def Save_Path():
    global Chemin
    Chemin = filedialog.askdirectory()

def afficher_contenu_ligne(event):
    global files, index_from_selected_ligne
    if files:
        item = tableau.selection()[0]
        contenu_ligne = tableau.item(item, 'values')
        index_from_selected_ligne = int(contenu_ligne[0])
        DisableButtonIfNecessery()

def mettre_a_jour_tableau():
    global tableau
    # Effacer toutes les lignes actuelles du tableau
    for row in tableau.get_children():
        tableau.delete(row)
    # Réinsérer les données mises à jour
    for data in All_data_in_tableau:
        tableau.insert('', 'end', values=data)
    GetFilesPAthList()

def GetFilesPAthList():
    global All_data_in_tableau,liste_chemin_update,liste_chemin
    liste_chemin_update=[]
    liste_chemin_update = [element[2] for element in All_data_in_tableau]
    liste_chemin = liste_chemin_update


def ButtonFlecheDown():
    global index_from_selected_ligne,All_data_in_tableau
    if (index_from_selected_ligne is not None):
        ChangePlaceDown(All_data_in_tableau,index_from_selected_ligne)
        mettre_a_jour_tableau()
        index_from_selected_ligne += 1
        NextLineToBeAutoSelected("Down")

def ButtonFlecheUp():
    global index_from_selected_ligne,All_data_in_tableau
    if (index_from_selected_ligne is not None):
        ChangePlaceUp(All_data_in_tableau,index_from_selected_ligne)
        mettre_a_jour_tableau()
        index_from_selected_ligne -= 1
        NextLineToBeAutoSelected("Up")

def SupprimerLigne():
    global index_from_selected_ligne,All_data_in_tableau
    print("Taille de AllDataInTableau : ",len(All_data_in_tableau))
    DeleteSelectedLine(All_data_in_tableau,index_from_selected_ligne-1)
    mettre_a_jour_tableau()
    GetFilesPAthList()
    if (len(All_data_in_tableau)==0):
        DeleteAlldata()
    else:
        NextLineToBeAutoSelected("Delete")
        exit

def NextLineToBeAutoSelected(action):
    global index_from_selected_ligne,All_data_in_tableau
    if (action == 'Delete'):
        if(index_from_selected_ligne==((All_data_in_tableau[-1][0])+1)): #If select line is the last of table
            tableau.selection_set(tableau.get_children()[-1]) #Autoselection of new last line after line deletion
            index_from_selected_ligne = len(All_data_in_tableau)
        else:
            item_id_NextLine = tableau.get_children()[index_from_selected_ligne-1]
            tableau.selection_set(item_id_NextLine)
    else:
        tableau.selection_set(tableau.get_children()[index_from_selected_ligne-1]) #Autoselection of new last line after line deletion
    DisableButtonIfNecessery()

def DisableButtonIfNecessery():
    global index_from_selected_ligne
    if((index_from_selected_ligne==All_data_in_tableau[0][0]) and (index_from_selected_ligne==All_data_in_tableau[-1][0])):
        Btn_FlecheBas.configure(state=tk.DISABLED)
        Btn_FlecheHaut.configure(state=tk.DISABLED)
    elif (index_from_selected_ligne==All_data_in_tableau[-1][0]):
        Btn_FlecheBas.configure(state=tk.DISABLED)
        Btn_FlecheHaut.configure(state=tk.NORMAL)
    elif (index_from_selected_ligne==All_data_in_tableau[0][0]):
        Btn_FlecheBas.configure(state=tk.NORMAL)
        Btn_FlecheHaut.configure(state=tk.DISABLED)
    else:
        Btn_FlecheHaut.configure(state=tk.NORMAL)
        Btn_FlecheBas.configure(state=tk.NORMAL)



root = tk.Tk()             #Creation de la fenetre


root.resizable(width=False, height=False) #blocage de la taille de la fenetre

tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text ='Pdf Creator')
tabControl.pack(expand= 1, fill ="both")

gui(root) # Selection du fichier csv

#-----------BOUTON SAVE-----------------#

#------------VARIABLE_SPACE-------------#

#Tableau :
Tableau_x_position = 50 ; Tableau_y_position = 220
Tableau_width = 600 ; Tableau_Height = 250

#Bouton Controle
Btn_controle_width = 50 ; Btn_controle_height = 50 ; Space_Between_Btn = 10
Btn_controle_x_init = 0 ; Btn_controle_y_init = Tableau_y_position - Btn_controle_height - 30
window_height = Tableau_Height + Btn_controle_y_init + Tableau_y_position
policeSize = 10

#Bouton Fleches
Btn_fleche_width = 25 ; Btn_fleche_height = 25 ; Space_Between_Btn_fleche = 10
Btn_fleche_y_init = Tableau_y_position + Tableau_Height + 10

#image Btn Controle
ImageReducer =  1

#----------------------------------------
#Nom Bouton, Texte, Image, Fonction

img_SelectFile = PhotoImage(file=resource_path("Pictures/AddFile.png"))
img_Reset = PhotoImage(file=resource_path("Pictures/Reset.png"))
img_Convert = PhotoImage(file=resource_path("Pictures/ConvertInPdf.png"))
img_Exit = PhotoImage(file=resource_path("Pictures/Exit.png"))
img_Test = PhotoImage(file=resource_path("Pictures/Test.png"))

Btn_SelectFile = tk.Button(tab1) ; Btn_Reset = tk.Button(tab1) ;
Btn_Convertir = tk.Button(tab1) ; Btn_Quitter = tk.Button(tab1) ;
Btn_Test = tk.Button(tab1) ;

Boutons_Controle = [
    [Btn_SelectFile, "Add file",img_SelectFile, choosemultifiles,tk.NORMAL ],
    [Btn_Reset, "Reset",img_Reset, RESET,tk.DISABLED],
    [Btn_Convertir, "Convertir",img_Convert, open_dialog,tk.DISABLED],
    [Btn_Quitter, "Quitter",img_Exit, root.destroy,tk.NORMAL],
    # [Btn_Test, "Test",img_Test, choosemultifiles],
]

# Boucle placement des bouttons
Position_x_recalculee = CalculPositionInitialeBoutonsDeControl()

for i in range(0,len(Boutons_Controle)):
    Boutons_Controle[i][2] = Boutons_Controle[i][2].subsample(ImageReducer, ImageReducer) #Réduction de la taille de l'image
    Boutons_Controle[i][0].configure( width=Btn_controle_width, height= Btn_controle_height, font=("Helvetica", policeSize),image=Boutons_Controle[i][2], command=Boutons_Controle[i][3], text = Boutons_Controle[i][1],compound=tk.TOP,state=Boutons_Controle[i][4] )
    Boutons_Controle[i][0].place(x=Position_x_recalculee, y=Btn_controle_y_init)
    Position_x_recalculee = Position_x_recalculee + Btn_controle_width + Space_Between_Btn
    Boutons_Controle[i].append(Position_x_recalculee) #Sauvegarde de la valeur x du bouton à la fin de la liste
    Boutons_Controle[i].append(Btn_controle_y_init) #Sauvegarde de la valeur y du bouton à la fin de la liste

style = ttk.Style()
style.map('Treeview', background=[('selected', '#eb0000')])
#tableau
tableau = ttk.Treeview(tab1, columns=('Position', 'Fichier','Chemin'))
tableau.heading('Position', text='Position')
tableau.column("Position", minwidth=80, width=65, stretch=NO)
tableau.heading('Fichier', text='Nom du fichier')
tableau.column("Fichier", minwidth=120, width=200, stretch=NO)
tableau.heading('Chemin', text='Chemin')
tableau.column("Chemin", minwidth=120, width=400, stretch=NO)
tableau['show'] = 'headings' # sans ceci, il y avait une colonne vide à gauche qui a pour rôle d'afficher le paramètre "text" qui peut être spécifié lors du insert
tableau.place(x=50, y=220, width=600, height=250)

#----------------------------------------
#Nom Bouton, Texte, Image, Fonction

img_Fleche_Haut = PhotoImage(file=resource_path("Pictures/img_Fleche_Haut.png"))
img_Fleche_Bas = PhotoImage(file=resource_path("Pictures/img_Fleche_Bas.png"))
img_SupprimerLigne = PhotoImage(file=resource_path("Pictures/Reset.png"))

Btn_FlecheHaut = tk.Button(tab1) ; Btn_FlecheBas = tk.Button(tab1) ;  Btn_SupprimerLigne = tk.Button(tab1)

Boutons_Fleche = [
    [Btn_FlecheHaut, "Monter",img_Fleche_Haut, ButtonFlecheUp ],
    [Btn_SupprimerLigne, "Supprimer",img_SupprimerLigne, SupprimerLigne],
    [Btn_FlecheBas, "Descendre",img_Fleche_Bas, ButtonFlecheDown],

]

# Boucle placement des bouttons
Position_x_recalculee_BtnsFleche = CalculPositionInitialeBoutonsFleche()

root.iconbitmap(resource_path("Pictures/OfficeAssistanticone.ico"))

# Associer la fonction afficher_contenu_ligne à l'événement de clic sur une ligne
tableau.bind('<ButtonRelease-1>', afficher_contenu_ligne)

root.geometry(str(window_width) + "x" + str(window_height))  # Taille de la fenetre
root.mainloop()
