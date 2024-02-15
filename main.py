#Ce programme fonctionne trsè bien, il permet de convertir un/des PNG en PDF

#-------------Pour_IG--------------------#
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from PIL import Image


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
    global Tableau_width,Boutons_Controle, Btn_controle_width, Btn_controle_height,Space_Between_Btn,Btn_controle_x_init, Tableau_x_position
    #Tous les boutons vont être collés et centré sur le tableau
    NbBtn = len(Boutons_Controle)
    EspacePrisParLesBoutons = NbBtn * (Btn_controle_width+Space_Between_Btn)
    freeSpace = Tableau_width - (EspacePrisParLesBoutons)
    if(freeSpace>0):
        Btn_controle_x_init = Tableau_x_position + (freeSpace / 2)
    else:
        debord = EspacePrisParLesBoutons - Tableau_width
        Btn_controle_x_init = Tableau_x_position - (debord / 2)

    return Btn_controle_x_init

def choosefile():
    global Chemin
    global chemin_init
    result = filedialog.askopenfilename(initialdir=chemin_init)
    if(result==''):
        Erreur_Annulation()
    else : 
        liste_chemin.append(result)
        #Permet de revenir sur le dernier chemin ouvert en cas de réutilisation du bouton.
        chemin_init=result 
        #On prend le nom du fichier qui trouve à la fin du chemin selectionné : 
        words = result.split('/') 
        Nom_Fichier.append(words[-1]) #On prend la dernière valeur qui correspond au nom du fichier
        #On rempli le tableau pour voir l'image selectionnée
        tableau.insert( '', 'end',values=(len(liste_chemin),words[-1],result))

def gui(root):
    frame = tk.Frame(root)
    root.title("Office Assistant")
 
def Convertir_pdf():
    chemin_final = Chemin
    if(chemin_final==''):               #Verif si un chemin final est indiqué
        Erreur_Chemin_Sauvegadre()
    elif(len(liste_chemin)==0):         #Verif si une image est selctionnée
        Erreur_Selection_img()
    elif(entry2.get()==Nom_fichier_init):#Verif si un nom est donné
        Erreur_nom_fichier()
        
    elif(len(liste_chemin)==1):         #Si une image à convertir
        image_1 = Image.open(r""+liste_chemin[0])
        im_1 = image_1.convert('RGB')
        nom=chemin_final+'\\'+entry2.get()+".pdf"
        im_1.save(r""+nom)
        
    else:                               #Si plusieurs images à convertir
        Nb_image = len(liste_chemin)
        for i in range(0,Nb_image):
            Images_Multiple.append(Image.open(r""+liste_chemin[i]))
        for i in range(0,Nb_image):
            IMG_Mult.append(Images_Multiple[i].convert('RGB'))
            
        nom=chemin_final+'\\'+entry2.get()+".pdf"
        IMG_Mult[0].save(r""+nom, save_all=True, append_images=IMG_Mult[1:])

def Erreur_Chemin_Sauvegadre():
    messagebox.showinfo("Erreur", "Chemin de sauvegarde manquant")
def Erreur_Selection_img():
    messagebox.showinfo("Erreur", "Pas d'image selectionnée")
def Erreur_nom_fichier():
    messagebox.showinfo("Erreur", "Donnez un nom au fichier")
def Erreur_Annulation():
    messagebox.showinfo("Erreur", "Vous avez annulé")
def RESET():
    tableau.delete(*tableau.get_children())
    liste_chemin.clear() #RESET de la liste liste_chemin
    Nom_Fichier.clear() #RESET de la liste Nom_Fichier
    entry2.delete(0,END) #RESET du nom de fichier final
    entry2.insert(0, Nom_fichier_init) # REmise du nom initial
def Save_Path():
    global Chemin
    Chemin = filedialog.askdirectory()
    lbl1.config(text=Chemin)
    
root = tk.Tk()             #Creation de la fenetre
root.geometry("700x700")   # Taille de la fenetre

root.resizable(width=False, height=False) #blocage de la taille de la fenetre

tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tabControl.add(tab1, text ='Pdf Creator')
tabControl.add(tab2, text ='In Progress')
tabControl.pack(expand= 1, fill ="both")

gui(root) # Selection du fichier csv

#-----------BOUTON SAVE-----------------#

#------------VARIABLE_SPACE-------------#

#Tableau : 
Tableau_x_position = 50 ; Tableau_y_position = 220 
Tableau_width = 600 ; Tableau_Height = 250

#Bouton
Btn_controle_width = 50 ; Btn_controle_height = 50 ; Space_Between_Btn = 10
Btn_controle_x_init = 0 ; Btn_controle_y_init = Tableau_y_position - Btn_controle_height - 30
policeSize = 10

#image Btn Controle 
ImageReducer =  1

#----------------------------------------
#Nom Bouton, Texte, Image, Fonction

img_SelectFile = PhotoImage(file=resource_path("Pictures/AddFile.png"))
img_Reset = PhotoImage(file=resource_path("Pictures/Reset.png"))
img_Convert = PhotoImage(file=resource_path("Pictures/ConvertInPdf.png"))
img_Exit = PhotoImage(file=resource_path("Pictures/Exit.png"))

Btn_SelectFile = tk.Button(tab1) ; Btn_Reset = tk.Button(tab1) ; 
Btn_Convertir = tk.Button(tab1) ; Btn_Quitter = tk.Button(tab1) ; 

Boutons_Controle = [
    [Btn_SelectFile, "Add file",img_SelectFile, choosefile ],
    [Btn_Reset, "Reset",img_Reset, RESET],
    [Btn_Convertir, "Convertir",img_Convert, Convertir_pdf],
    [Btn_Quitter, "Quitter",img_Exit, root.destroy],
]

# Boucle placement des bouttons
CalculPositionInitialeBoutonsDeControl()

for i in range(0,len(Boutons_Controle)):
    Boutons_Controle[i][2] = Boutons_Controle[i][2].subsample(ImageReducer, ImageReducer) #Réduction de la taille de l'image
    Boutons_Controle[i][0].configure( width=Btn_controle_width, height= Btn_controle_height, font=("Helvetica", policeSize),image=Boutons_Controle[i][2], command=Boutons_Controle[i][3], text = Boutons_Controle[i][1],compound=tk.TOP)
    Boutons_Controle[i][0].place(x=Btn_controle_x_init, y=Btn_controle_y_init)
    Btn_controle_x_init = Btn_controle_x_init + Btn_controle_width + Space_Between_Btn
    Boutons_Controle[i].append(Btn_controle_x_init) #Sauvegarde de la valeur x du bouton à la fin de la liste
    Boutons_Controle[i].append(Btn_controle_y_init) #Sauvegarde de la valeur y du bouton à la fin de la liste


# Bouton_Emplacement_Sauvegarde = tk.Button(tab1, text="Dossier de Sauvegarde", command=Save_Path)
# Bouton_Emplacement_Sauvegarde.place(x=50, y=25, width=200, height=40)

# # CHemin de la sauvegarde
# lbl1 = Label(tab1, text='Veuillez selectionner un dossier', width=10)
# lbl1.place(x=250, y=25, width=400, height=40)

# #Nom fichier final
# lbl2 = Label(tab1, text="Nom du fichier pdf créé : ", width=10)
# lbl2.place(x=50, y=100, width=200, height=30)
# entry2 = Entry(tab1, text="")
# Nom_fichier_init = "Nom du fichier"
# entry2.insert(0, Nom_fichier_init)
# entry2.place(x=250, y=100, width=300, height=30)

#tableau
tableau = ttk.Treeview(tab1, columns=('Position', 'Fichier','Chemin'))
tableau.heading('Position', text='Numéro')
tableau.column("Position", minwidth=80, width=65, stretch=NO)
tableau.heading('Fichier', text='Nom du fichier')
tableau.column("Fichier", minwidth=120, width=200, stretch=NO) 
tableau.heading('Chemin', text='Chemin')
tableau.column("Chemin", minwidth=120, width=400, stretch=NO) 
tableau['show'] = 'headings' # sans ceci, il y avait une colonne vide à gauche qui a pour rôle d'afficher le paramètre "text" qui peut être spécifié lors du insert
tableau.place(x=50, y=220, width=600, height=250)

root.mainloop()
