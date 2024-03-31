from imports import *
from PIL import Image
from PIL import ImageTk  

def test():
    print("test")

# def click_on_canvas(event):
#     choosefile()

def reset():
    global tab2SelectedImg,Btn_SelectFileTab2,Btn_ResetTab2
    Btn_SelectFileTab2.config(state="normal")
    Btn_ResetTab2.config(state="disabled")
    canvas.delete("all")


def Affiche_IMG_selectionnee(result):
    global MAJ_image, canvas, photo_image  # Assurez-vous d'avoir déclaré la variable photo_image comme globale

    # Load an image from the file path
    img = Image.open(result)

    # Resize the image
    Largeur_Img_IHM = 400
    Hauteur_Img_IHM = 400
    resized_image = img.resize((Largeur_Img_IHM, Hauteur_Img_IHM))

    # Convert the resized image to a PhotoImage object
    photo_image = ImageTk.PhotoImage(resized_image)

    # Add the image to the Canvas
    MAJ_image = canvas.create_image(0, 0, anchor="nw", image=photo_image)


    

def choosefile():
    global canvas, txt,tab2SelectedImg,Btn_ResetTab2,Btn_SelectFileTab2
    result = filedialog.askopenfilename()
    if(result==''):
        print("pas d'image selectionnées")
        tab2SelectedImg = 0 
        Btn_ResetTab2.config(state="disabled")
    
    else : 
        Btn_ResetTab2.config(state="normal")
        Btn_SelectFileTab2.config(state="disabled")
        tab2SelectedImg = 1 
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
        


def Tab2PictureOffuscation(master,root):
    global canvas, txt
    global Btn_ResetTab2,Btn_SelectFileTab2
    global tab2
    tab2 = ttk.Frame(master)

    canvas = tk.Canvas(tab2, bg="white")
    canvas.place(x=Tab2DisplayWindow_x_position, y=Tab2DisplayWindow_y_position,width=Tab2DisplayWindow_width, height=Tab2DisplayWindow_Height)

    img_SelectFileTab2 = PhotoImage(file=resource_path("Pictures/AddFile.png"))
    img_ValiderTab2 = PhotoImage(file=resource_path("Pictures/Valider.png"))
    img_ConvertTab2 = PhotoImage(file=resource_path("Pictures/ConvertInPdf.png"))
    img_ExitTab2 = PhotoImage(file=resource_path("Pictures/Exit.png"))
    img_TestTab2 = PhotoImage(file=resource_path("Pictures/test.png"))
    img_Reset = PhotoImage(file=resource_path("Pictures/Reset.png"))
    
    Btn_SelectFileTab2 = tk.Button(tab2) ; Btn_ValiderTab2 = tk.Button(tab2) 
    Btn_ConvertirTab2 = tk.Button(tab2) ; Btn_QuitterTab2 = tk.Button(tab2) 
    Btn_TestTab2 = tk.Button(tab2) ; Btn_ResetTab2=tk.Button(tab2)

    canvas = tk.Canvas(tab2, highlightthickness=1, highlightbackground="black")
    canvas.place(x=Tab2DisplayWindow_x_position, y=Tab2DisplayWindow_y_position,width=Tab2DisplayWindow_width, height=Tab2DisplayWindow_Height)
    # canvas.bind("<Button-1>", click_on_canvas)
    txt = canvas.create_text(300, 200, text="Selectionnez une image", font="Arial 16 italic", fill="blue")

    Boutons_ControleTab2 = [
        [Btn_SelectFileTab2, "Add file",img_SelectFileTab2, choosefile,tk.NORMAL ],
        [Btn_ValiderTab2, "Valider",img_ValiderTab2, test,tk.DISABLED],
        # [Btn_ConvertirTab2, "Convertir",img_ConvertTab2, test,tk.DISABLED],
        [Btn_ResetTab2, "Reset",img_Reset, reset,tk.DISABLED],
        [Btn_QuitterTab2, "Quitter",img_ExitTab2, root.destroy,tk.NORMAL],
        
        # [Btn_TestTab2, "Test",img_Test, HideProcessing, tk.NORMAL],
    ]

    # Boucle placement des bouttons
    Position_x_recalculeeTab2,Position_y_recalculeeTab2 = CalculPositionInitialeBoutonsDeControl(Boutons_ControleTab2,Tab2Canvas,offset=30)
    
#font=("Helvetica", policeSize),image=Boutons_ControleTab2[i][2], command=Boutons_ControleTab2[i][3], text = Boutons_ControleTab2[i][1],compound=tk.TOP,state=Boutons_ControleTab2[i][4] )
    Btn_QuitterTab2.config(width=25, height= 25,command=test, image=img_ExitTab2)
    Btn_QuitterTab2.image = img_ExitTab2
    Btn_QuitterTab2.place(x=50, y=50)

    for i in range(0,len(Boutons_ControleTab2)):
        Boutons_ControleTab2[i][2] = Boutons_ControleTab2[i][2].subsample(1, 1) #Réduction de la taille de l'image
        Boutons_ControleTab2[i][0].configure( width=Btn_controle_width, height= Btn_controle_height, font=("Helvetica", policeSize),image=Boutons_ControleTab2[i][2], command=Boutons_ControleTab2[i][3], text = Boutons_ControleTab2[i][1],compound=tk.TOP,state=Boutons_ControleTab2[i][4] )
        Boutons_ControleTab2[i][0].image = Boutons_ControleTab2[i][2]
        Boutons_ControleTab2[i][0].place(x=Position_x_recalculeeTab2, y=Position_y_recalculeeTab2)
        Position_x_recalculeeTab2 = Position_x_recalculeeTab2 + Btn_controle_width + Space_Between_Btn
        Boutons_ControleTab2[i].append(Position_x_recalculeeTab2) #Sauvegarde de la valeur x du bouton à la fin de la liste
        Boutons_ControleTab2[i].append(Position_y_recalculeeTab2) #Sauvegarde de la valeur y du bouton à la fin de la liste

    return tab2
    