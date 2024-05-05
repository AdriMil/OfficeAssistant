from SharedFunctions.imports import *

#-------------------INIT-----------#
Chemin=''
Path_List=[]
File_Name = []
Selected_Save_Path=''
Many_Selected_Pictures_List=[]
IMG_Mult=[]
Selected_Files = None
Place_Arrows_Only_Once = 0 #Permet de ne placer qu'une fois les boutons fleches
All_Data_In_Table = []
Files_Paths_Updated_List=[]
Selected_Line_Index = 0 # Select first line when Selected_Files are imported for 1st time 



#----------------SEND VALUES TO MAIN Windows-----------------#
def WindowsSizeSendData():
    global Window_Height, Window_Width
    return Window_Height,Window_Width
#-------------------------------------------------------------


def ArrowButtons_InitPositionCalculation():
    global Table_Width,Arrows_Buttons, Arrows_Buttons_Width,Space_Between_Arrows_Buttons,x_Position_Recalculated_For_Arrows_Buttons, Table_x_Position,Window_Width, Table_Height
    Buttons_Number = len(Arrows_Buttons)
    Spaces_Used_By_Buttons = Buttons_Number * (Arrows_Buttons_Width+Space_Between_Arrows_Buttons)
    Free_Space = Table_Width - (Spaces_Used_By_Buttons)
    if(Free_Space>0):
        x_Position_Recalculated_For_Arrows_Buttons = Table_x_Position + (Free_Space / 2)
        Window_Width = Table_Width + Table_x_Position *2

    else:
        Extra_Buttons_Space = Spaces_Used_By_Buttons - Table_Width
        x_Position_Recalculated_For_Arrows_Buttons = Table_x_Position - (Extra_Buttons_Space / 2)
        Window_Width = Table_Width + Extra_Buttons_Space

    return x_Position_Recalculated_For_Arrows_Buttons

def Arrows_Buttons_Place_On_Ui():
    global Arrows_Buttons,Picture_Reducer_Value,Arrows_Buttons_Width,Arrows_Buttons_Height,Police_Size,x_Position_Recalculated_For_Arrows_Buttons,Arrows_Buttons_Init_y_Position,Space_Between_Arrows_Buttons
    for i in range(0,len(Arrows_Buttons)):
        Arrows_Buttons[i][2] = Arrows_Buttons[i][2].subsample(Picture_Reducer_Value, Picture_Reducer_Value) #Réduction de la taille de l'image
        Arrows_Buttons[i][0].configure( width=Arrows_Buttons_Width, height= Arrows_Buttons_Height,image=Arrows_Buttons[i][2], command=Arrows_Buttons[i][3])
        Arrows_Buttons[i][0].place(x=x_Position_Recalculated_For_Arrows_Buttons, y=Arrows_Buttons_Init_y_Position)
        x_Position_Recalculated_For_Arrows_Buttons = x_Position_Recalculated_For_Arrows_Buttons + Arrows_Buttons_Width + Space_Between_Arrows_Buttons
        Arrows_Buttons[i].append(x_Position_Recalculated_For_Arrows_Buttons) #Sauvegarde de la valeur x du bouton à la fin de la liste
        Arrows_Buttons[i].append(Arrows_Buttons_Init_y_Position) #Sauvegarde de la valeur y du bouton à la fin de la liste

def ChooseMultiFile():
    global Selected_Files,Place_Arrows_Only_Once, Selected_Line_Index,Button_Reset,table
    Selected_Files = filedialog.askopenfilenames(title="Sélectionner plusieurs fichiers", filetypes=(("Images PNG", "*.png"), ("Images JPEG", "*.jpg"),("Images HEIC", "*.heic")))
    if Selected_Files:
        Button_Reset.configure(state=tk.NORMAL); Button_Convert.configure(state=tk.NORMAL)
        for file in Selected_Files:
            Path_List.append(file)
            # print("Liste des chemin selectionnés : ", Path_List)
            words = file.split('/')
            File_Name.append(words[-1]) #On prend la dernière valeur qui correspond au nom du fichier
            table.insert( '', 'end',values=(len(Path_List),words[-1],file))
            All_Data_In_Table.append([len(Path_List),words[-1],file]) #Give list of all data in tab -> will use do modify file order

        if (Place_Arrows_Only_Once == 0 ): #Bloquer la repetitiuon d'ajoute  des boutons fleches
            Arrows_Buttons_Place_On_Ui()
            Place_Arrows_Only_Once = 1
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
    global Path_List_update
    if (Files_Paths_Updated_List == []):
        GetFilesPathList()

    SavePath()
    Selected_Save_Path = Chemin
    if(Selected_Save_Path==''):               #Verif si un chemin final est indiqué
        Error_BadSavePath()
    elif(len(Path_List)==0):         #Verif si au moins une image est selctionnée
        Error_NoPicture()

    else:                               #Si plusieurs images à convertir
        # TraitementConversion.place(x=Table_x_Position + 1, y=Table_y_Position + 24, width=Table_Width, height=Table_Height)
        DisplayProcessing()
        PicturesProcessing(Files_Paths_Updated_List, FileName, Selected_Save_Path)
        Info_ProcessFinished(Files_Paths_Updated_List,FileName,Selected_Save_Path)


def Reset():
    User_Answer=INfo_Reset()
    if User_Answer == 'yes':
        DeleteAlldata()

def DeleteAlldata():
    global Place_Arrows_Only_Once,Selected_Files,All_Data_In_Table,x_Position_Recalculated_For_Arrows_Buttons
    global Files_Paths_Updated_List, Selected_Save_Path
        # Reset Arrows button
    Place_Arrows_Only_Once = 0
    for btn in Arrows_Buttons:
        btn[0].place_forget()

    # Reset btn Reset et convertir
    Button_Reset.configure(state=tk.DISABLED); Button_Convert.configure(state=tk.DISABLED)
    Path_List.clear() #RESET de la liste Path_List
    File_Name.clear() #RESET de la liste File_Name
    x_Position_Recalculated_For_Arrows_Buttons = ArrowButtons_InitPositionCalculation() #Permet de reset la position des btns et donc d'éviter un décallage des btns à chaque reset

    #REset List of data
    Selected_Files = []
    All_Data_In_Table = []
    Files_Paths_Updated_List=[]
    FileName= []
    Selected_Save_Path = []
    #REset displayed data in Tableau
    table.delete(*table.get_children())

def SavePath():
    global Chemin
    Chemin = filedialog.askdirectory()

def DisplaySelectedLineContent(event):
    global Selected_Files, Selected_Line_Index
    if Selected_Files:
        item = table.selection()[0]
        Line_Content = table.item(item, 'values')
        Selected_Line_Index = int(Line_Content[0])
        DisableButtonIfNecessery()

def UpdateTable():
    global table
    # Effacer toutes les lignes actuelles du tableau
    for row in table.get_children():
        table.delete(row)
    # Réinsérer les données mises à jour
    for data in All_Data_In_Table:
        table.insert('', 'end', values=data)
    GetFilesPathList()

def GetFilesPathList():
    global All_Data_In_Table,Files_Paths_Updated_List,Path_List
    Files_Paths_Updated_List=[]
    Files_Paths_Updated_List = [element[2] for element in All_Data_In_Table]
    Path_List = Files_Paths_Updated_List

def ButtonArrowDownAction():
    global Selected_Line_Index,All_Data_In_Table
    if (Selected_Line_Index is not None):
        ChangePlaceDown(All_Data_In_Table,Selected_Line_Index)
        UpdateTable()
        Selected_Line_Index += 1
        NextLineToBeAutoSelected("Down")

def ButtonArrowUpAction():
    global Selected_Line_Index,All_Data_In_Table
    if (Selected_Line_Index is not None):
        ChangePlaceUp(All_Data_In_Table,Selected_Line_Index)
        UpdateTable()
        Selected_Line_Index -= 1
        NextLineToBeAutoSelected("Up")

def DeleteSelectedLineFromTable():
    global Selected_Line_Index,All_Data_In_Table
    DeleteSelectedLine(All_Data_In_Table,Selected_Line_Index-1)
    UpdateTable()
    GetFilesPathList()
    if (len(All_Data_In_Table)==0):
        DeleteAlldata()
    else:
        NextLineToBeAutoSelected("Delete")
        exit

def NextLineToBeAutoSelected(action):
    global Selected_Line_Index,All_Data_In_Table
    if (action == 'Delete'):
        if(Selected_Line_Index==((All_Data_In_Table[-1][0])+1)): #If select line is the last of table
            table.selection_set(table.get_children()[-1]) #Autoselection of new last line after line deletion
            Selected_Line_Index = len(All_Data_In_Table)
        else:
            item_id_NextLine = table.get_children()[Selected_Line_Index-1]
            table.selection_set(item_id_NextLine)
    else:
        table.selection_set(table.get_children()[Selected_Line_Index-1]) #Autoselection of new last line after line deletion
    DisableButtonIfNecessery()

def DisableButtonIfNecessery():
    global Selected_Line_Index
    if((Selected_Line_Index==All_Data_In_Table[0][0]) and (Selected_Line_Index==All_Data_In_Table[-1][0])):
        Button_Arrow_Dow.configure(state=tk.DISABLED)
        Button_Arrow_Up.configure(state=tk.DISABLED)
    elif (Selected_Line_Index==All_Data_In_Table[-1][0]):
        Button_Arrow_Dow.configure(state=tk.DISABLED)
        Button_Arrow_Up.configure(state=tk.NORMAL)
    elif (Selected_Line_Index==All_Data_In_Table[0][0]):
        Button_Arrow_Dow.configure(state=tk.NORMAL)
        Button_Arrow_Up.configure(state=tk.DISABLED)
    else:
        Button_Arrow_Up.configure(state=tk.NORMAL)
        Button_Arrow_Dow.configure(state=tk.NORMAL)

def ConvertHeicToPillowFormat(heic_path):
    # Enregistrement du module d'ouverture pour le format HEIC
    register_heif_opener()

    # Ouverture de l'image HEIC et conversion en mode RGB
    with Image.open(heic_path) as im:
        return im.convert("RGB")

def PicturesProcessing(Path_List, FileName, Selected_Save_Path):
    Many_Selected_Pictures_List = []
    IMG_Mult = []
    incrementation = 0

    for chemin in Path_List:
        # Vérifier si le fichier est au format .heic
        _, extension = os.path.splitext(chemin)
        if extension.lower() == '.heic':
            # Convertir .heic en image lisible avec PIL
            img_heic = ConvertHeicToPillowFormat(chemin)
            Many_Selected_Pictures_List.append(img_heic)
        else:
            # Pour les autres formats, ouvrir directement avec PIL
            Many_Selected_Pictures_List.append(Image.open(chemin))

    for Selected_Picture in Many_Selected_Pictures_List:
        incrementation = incrementation + 1 
        # Convertir en mode RGB et ajouter à la liste IMG_Mult
        IMG_Mult.append(Selected_Picture.convert('RGB'))
        texttodisplay = "Image convertie : {} / {}".format(incrementation, len(Many_Selected_Pictures_List))
        UpdateProcessing(texttodisplay)
        
    # Sauvegarder le fichier PDF
    UpdateProcessing("Enregistrement du PDF")
    UpdateProcessing("...")
    nom = os.path.join(Selected_Save_Path, f"{FileName}.pdf")
    IMG_Mult[0].save(nom, save_all=True, append_images=IMG_Mult[1:])
    UpdateProcessing("PDF enregistré")
    HideProcessing()

def DisplayProcessing():
    global cadre, texte, ascenseur, bouton_cacher, tab1
    
    cadre = tk.Frame(tab1,borderwidth=1, relief="solid")
    cadre.place(x=Table_x_Position, y=Table_y_Position, width=Table_Width, height=Table_Height+25)
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

    Icon_Add_File, Icon_Reset, Icon_Convert_To_Pdf, Icon_Exit, Icon_Test, Icon_Validate, Icon_Zoom_More, Icon_Zoom_Less, Icon_Arrow_Up, Icon_Arrow_Down, Icon_Delete_Selected_Line = IconsDeclaration() #Icons Declaration, cannot be perfomed above, must wait line tab1 = ttk.Frame(master) to get tkinter instance
    
    global Button_Select_Files,Button_Reset,Button_Exit,Button_Convert,Button_Test,Boutons_Controle,Arrows_Buttons,table,Button_Arrow_Up ,Button_Arrow_Dow, Button_Delete_Selected_Line 
    global TraitementConversion,x_Position_Recalculated_For_Arrows_Buttons
    #----------------------------------------
    #Nom Bouton, Texte, Image, Fonction


    Button_Select_Files = tk.Button(tab1) ; Button_Reset = tk.Button(tab1) ;
    Button_Convert = tk.Button(tab1) ; Button_Exit = tk.Button(tab1) ;
    Button_Test = tk.Button(tab1) ;

    Boutons_Controle = [
        [Button_Select_Files, "Add file",Icon_Add_File, ChooseMultiFile,tk.NORMAL ],
        [Button_Reset, "Reset",Icon_Reset, Reset,tk.DISABLED],
        [Button_Convert, "Convertir",Icon_Convert_To_Pdf, OpenDialogToSavePdf,tk.DISABLED],
        [Button_Exit, "Quitter",Icon_Exit, root.destroy,tk.NORMAL],
        # [Button_Test, "Test",Icon_Test, HideProcessing, tk.NORMAL],
    ]

    # Boucle placement des bouttons
    Position_x_recalculee,Position_y_recalculee = ControlsButtonsInitPositionCalculation(Boutons_Controle,Tab1Table,offset=30)

    for i in range(0,len(Boutons_Controle)):
        Boutons_Controle[i][2] = Boutons_Controle[i][2].subsample(Picture_Reducer_Value, Picture_Reducer_Value) #Réduction de la taille de l'image
        Boutons_Controle[i][0].configure( width=Control_Button_Width, height= Control_Button_Height, font=("Helvetica", Police_Size),image=Boutons_Controle[i][2], command=Boutons_Controle[i][3], text = Boutons_Controle[i][1],compound=tk.TOP,state=Boutons_Controle[i][4] )
        Boutons_Controle[i][0].place(x=Position_x_recalculee, y=Position_y_recalculee)
        print("--------------------------------------------")
        print(type(Position_x_recalculee))
        print(type(Control_Button_Width))
        print(type(Space_Between_Button))
        Position_x_recalculee = Position_x_recalculee + Control_Button_Width + Space_Between_Button
        Boutons_Controle[i].append(Position_x_recalculee) #Sauvegarde de la valeur x du bouton à la fin de la liste
        Boutons_Controle[i].append(Control_Button_Init_y_Position) #Sauvegarde de la valeur y du bouton à la fin de la liste

    style = ttk.Style()
    style.map('Treeview', background=[('selected', '#eb0000')])
    #tableau
    table = ttk.Treeview(tab1, columns=('Position', 'Fichier','Chemin'))
    table.heading('Position', text='Position')
    table.column("Position", minwidth=80, width=65, stretch=NO)
    table.heading('Fichier', text='Nom du fichier')
    table.column("Fichier", minwidth=120, width=200, stretch=NO)
    table.heading('Chemin', text='Chemin')
    table.column("Chemin", minwidth=120, width=400, stretch=NO)
    table['show'] = 'headings' # sans ceci, il y avait une colonne vide à gauche qui a pour rôle d'afficher le paramètre "text" qui peut être spécifié lors du insert
    table.place(x=Table_x_Position, y=Table_y_Position, width=Table_Width, height=Table_Height)

    TraitementConversion = tk.Label(tab1, text="", borderwidth=1, relief="solid")

    #----------------------------------------
    #Nom Bouton, Texte, Image, Fonction
    Button_Arrow_Up = tk.Button(tab1) ; Button_Arrow_Dow = tk.Button(tab1) ;  Button_Delete_Selected_Line = tk.Button(tab1)

    Arrows_Buttons = [
        [Button_Arrow_Up, "Monter",Icon_Arrow_Up, ButtonArrowUpAction ],
        [Button_Delete_Selected_Line, "Supprimer",Icon_Delete_Selected_Line, DeleteSelectedLineFromTable],
        [Button_Arrow_Dow, "Descendre",Icon_Arrow_Down, ButtonArrowDownAction],
    ]

    # Boucle placement des bouttons
    x_Position_Recalculated_For_Arrows_Buttons = ArrowButtons_InitPositionCalculation()

    # Associer la fonction DisplaySelectedLineContent à l'événement de clic sur une ligne
    table.bind('<ButtonRelease-1>', DisplaySelectedLineContent)

    return tab1