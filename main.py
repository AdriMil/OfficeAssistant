#Ce programme fonctionne trsè bien, il permet de convertir un/des PNG en PDF

#-------------Pour_IG--------------------#
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from PIL import Image

#-------------------INIT-----------#

Chemin=''
liste_chemin=[]
Nom_Fichier = []
chemin_init="C:\\Users\Adrie\Desktop\Convertir PNG EN PDF Python"
chemin_final=''
Images_Multiple=[]
IMG_Mult=[]

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


#----------------------------------------

Bouton_Emplacement_Sauvegarde = tk.Button(tab1, text="Dossier de Sauvegarde", command=Save_Path)
Bouton_Emplacement_Sauvegarde.place(x=50, y=25, width=200, height=40)

Bouton_Selec_image = tk.Button(tab1, text="Selectionner fichier", command=choosefile)
Bouton_Selec_image.place(x=150, y=160, width=400, height=50)

Bouton_Validation = tk.Button(tab1, text="Convertir en Pdf", command=Convertir_pdf)
Bouton_Validation.place(x=150, y=500, width=400, height=50)

Bouton_Reset= Button(tab1, text="Reset selection", command=RESET)
Bouton_Reset.place(x=150, y=575, width=200, height=50)

Bouton_Quitter = Button(tab1, text="Quitter", command=root.destroy)
Bouton_Quitter.place(x=350, y=575, width=200, height=50)


# CHemin de la sauvegarde
lbl1 = Label(tab1, text='Veuillez selectionner un dossier', width=10)
lbl1.place(x=250, y=25, width=400, height=40)

#Nom fichier final
lbl2 = Label(tab1, text="Nom du fichier pdf créé : ", width=10)
lbl2.place(x=50, y=100, width=200, height=30)
entry2 = Entry(tab1, text="")
Nom_fichier_init = "Nom du fichier"
entry2.insert(0, Nom_fichier_init)
entry2.place(x=250, y=100, width=300, height=30)

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
