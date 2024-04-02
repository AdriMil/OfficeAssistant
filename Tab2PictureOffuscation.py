from imports import *
from PIL import Image
from PIL import ImageTk  

img = None
PlacementUniqueZoom = 0 #
Position_x_recalculee_BtnsZoom = 0 
c1=c2=c3=None # Used for pixel coloration
SaveCoordonees = []
Zoomincrementation = 0

def test():
    print("test")

def on_canvas_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
# def click_on_canvas(event):
#     choosefile()

def reset():
    global img, photo_image, resized_image
    img = None
    photo_image = None
    resized_image = None

    Btn_SelectFileTab2.config(state="normal")
    Btn_ResetTab2.config(state="disabled")
    canvas.delete("all")

    hide_scrollbars()

    Boutons_Zoom[0][0].configure(state=tk.DISABLED)
    Boutons_Zoom[1][0].configure(state=tk.DISABLED)
    Boutons_ControleTab2[1][0].configure(state=tk.DISABLED)

def clic_droit(event):
    global SaveCoordonees
    x = event.x
    y = event.y
    # Convertir les coordonnées du canevas en coordonnées relatives à l'image
    x_image = canvas.canvasx(x)
    y_image = canvas.canvasy(y)

    SaveCoordonees.append([x_image, y_image])
    print("Clic droit à la position (x={}, y={})".format(x_image, y_image))
    x2, y2 = CalculateRealPixelPosition(*SaveCoordonees[-1])

    print(SaveCoordonees)

def CalculateRealPixelPosition(x,y):
    if(Zoomincrementation==0):
        x = x *(Reduction_ratio)
        y = y *(Reduction_ratio)
    elif(Zoomincrementation<0):
        x = x *(Reduction_ratio+(2**(-Zoomincrementation)))
        y = y *(Reduction_ratio+(2**(-Zoomincrementation)))
    else:
        x = x *(Reduction_ratio/Zoomincrementation)
        y = y *(Reduction_ratio/Zoomincrementation)  


    # print("ancien x: ",x,"ancien y: ",y)
    print("nouveau x: ",x,"nouveua y: ",y)
    return x,y



def Save():
    # global img,c1,c2,c3, SaveCoordonees
    global img
    if (img is None):
        messagebox.showinfo("Erreur", "Selectionnez une image")
    # elif(c1==None and c2==None and c3==None):
    #     messagebox.showinfo("Erreur", "Selectionnez une couleur à rendre transparente en cliquant sur l'image")
    else :
        global Chemin_fichier,words,chemin_init,Nom_Fichier,Nom_Fichier_final
    
        imgForSaving = Image.open(Chemin_fichier)
        largeur, hauteur = imgForSaving.size
        print(largeur, hauteur)
        rgba = imgForSaving.convert("RGBA")
        datas = rgba.getdata()
        newData = []

        # Largeur de la bande verte
        largeur_bande = 2
        couleur_verte = (0, 255, 0, 255)


                # Coordonnées du coin supérieur gauche du carré
        # x1, y1 = SaveCoordonees[-2]
        x1, y1 = CalculateRealPixelPosition(*SaveCoordonees[-2])
        # Coordonnées du coin inférieur droit du carré
        # x2, y2 = SaveCoordonees[-1]
        x2, y2 = CalculateRealPixelPosition(*SaveCoordonees[-1])
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
                    pixel = imgForSaving.getpixel((x, y))
                    newData.append(pixel)

        # Créer une nouvelle image avec les nouvelles données
        imgForSaving.putdata(newData)
        # Sauvegarder l'image
        imgForSaving.save(Nom_Fichier_final+".png", "PNG")

def Zoom(op):
    global img, largeur_img, hauteur_img, canvas, MAJ_image, photo_image
    global Best_Height_Picture,Best_Width_Picture #share new size of picture
    global Zoomincrementation,ratioZoom #know zoom on picture
    ratioZoom=2
    
    if img is not None:
        if(op == "//"):
            Zoomincrementation = Zoomincrementation  - 2
            Best_Width_Picture = Best_Width_Picture // ratioZoom 
            Best_Height_Picture = Best_Height_Picture // ratioZoom

        elif(op=="*"):
           
            Zoomincrementation = Zoomincrementation  + 2
            
            Best_Width_Picture = Best_Width_Picture * ratioZoom 
            Best_Height_Picture = Best_Height_Picture * ratioZoom 
        
        # Redimensionner l'image
        print("Zoomincrementation: ",Zoomincrementation)
        Zoomedimg = img.resize((Best_Width_Picture, Best_Height_Picture))
        largeur_img, hauteur_img = Zoomedimg.size
        print("largeur_img: ", largeur_img,"hauteur_img: ", hauteur_img)

        # Convertir l'image redimensionnée en PhotoImage
        photo_image = ImageTk.PhotoImage(Zoomedimg)

        # Mettre à jour l'image dans le canevas
        canvas.itemconfig(MAJ_image, image=photo_image)
        ScrollBarLenghCalculation()


def Affiche_IMG_selectionnee(result):
    global MAJ_image, canvas, photo_image  # Assurez-vous d'avoir déclaré la variable photo_image comme globale
    global img,photo_image,resized_image, largeur_img, hauteur_img
    global Best_Width_Picture,Best_Height_Picture # Share init size of the picture we are displaying. Values will be use by zooms functions
    global Reduction_ratio,Zoomincrementation # use for pixel selection scalling 
    # Load an image from the file path
    img = Image.open(result)

    largeur_img, hauteur_img = img.size

    Reduction_ratio = (largeur_img/Tab2DisplayWindow_width)
    # Zoomincrementation = Reduction_ratio
    print("Reduction_ratio: ",Reduction_ratio)
    if int(Reduction_ratio)==0:
        Best_Width_Picture = largeur_img 
        Best_Height_Picture = hauteur_img
    else:
        Best_Width_Picture = int(largeur_img // Reduction_ratio)
        Best_Height_Picture = int(hauteur_img // Reduction_ratio)
    resized_image = img.resize((Best_Width_Picture, Best_Height_Picture))

    # Convert the resized image to a PhotoImage object
    photo_image = ImageTk.PhotoImage(resized_image)

    # Add the image to the Canvas
    MAJ_image = canvas.create_image(0, 0, anchor="nw", image=photo_image)
    ScrollBarLenghCalculation()
        
def ScrollBar():
    global x_scroll,y_scroll
        # Add horizontal scrollbar
    x_scroll = tk.Scrollbar(canvas, orient="horizontal", command=canvas.xview)
    canvas.configure(xscrollcommand=x_scroll.set)

    # Add vertical scrollbar
    y_scroll = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=y_scroll.set)

def ScrollBarLenghCalculation():
    canvas.config(scrollregion=canvas.bbox(tk.ALL))

def hide_scrollbars():
    x_scroll.pack_forget()
    y_scroll.pack_forget()

def show_scrollbars():
    x_scroll.pack(side="bottom", fill="x")
    y_scroll.pack(side="right", fill="y")

def deplacement_horizontal(event):
    global last_x, last_y
    last_x = event.x_root
    last_y = event.y_root

def deplacement_souris(event):
    global last_x, last_y
    x = event.x_root
    y = event.y_root
    delta_x = x - last_x
    delta_y = y - last_y
    if delta_x > 0:
        canvas.xview_scroll(-1, "units")  # Défilement vers la gauche
    elif delta_x < 0:
        canvas.xview_scroll(1, "units")   # Défilement vers la droite
    if delta_y > 0:
        canvas.yview_scroll(-1, "units")  # Défilement vers le haut
    elif delta_y < 0:
        canvas.yview_scroll(1, "units")   # Défilement vers le bas
    last_x = x
    last_y = y

def on_mousewheel(event):
    if event.delta > 0:
        canvas.yview_scroll(-1, "units")  # Défilement vers le haut
    else:
        canvas.yview_scroll(1, "units")   # Défilement vers le bas
    

def choosefile():
    global canvas, txt,tab2SelectedImg,Btn_ResetTab2,Btn_SelectFileTab2
    global PlacementUniqueZoom #Know if zoom btns have already been positionned
    global Chemin_fichier,Nom_Fichier_final # use for save function
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
        Nom_Fichier_final= Nom_Fichier_sans_ext + " - Obfuscated"
    #-------Chemin de sauv identique sans prendre le nom du fichier    
        Nom_Chemin = Chemin_fichier[:-len(Nom_Fichier)]  #On prend tt sauf le nom du fichier
        
        Affiche_IMG_selectionnee(result)
        canvas.delete(txt) #Suppression de l'écriture bleu en cas de chargement d'une image transparente
        ScrollBarLenghCalculation()
        show_scrollbars()

        Boutons_Zoom[0][0].configure(state=tk.NORMAL)
        Boutons_Zoom[1][0].configure(state=tk.NORMAL)
        Boutons_ControleTab2[1][0].configure(state=tk.NORMAL)

        if (PlacementUniqueZoom == 0 ): #Bloquer la repetitiuon d'ajoute  des boutons zoom
                PlaceBtnsZoom()
                PlacementUniqueZoom = 1

def CalculPositionInitialeBoutonsZoom():
    global Position_x_recalculee_BtnsZoom
    NbBtn = len(Boutons_Zoom)
    EspacePrisParLesBoutonsZoom = NbBtn * (Btn_zoom_width+Space_Between_Btn_zoom)
    freeSpace = Tab2DisplayWindow_width - (EspacePrisParLesBoutonsZoom)
    if(freeSpace>0):
        Position_x_recalculee_BtnsZoom = Tab2DisplayWindow_x_position + (freeSpace / 2)

    else:
        debord = EspacePrisParLesBoutonsZoom - Tab2DisplayWindow_x_position
        Position_x_recalculee_BtnsZoom = Tab2DisplayWindow_x_position - (debord / 2)

    return Position_x_recalculee_BtnsZoom

def PlaceBtnsZoom():
    global Position_x_recalculee_BtnsZoom
    for i in range(0,len(Boutons_Zoom)):
        Boutons_Zoom[i][2] = Boutons_Zoom[i][2].subsample(ImageReducer, ImageReducer) #Réduction de la taille de l'image
        Boutons_Zoom[i][0].configure( width=Btn_zoom_width, height= Btn_zoom_height,image=Boutons_Zoom[i][2], command=Boutons_Zoom[i][3])
        Boutons_Zoom[i][0].place(x=Position_x_recalculee_BtnsZoom, y=Btn_zoom_y_init)
        Position_x_recalculee_BtnsZoom = Position_x_recalculee_BtnsZoom + Btn_zoom_width + Space_Between_Btn_zoom
        Boutons_Zoom[i].append(Position_x_recalculee_BtnsZoom) #Sauvegarde de la valeur x du bouton à la fin de la liste
        Boutons_Zoom[i].append(Btn_zoom_y_init) #Sauvegarde de la valeur y du bouton à la fin de la liste

def Tab2PictureOffuscation(master,root):
    global canvas, txt
    global Btn_ResetTab2,Btn_SelectFileTab2
    global tab2
    global Boutons_Zoom,Position_x_recalculee_BtnsZoom
    global Boutons_ControleTab2 # Used to active or disable button depend on UI actions
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

    ScrollBar()
    Boutons_ControleTab2 = [
        [Btn_SelectFileTab2, "Add file",img_SelectFileTab2, choosefile,tk.NORMAL ],
        [Btn_ValiderTab2, "Valider",img_ValiderTab2, Save,tk.DISABLED],
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


    
    img_Zoom_Plus = PhotoImage(file=resource_path("Pictures/zoomPlus.png"))
    img_Zoom_Moins = PhotoImage(file=resource_path("Pictures/zoomMoins.png"))
    Btn_ZoomPlus = tk.Button(tab2) ; Btn_ZoomMoins = tk.Button(tab2) 

    Boutons_Zoom = [
        [Btn_ZoomPlus, "Zoomer",img_Zoom_Plus, lambda: Zoom("*") ],
        [Btn_ZoomMoins, "Dézoomer",img_Zoom_Moins, lambda: Zoom("//")],
    ]

    Position_x_recalculee_BtnsZoom = CalculPositionInitialeBoutonsZoom()
    print("Position_x_recalculee_BtnsZoom :", Position_x_recalculee_BtnsZoom)

    # root.bind("<MouseWheel>", lambda event: ZoomMoletteUp(event) if event.delta > 0 else ZoomMoletteDown(event))

    canvas.bind("<MouseWheel>", on_mousewheel)
    # Associer la fonction à l'événement de clic de la molette de la souris
    canvas.bind("<Button-2>", deplacement_horizontal)
    # Associer la fonction à l'événement de déplacement de la souris
    canvas.bind("<B2-Motion>", deplacement_souris)

    canvas.bind("<Button-3>", clic_droit)
    return tab2
    