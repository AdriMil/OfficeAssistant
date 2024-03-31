# 01/07/23 : Semble être la derniere version 

#-------------Pour_IG--------------------#
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from PIL import Image
from PIL import ImageTk  
 
#-------------------INIT-----------#

Chemin_fichier=''

Nom_Fichier = ''
chemin_init="C:\\Users\Adrie\Desktop\Python Fond Transparent"
chemin_final=''
Images_Multiple=[]
IMG_Mult=[]
Nom_Fichier_final=''
img = 0
init=0
c1=c2=c3=None

SaveCoordonees = []


#-------------0-Lancement de l'interface WEB-------------#
def gui(root):
    frame = tk.Frame(root)
    root.title("Colors Backgroud to transparent")
    frame.pack(expand=1, fill='both')

#-------------1-Clic sur le Canvas ou sur le bouton pour charger une image-------------#

def click_on_canvas(event):
    #Clic sur le canvas : Remplissage d'un réctangle qui donne la couleur seletionnée.
    global img,valeur_pixel_selct_clic,c1,c2,c3,Info
    valeur_pixel_selct_clic=None #Pas de pixel selectionnés, donc pas de couleur à rendre transparente définie. 
    
    #Si aucune image a été selectionnée, on ouvre l'exploreur de fichier.
    if (img ==0): 
        choosefile()  
        
    #Si image déjà chargée : 
    else :
        Couleur_select.delete(Info)#Suppression du texte d'indication du Canvas Couleur selectionnee
        x, y = event.x, event.y #Selection des coordonées du curseur
        valeur_pixel_selct_clic = calcul_pixel_selctionne(x, y)
        
        #Valeur RGB du pixel selectionné
        c1 = valeur_pixel_selct_clic[0]
        c2 = valeur_pixel_selct_clic[1]
        c3 = valeur_pixel_selct_clic[2]
        
        #convertir les valeurs RGB en Hexa
        convert_RGB_to_BG = "#%02x%02x%02x" % (c1, c2, c3)
        Couleur_select.configure(bg=convert_RGB_to_BG)
        return (convert_RGB_to_BG)

#----If Condition 2
def calcul_pixel_selctionne(x, y):
    #Permet après un clic sur l'image de récuperer la couleur du pixel par proportion
    #La fonction Getpixel se fait sur l'image chargée et non sur le Canvas. Donc qd on clic sur le canvas par proportion on récupère les coordonées du pixel sur l'image chargée. 
    global Largeur_Img_importee, Hauteur_Img_importee,Largeur_Img_IHM, Hauteur_Img_IHM,img
    Largeur_recalculee = int((Largeur_Img_importee/Largeur_Img_IHM)*x)
    Hauteur_recalculee = int((Hauteur_Img_importee/Hauteur_Img_IHM)*y)
    img_convert = img.convert("RGB")
    img_value = img_convert.getpixel((Largeur_recalculee,Hauteur_recalculee))
    #img_value : Couleur du pixel sur l'image chargée, obtenue après clic sur canvas. 
    return(img_value) 

#----If Condition 1
def choosefile():
    global Chemin_fichier,words,chemin_init,Nom_Fichier,Nom_Fichier_final,result,Info
    result = filedialog.askopenfilename(initialdir=chemin_init)
    if(result==''):
        Erreur_Annulation()
    else : 
        Chemin_fichier=result
#-------Permet de revenir sur le dernier chemin ouvert en cas de réutilisation du bouton.
        chemin_init=result 
#-------On prend le nom du fichier qui trouve à la fin du chemin selectionné : 
        words = result.split('/') 
        Nom_Fichier=words[-1] #On prend la dernière valeur qui correspond au nom du fichier
#-------Selection du nom sans extension .png ou .jpg
        Nom_Fichiersplit = result.split('.')
        Nom_Fichier_sans_ext = Nom_Fichiersplit[0]
#-------Nom identique lors de la sauvegadre avec ajout de "- Transparent"
        Nom_Fichier_final= Nom_Fichier_sans_ext + " - Transparent"
#-------Chemin de sauv identique sans prendre le nom du fichier    
        Nom_Chemin = Chemin_fichier[:-len(Nom_Fichier)]  #On prend tt sauf le nom du fichier
        
        Affiche_IMG_selectionnee(result)
        canvas.delete(txt) #Suppression de l'écriture bleu en cas de chargement d'une image transparente
        
        #Visualisation Canvas couleur selectionnée
        Couleur_select.config(highlightthickness=1, highlightbackground="black")
        Info = Couleur_select.create_text(100, 50, text="Cliquez sur l'image", font="Arial 8", fill="black")


#----#----If Condition 1
def Erreur_Annulation():
    messagebox.showinfo("Erreur", "Vous avez annulé")
    
#----#----If Condition 2
def Affiche_IMG_selectionnee(result):
    global new_image, tag,MAJ_image,Largeur_Img_importee, Hauteur_Img_importee,Largeur_Img_IHM, Hauteur_Img_IHM,img

    # Load an image in the script
    img= (Image.open(result))
    Largeur_Img_importee, Hauteur_Img_importee = img.size
    # Resize the Image using resize method
    
    Largeur_Img_IHM = 400
    Hauteur_Img_IHM = 400
    resized_image= img.resize((Largeur_Img_IHM,Hauteur_Img_IHM))
    new_image= ImageTk.PhotoImage(img)
    # Add image to the Canvas Items
    MAJ_image = canvas.create_image(0,0, anchor="nw", image=new_image)
    # canvas.itemconfig(MAJ_image)
    
    
def Fond_Transparent():
    global img,c1,c2,c3, SaveCoordonees
    if (img==0):
        messagebox.showinfo("Erreur", "Selectionnez une image")
    elif(c1==None and c2==None and c3==None):
        messagebox.showinfo("Erreur", "Selectionnez une couleur à rendre transparente en cliquant sur l'image")
    else :
        global Chemin_fichier,words,chemin_init,Nom_Fichier,Nom_Fichier_final
    
        img = Image.open(Chemin_fichier)
        largeur, hauteur = img.size
        print(largeur, hauteur)
        rgba = img.convert("RGBA")
        datas = rgba.getdata()
        newData = []

        # Largeur de la bande verte
        largeur_bande = 2
        couleur_verte = (0, 255, 0, 255)

        # # Coordonnées du coin supérieur gauche du carré
        # x1, y1 = 125, 150
        # # Coordonnées du coin inférieur droit du carré
        # x2, y2 = 175, 175


                # Coordonnées du coin supérieur gauche du carré
        x1, y1 = SaveCoordonees[-2]
        # Coordonnées du coin inférieur droit du carré
        x2, y2 = SaveCoordonees[-1]

        print("x1: ",x1," y1: ",y1)
        print("x2: ",x2," y2: ",y2)

        # Parcourir les pixels de l'image
        for y in range(hauteur):
            for x in range(largeur):
                # Vérifier si le pixel est à l'intérieur du carré
                if x1 <= x <= x2 and y1 <= y <= y2:
                    newData.append(couleur_verte)  # Ajouter la couleur verte
                else:
                    # Si le pixel n'est pas à l'intérieur du carré, ajouter le pixel d'origine
                    pixel = img.getpixel((x, y))
                    newData.append(pixel)

        # Créer une nouvelle image avec les nouvelles données
        img.putdata(newData)

        # Sauvegarder l'image
        img.save(Nom_Fichier_final+".png", "PNG")
        

    
def Couleur_du_fond_mvt_canvas():
    global valeur_pixel_selct_mvt

    if(valeur_pixel_selct_mvt==None):
        messagebox.showinfo("Choix couleur", "Selctionnez une couleur de transparence")
    else : 
        i1 = valeur_pixel_selct_mvt[0]
        i2 = valeur_pixel_selct_mvt[1]
        i3 = valeur_pixel_selct_mvt[2]
    return [i1,i2,i3]
        

    
def motion_on_canvas(event):
    #Mvt de souris sur l'image : création d'un carré bleu de la couleur du pixel que pointe la souris
    global img,valeur_pixel_selct_mvt
    valeur_pixel_selct_mvt=None
    if (img ==0):
        choosefile()        
    else :
        x, y = event.x, event.y
        # print("x: ", x, "y: ",y)
        valeur_pixel_selct_mvt = calcul_pixel_selctionne(x, y)
        
        [i1,i2,i3] = Couleur_du_fond_mvt_canvas()
        convert_RGB_to_BG = "#%02x%02x%02x" % (i1, i2, i3)
        return (convert_RGB_to_BG)
            
def motion(event):
    global init,myrect,img
    if (img !=0): #Que si une image est chargée
        if(init==1):
            convert_RGB_to_BG=motion_on_canvas(event)
            canvas.delete(myrect) #Deletes the rectangle
            x, y = event.x, event.y
            myrect = canvas.create_rectangle(x,y,x-20,y-20,outline="#f11", fill=convert_RGB_to_BG, width=1)
        else: 
            x, y = event.x, event.y
            myrect = canvas.create_rectangle(x-10,y-10,x+10,y+10,outline="#f11", fill="#1f1", width=2)
            init=1
    
def clic_droit(event):
    global SaveCoordonees
    x = event.x
    y = event.y
    print("Clic droit à la position (x={}, y={})".format(x, y))
    SaveCoordonees.append([x, y])
    print(SaveCoordonees)

def on_canvas_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

import tkinter as tk
from tkinter import Button, Canvas



root = tk.Tk() # Création de la fenêtre
root.geometry("700x650") # Taille de la fenêtre
root.resizable(width=False, height=False) # Blocage de la taille de la fenêtre

# CANVAS
canvas = tk.Canvas(root, width=400, height=400, highlightthickness=1, highlightbackground="black")  
canvas.pack(side="left", fill="both", expand=True)
txt = canvas.create_text(200, 200, text="Selectionnez une image", font="Arial 16 italic", fill="blue")
canvas.bind("<Button-1>", click_on_canvas)
x_scrollbar = tk.Scrollbar(canvas, orient="horizontal", command=canvas.xview)
x_scrollbar.pack(side="bottom", fill="x")
y_scrollbar = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
y_scrollbar.pack(side="right", fill="y")
canvas.config(xscrollcommand=x_scrollbar.set, yscrollcommand=y_scrollbar.set)
canvas.bind("<Configure>", on_canvas_configure)
canvas.bind('<Motion>', motion)
canvas.bind("<Button-3>", clic_droit)

# BOUTONS
Bouton_Selec_image = tk.Button(root, text="Selectionner fichier", command=choosefile)
Bouton_Selec_image.pack(side="top", fill="x")

Bouton_Quitter = Button(root, text="Quitter", command=root.destroy)
Bouton_Quitter.pack(side="top", fill="x")

Bouton_Validation = tk.Button(root, text="Valider", command=Fond_Transparent)
Bouton_Validation.pack(side="top", fill="x")

# CANVAS COULEUR SELECTIONEE
Couleur_select = Canvas(root, width=10, height=10) 
Couleur_select.pack(side="bottom", fill="x")

root.mainloop()
