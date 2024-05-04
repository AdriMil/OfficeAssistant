from SharedFunctions.imports import *

#-------------------INIT-----------#
Chemin=''
liste_chemin=[]
Nom_Fichier = []
chemin_final=''
Images_Multiple=[]
IMG_Mult=[]
files = None
PlacementUniqueFleche = 0 #Permet de ne placer qu'une fois les boutons fleches
All_data_in_tableau = []
liste_chemin_update=[]
index_from_selected_ligne = 0 # Select first line when files are imported for 1st time 

#----------------SEND VALUES TO MAIN Windows-----------------#
def WindowsSizeSendData():
    global window_height, window_width
    return window_height,window_width
#-------------------------------------------------------------


def ArrowButtons_InitPositionCalculation():
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

def ArrowButtons_PlaceOnUi():
    global Boutons_Fleche,ImageReducer,Btn_fleche_width,Btn_fleche_height,policeSize,Position_x_recalculee_BtnsFleche,Btn_fleche_y_init,Space_Between_Btn_fleche
    for i in range(0,len(Boutons_Fleche)):
        Boutons_Fleche[i][2] = Boutons_Fleche[i][2].subsample(ImageReducer, ImageReducer) #Réduction de la taille de l'image
        Boutons_Fleche[i][0].configure( width=Btn_fleche_width, height= Btn_fleche_height,image=Boutons_Fleche[i][2], command=Boutons_Fleche[i][3])
        Boutons_Fleche[i][0].place(x=Position_x_recalculee_BtnsFleche, y=Btn_fleche_y_init)
        Position_x_recalculee_BtnsFleche = Position_x_recalculee_BtnsFleche + Btn_fleche_width + Space_Between_Btn_fleche
        Boutons_Fleche[i].append(Position_x_recalculee_BtnsFleche) #Sauvegarde de la valeur x du bouton à la fin de la liste
        Boutons_Fleche[i].append(Btn_fleche_y_init) #Sauvegarde de la valeur y du bouton à la fin de la liste

def ChooseMultiFile():
    global files,PlacementUniqueFleche, index_from_selected_ligne,Btn_Reset,tableau
    files = filedialog.askopenfilenames(title="Sélectionner plusieurs fichiers", filetypes=(("Images PNG", "*.png"), ("Images JPEG", "*.jpg"),("Images HEIC", "*.heic")))
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
            ArrowButtons_PlaceOnUi()
            PlacementUniqueFleche = 1
        DisableButtonIfNecessery()

    else:
        Error_Cancelation()

def OpenDialogToSavePdf():
    user_input = simpledialog.askstring("Nommez votre fichier ", "Nom du fichier :")
    if user_input is None:
        print("L'utilisateur a cliqué sur Cancel.")
    elif user_input:
        FileName = user_input
        ConvertPictureToPdf(FileName)
    else:
        messagebox.showinfo("Erreur", "Donnez un titre au document qui va être créé")
        OpenDialogToSavePdf()


def ConvertPictureToPdf(FileName):
    global liste_chemin_update
    if (liste_chemin_update == []):
        GetFilesPathList()

    SavePath()
    chemin_final = Chemin
    if(chemin_final==''):               #Verif si un chemin final est indiqué
        Error_BadSavePath()
    elif(len(liste_chemin)==0):         #Verif si au moins une image est selctionnée
        Error_NoPicture()

    else:                               #Si plusieurs images à convertir
        # TraitementConversion.place(x=Tableau_x_position + 1, y=Tableau_y_position + 24, width=Tableau_width, height=Tableau_Height)
        DisplayProcessing()
        PicturesProcessing(liste_chemin_update, FileName, chemin_final)
        Info_ProcessFinished(liste_chemin_update,FileName,chemin_final)


def Reset():
    User_Answer=INfo_Reset()
    if User_Answer == 'yes':
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
    Position_x_recalculee_BtnsFleche = ArrowButtons_InitPositionCalculation() #Permet de reset la position des btns et donc d'éviter un décallage des btns à chaque reset

    #REset List of data
    files = []
    All_data_in_tableau = []
    liste_chemin_update=[]
    FileName= []
    chemin_final = []
    #REset displayed data in Tableau
    tableau.delete(*tableau.get_children())

def SavePath():
    global Chemin
    Chemin = filedialog.askdirectory()

def DisplaySelectedLineContent(event):
    global files, index_from_selected_ligne
    if files:
        item = tableau.selection()[0]
        contenu_ligne = tableau.item(item, 'values')
        index_from_selected_ligne = int(contenu_ligne[0])
        DisableButtonIfNecessery()

def UpdateTable():
    global tableau
    # Effacer toutes les lignes actuelles du tableau
    for row in tableau.get_children():
        tableau.delete(row)
    # Réinsérer les données mises à jour
    for data in All_data_in_tableau:
        tableau.insert('', 'end', values=data)
    GetFilesPathList()

def GetFilesPathList():
    global All_data_in_tableau,liste_chemin_update,liste_chemin
    liste_chemin_update=[]
    liste_chemin_update = [element[2] for element in All_data_in_tableau]
    liste_chemin = liste_chemin_update

def ButtonArrowDownAction():
    global index_from_selected_ligne,All_data_in_tableau
    if (index_from_selected_ligne is not None):
        ChangePlaceDown(All_data_in_tableau,index_from_selected_ligne)
        UpdateTable()
        index_from_selected_ligne += 1
        NextLineToBeAutoSelected("Down")

def ButtonArrowUpAction():
    global index_from_selected_ligne,All_data_in_tableau
    if (index_from_selected_ligne is not None):
        ChangePlaceUp(All_data_in_tableau,index_from_selected_ligne)
        UpdateTable()
        index_from_selected_ligne -= 1
        NextLineToBeAutoSelected("Up")

def DeleteTableLines():
    global index_from_selected_ligne,All_data_in_tableau
    DeleteSelectedLine(All_data_in_tableau,index_from_selected_ligne-1)
    UpdateTable()
    GetFilesPathList()
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

def ConvertHeicToPillowFormat(heic_path):
    # Enregistrement du module d'ouverture pour le format HEIC
    register_heif_opener()

    # Ouverture de l'image HEIC et conversion en mode RGB
    with Image.open(heic_path) as im:
        return im.convert("RGB")

def PicturesProcessing(liste_chemin, FileName, chemin_final):
    Images_Multiple = []
    IMG_Mult = []
    incrementation = 0

    for chemin in liste_chemin:
        # Vérifier si le fichier est au format .heic
        _, extension = os.path.splitext(chemin)
        if extension.lower() == '.heic':
            # Convertir .heic en image lisible avec PIL
            img_heic = ConvertHeicToPillowFormat(chemin)
            Images_Multiple.append(img_heic)
        else:
            # Pour les autres formats, ouvrir directement avec PIL
            Images_Multiple.append(Image.open(chemin))

    for img in Images_Multiple:
        incrementation = incrementation + 1 
        # Convertir en mode RGB et ajouter à la liste IMG_Mult
        IMG_Mult.append(img.convert('RGB'))
        texttodisplay = "Image convertie : {} / {}".format(incrementation, len(Images_Multiple))
        UpdateProcessing(texttodisplay)
        
    # Sauvegarder le fichier PDF
    UpdateProcessing("Enregistrement du PDF")
    UpdateProcessing("...")
    nom = os.path.join(chemin_final, f"{FileName}.pdf")
    IMG_Mult[0].save(nom, save_all=True, append_images=IMG_Mult[1:])
    UpdateProcessing("PDF enregistré")
    HideProcessing()

def DisplayProcessing():
    global cadre, texte, ascenseur, bouton_cacher, tab1
    
    cadre = tk.Frame(tab1,borderwidth=1, relief="solid")
    cadre.place(x=Tableau_x_position, y=Tableau_y_position, width=Tableau_width, height=Tableau_Height+25)
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

def PdfCreatorTab(master,root):

    global tab1
    tab1 = ttk.Frame(master)
    
    global Btn_SelectFile,Btn_Reset,Btn_Quitter,Btn_Convertir,Btn_Test,Boutons_Controle,Boutons_Fleche,tableau,Btn_FlecheHaut ,Btn_FlecheBas, Btn_SupprimerLigne 
    global TraitementConversion,Position_x_recalculee_BtnsFleche
    #----------------------------------------
    #Nom Bouton, Texte, Image, Fonction

    img_SelectFile = PhotoImage(file=resource_path("Pictures/AddFile.png"))
    img_Reset = PhotoImage(file=resource_path("Pictures/Reset.png"))
    img_Convert = PhotoImage(file=resource_path("Pictures/ConvertInPdf.png"))
    img_Exit = PhotoImage(file=resource_path("Pictures/Exit.png"))
    img_Test = PhotoImage(file=resource_path("Pictures/test.png"))

    Btn_SelectFile = tk.Button(tab1) ; Btn_Reset = tk.Button(tab1) ;
    Btn_Convertir = tk.Button(tab1) ; Btn_Quitter = tk.Button(tab1) ;
    Btn_Test = tk.Button(tab1) ;

    Boutons_Controle = [
        [Btn_SelectFile, "Add file",img_SelectFile, ChooseMultiFile,tk.NORMAL ],
        [Btn_Reset, "Reset",img_Reset, Reset,tk.DISABLED],
        [Btn_Convertir, "Convertir",img_Convert, OpenDialogToSavePdf,tk.DISABLED],
        [Btn_Quitter, "Quitter",img_Exit, root.destroy,tk.NORMAL],
        # [Btn_Test, "Test",img_Test, HideProcessing, tk.NORMAL],
    ]

    # Boucle placement des bouttons
    Position_x_recalculee,Position_y_recalculee = CalculPositionInitialeBoutonsDeControl(Boutons_Controle,Tab1Tableau,offset=30)

    for i in range(0,len(Boutons_Controle)):
        Boutons_Controle[i][2] = Boutons_Controle[i][2].subsample(ImageReducer, ImageReducer) #Réduction de la taille de l'image
        Boutons_Controle[i][0].configure( width=Btn_controle_width, height= Btn_controle_height, font=("Helvetica", policeSize),image=Boutons_Controle[i][2], command=Boutons_Controle[i][3], text = Boutons_Controle[i][1],compound=tk.TOP,state=Boutons_Controle[i][4] )
        Boutons_Controle[i][0].place(x=Position_x_recalculee, y=Position_y_recalculee)
        print("--------------------------------------------")
        print(type(Position_x_recalculee))
        print(type(Btn_controle_width))
        print(type(Space_Between_Btn))
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
    tableau.place(x=Tableau_x_position, y=Tableau_y_position, width=Tableau_width, height=Tableau_Height)

    TraitementConversion = tk.Label(tab1, text="", borderwidth=1, relief="solid")

    #----------------------------------------
    #Nom Bouton, Texte, Image, Fonction

    img_Fleche_Haut = PhotoImage(file=resource_path("Pictures/img_Fleche_Haut.png"))
    img_Fleche_Bas = PhotoImage(file=resource_path("Pictures/img_Fleche_Bas.png"))
    img_SupprimerLigne = PhotoImage(file=resource_path("Pictures/Reset.png"))

    Btn_FlecheHaut = tk.Button(tab1) ; Btn_FlecheBas = tk.Button(tab1) ;  Btn_SupprimerLigne = tk.Button(tab1)

    Boutons_Fleche = [
        [Btn_FlecheHaut, "Monter",img_Fleche_Haut, ButtonArrowUpAction ],
        [Btn_SupprimerLigne, "Supprimer",img_SupprimerLigne, DeleteTableLines],
        [Btn_FlecheBas, "Descendre",img_Fleche_Bas, ButtonArrowDownAction],
    ]

    # Boucle placement des bouttons
    Position_x_recalculee_BtnsFleche = ArrowButtons_InitPositionCalculation()

    # Associer la fonction DisplaySelectedLineContent à l'événement de clic sur une ligne
    tableau.bind('<ButtonRelease-1>', DisplaySelectedLineContent)

    return tab1