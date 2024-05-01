from imports import *
from PIL import Image
from PIL import ImageTk  

def init_values():
    global img, PlacementUniqueZoom, Position_x_recalculee_BtnsZoom, Zoomincrementation, liste_coordonnees_rectangle, rectangles, current_rectangle, start_x, start_y
    img = None
    PlacementUniqueZoom = 0 #
    Position_x_recalculee_BtnsZoom = 0 
    Zoomincrementation = 0
    liste_coordonnees_rectangle = [] 
    rectangles = [] # Store rectangle's id
    current_rectangle = None # Store current rectangle's id
    start_x = None #Store first clic x locatoin
    start_y = None #Store first clic y locatoin

#Allows to displays print to debug
debug = 1
def test():
    print("test")

# When left clik on mouse,  start rectangle creation
def start_rectangle(event):
    global start_x, start_y, current_rectangle
    start_x = event.x + canvas.canvasx(0)
    start_y = event.y + canvas.canvasy(0)
    current_rectangle = canvas.create_rectangle(start_x, start_y, start_x, start_y, outline="red", fill="black")

# Update rectangle position during mouse mouvments
def update_rectangle(event):
    global start_x, start_y, current_rectangle
    if start_x is not None and start_y is not None:
        x_image = event.x + canvas.canvasx(0)
        y_image = event.y + canvas.canvasy(0)
        canvas.coords(current_rectangle, start_x, start_y, x_image, y_image)

# Finish rectangle build when left click is released
def end_rectangle(event):
    global start_x, start_y, rectangles, current_rectangle,liste_coordonnees_rectangle
    if start_x is not None and start_y is not None:
        x_image = event.x + canvas.canvasx(0)
        y_image = event.y + canvas.canvasy(0)
        rectangles.append(current_rectangle)
        start_x, start_y,x_image,y_image = FixValues(start_x, start_y,x_image,y_image)
        liste_coordonnees_rectangle.append([start_x, start_y,x_image,y_image])
        print((liste_coordonnees_rectangle) if debug==1 else "")
    start_x = None
    start_y = None

#Fix issue if you created your rectangle from bottom to top (wihtout this function rectangle won't appears on save pictures)
def FixValues(start_x, start_y, x_image, y_image):
    if start_x > x_image:
        start_x, x_image = x_image, start_x
    if start_y > y_image:
        start_y, y_image = y_image, start_y
    return start_x, start_y, x_image, y_image

##-------Not in this milestone Scope, will be used later to calculate rectangle new siez and position depending on zoom
# def resize_image():
#     global img, photo
#     new_width = img.width // 2
#     new_height = img.height // 2
#     img = img.resize((new_width, new_height))
#     photo = ImageTk.PhotoImage(img)
#     canvas.config(width=new_width, height=new_height)
#     canvas.itemconfig(MAJ_image, image=photo)
#     update_rectangles_positions(new_width, new_height)

##-------Not in this milestone Scope, will be used later to calculate rectangle new siez and position depending on zoom
# def update_rectangles_positions(state_ratio_zoom):
#     for rectangle_id in rectangles:
#         coords = canvas.coords(rectangle_id)
#         new_coords = [coords[i] * state_ratio_zoom for i in range(4)]
#         canvas.coords(rectangle_id, *new_coords)

def reset():
    global img, photo_image, resized_image

    global ZoomLevel
    img = None
    global img, photo_image, resized_image,Reduction_ratio
    init_values()
    photo_image = None
    resized_image = None
    Reduction_ratio

    Btn_SelectFileTab2.config(state="normal")
    Btn_ResetTab2.config(state="disabled")
    canvas.delete("all")

    hide_scrollbars()
    #------BUTTON ZOOM +  ARE RESETED
    Boutons_Zoom[0][0].configure(state=tk.DISABLED)
    Boutons_Zoom[1][0].configure(state=tk.DISABLED)
    Boutons_ControleTab2[1][0].configure(state=tk.DISABLED)

def remplacer_pixels_rectangles(image, liste_coordonnees):
    for coordonnees in liste_coordonnees:
        x1, y1, x2, y2 = coordonnees
        
        #If picture is narrower than canvas, we do not apply recalculation of the rectangles positions
        if int(Reduction_ratio) != 0: x1, y1, x2, y2 = [int(coord * Reduction_ratio) for coord in (x1, y1, x2, y2)]
        # Loop de replace pixels under rectangles
        for x in range(int(x1), int(x2) + 1):
            for y in range(int(y1), int(y2) + 1):
                # modify pixels by black pixels
                image.putpixel((x, y), (0, 0, 0))  # Met les pixels en vert
    return image

def Save():
    global img
    if (img is None):
        messagebox.showinfo("Erreur", "Selectionnez une image")
    else :
        global Chemin_fichier,Nom_Fichier_final, photo_image
        imgForSaving = Image.open(Chemin_fichier)
        largeur, hauteur = imgForSaving.size
        print((largeur, hauteur) if debug == 1 else "")

        imgForSaving = remplacer_pixels_rectangles(img, liste_coordonnees_rectangle)
        imgForSaving.save(Nom_Fichier_final+".png", "PNG")

#Function Zoom is called when both button zoom + or button -. They send "*" or // depend on zoom + or zoom -
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
        if(Zoomincrementation<=-2):
            Boutons_Zoom[0][0].configure(state=tk.NORMAL)
            Boutons_Zoom[1][0].configure(state=tk.DISABLED)
        elif(Zoomincrementation>=6):
            Boutons_Zoom[0][0].configure(state=tk.DISABLED)
            Boutons_Zoom[1][0].configure(state=tk.NORMAL)
        else:
            Boutons_Zoom[0][0].configure(state=tk.NORMAL)
            Boutons_Zoom[1][0].configure(state=tk.NORMAL)

        # Redimensionner l'image
        print("Zoomincrementation: ",Zoomincrementation)
        Zoomedimg = img.resize((Best_Width_Picture, Best_Height_Picture))
        largeur_img, hauteur_img = Zoomedimg.size
    global ZoomLevel
    if img is not None:
        if(op == "//"):
            Best_Width_Picture = Best_Width_Picture // 2 
            Best_Height_Picture = Best_Height_Picture // 2
            ZoomLevel = ZoomLevel - 1
            

        elif(op=="*"):
            Best_Width_Picture = Best_Width_Picture * 2 
            Best_Height_Picture = Best_Height_Picture * 2 
            ZoomLevel = ZoomLevel + 1 
        
        # Redimensionner l'image
        print(ZoomLevel)
        if(ZoomLevel<=-1):
            Boutons_Zoom[0][0].configure(state=tk.NORMAL)
            Boutons_Zoom[1][0].configure(state=tk.DISABLED)
        elif(ZoomLevel>=3):
            Boutons_Zoom[0][0].configure(state=tk.DISABLED)
            Boutons_Zoom[1][0].configure(state=tk.NORMAL)
        else:
            Boutons_Zoom[0][0].configure(state=tk.NORMAL)
            Boutons_Zoom[1][0].configure(state=tk.NORMAL)
            
        img = img.resize((Best_Width_Picture, Best_Height_Picture))
        largeur_img, hauteur_img = img.size
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

    #Get selected picture size.
    largeur_img, hauteur_img = img.size

    #Calculate how to ajust the picture size in the UI
    Reduction_ratio = (largeur_img/Tab2DisplayWindow_width)
    # Zoomincrementation = Reduction_ratio
    print(("Reduction_ratio brut : ",Reduction_ratio) if debug ==1 else "")
    print(("Reduction_ratio int() : ",int(Reduction_ratio)) if debug ==1 else "")
    #If picture width is already smaller than table width, picture size is not modifed.
    if int(Reduction_ratio)==0:
        Best_Width_Picture = largeur_img 
        Best_Height_Picture = hauteur_img
    #Else Picture is ajusted
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

    #-------Selection du nom sans extension .png ou .jpg
        Nom_Fichiersplit = result.split('.')
        Nom_Fichier_sans_ext = Nom_Fichiersplit[0]
    #-------Nom identique lors de la sauvegadre avec ajout de "- Transparent"
        Nom_Fichier_final= Nom_Fichier_sans_ext + " - Obfuscated"

        Affiche_IMG_selectionnee(result)
        canvas.delete(txt) #Suppression de l'écriture bleu en cas de chargement d'une image transparente
        ScrollBarLenghCalculation()
        show_scrollbars()

        Boutons_Zoom[0][0].configure(state=tk.NORMAL)
        Boutons_Zoom[1][0].configure(state=tk.NORMAL)
        Boutons_ControleTab2[1][0].configure(state=tk.NORMAL)
        #Disable zoom For current Milestone
        Boutons_Zoom[0][0].configure(state=tk.DISABLED)
        Boutons_Zoom[1][0].configure(state=tk.DISABLED)

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
    init_values()
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
    img_ExitTab2 = PhotoImage(file=resource_path("Pictures/Exit.png"))
    img_TestTab2 = PhotoImage(file=resource_path("Pictures/test.png"))
    img_Reset = PhotoImage(file=resource_path("Pictures/Reset.png"))
    
    Btn_SelectFileTab2 = tk.Button(tab2) ; Btn_ValiderTab2 = tk.Button(tab2) 
    Btn_TestTab2 = tk.Button(tab2) ; Btn_ResetTab2=tk.Button(tab2)
    Btn_QuitterTab2 = tk.Button(tab2) 

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
    print(("Position_x_recalculee_BtnsZoom :", Position_x_recalculee_BtnsZoom) if debug == 1 else "")

    canvas.bind("<MouseWheel>", on_mousewheel)
    canvas.bind("<Button-2>", deplacement_horizontal)
    canvas.bind("<B2-Motion>", deplacement_souris)
    canvas.bind("<Motion>", update_rectangle)
    canvas.bind("<Button-1>", start_rectangle)
    canvas.bind("<ButtonRelease-1>", end_rectangle)

    return tab2
    