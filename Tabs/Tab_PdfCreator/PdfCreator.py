import SharedFunctions.imports as Import

#-------------------INIT-----------#
def InitValues():
    global Chemin,Path_List,File_Name,Selected_Save_Path,Many_Selected_Pictures_List,IMG_Mult,Selected_Files,Place_Arrows_Only_Once,All_Data_In_Table,Files_Paths_Updated_List,Selected_Line_Index
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
    global  Window_Width
    return Import.Window_Height,Import.Window_Width
#-------------------------------------------------------------

def ArrowButtons_InitPositionCalculation():
    global Table_Width,x_Position_Recalculated_For_Arrows_Buttons,Window_Width
    Buttons_Number = len(Arrows_Buttons)
    Spaces_Used_By_Buttons = Buttons_Number * (Import.Arrows_Buttons_Width+Import.Space_Between_Arrows_Buttons)
    Free_Space = Import.Table_Width - (Spaces_Used_By_Buttons)
    if(Free_Space>0):
        x_Position_Recalculated_For_Arrows_Buttons = Import.Table_x_Position + (Free_Space / 2)
        Window_Width = Import.Table_Width + Import.Table_x_Position *2

    else:
        Extra_Buttons_Space = Spaces_Used_By_Buttons - Import.Table_Width
        x_Position_Recalculated_For_Arrows_Buttons = Import.Table_x_Position - (Extra_Buttons_Space / 2)
        Window_Width = Import.Table_Width + Extra_Buttons_Space

    return x_Position_Recalculated_For_Arrows_Buttons

def ChooseMultiFile():
    global Selected_Files,Place_Arrows_Only_Once,Button_Reset,table
    Selected_Files = Import.filedialog.askopenfilenames(title=Texte_From_Json["Tab1"]["SelectFiles"][Import.Language], filetypes= Import.filetypes)
    if Selected_Files:
        Button_Reset.configure(state=Import.tk.NORMAL); Button_Convert.configure(state=Import.tk.NORMAL)
        for file in Selected_Files:
            Path_List.append(file)
            # print("Liste des chemin selectionnés : ", Path_List)
            words = file.split('/')
            File_Name.append(words[-1]) #On prend la dernière valeur qui correspond au nom du fichier
            table.insert( '', 'end',values=(len(Path_List),words[-1],file))
            All_Data_In_Table.append([len(Path_List),words[-1],file]) #Give list of all data in tab -> will use do modify file order

        if (Place_Arrows_Only_Once == 0 ): #Bloquer la repetitiuon d'ajoute  des boutons fleches
            Import.PlaceButtonsAutomaticaly(Arrows_Buttons,Import.Arrows_Buttons_Init_y_Position,Import.Arrows_Buttons_Width,Import.Arrows_Buttons_Height,Import.Space_Between_Arrows_Buttons,Import.Picture_Reducer_Value,x_Position_Recalculated_For_Arrows_Buttons,Import.Police_Size,TextDisplay=0,Init_State=0)
            Place_Arrows_Only_Once = 1
        DisableButtonIfNecessery()

    else:
        Import.Error_Cancelation()

def OpenDialogToSavePdf():
    user_input = Import.simpledialog.simpledialog.askstring(Texte_From_Json["Tab1"]["SaveFile"]["WindowName"][Import.Language], Texte_From_Json["Tab1"]["SaveFile"]["Instruction"][Import.Language])
    if user_input is None:
        print("L'utilisateur a cliqué sur Cancel.")
    elif user_input:
        FileName = user_input
        ConvertPictureToPdf(FileName)
    else:
        Import.Error_NoTitle(Texte_From_Json,Import.Language)
        OpenDialogToSavePdf()

def ConvertPictureToPdf(FileName):
    if (Files_Paths_Updated_List == []):
        GetFilesPathList()
    SavePath()
    Selected_Save_Path = Chemin
    if(Selected_Save_Path==''):               #Verif si un chemin final est indiqué
        Import.Error_BadSavePath()
    elif(len(Path_List)==0):         #Verif si au moins une image est selctionnée
        Import.Error_NoPicture()
    else:                               #Si plusieurs images à convertir
        # TraitementConversion.place(x=Table_x_Position + 1, y=Table_y_Position + 24, width=Table_Width, height=Table_Height)
        Import.DisplayProcessing(Import.Table_x_Position,Import.Table_y_Position,Import.Table_Width,Import.Table_Height,tab1) #Call process
        PicturesProcessing(Files_Paths_Updated_List, FileName, Selected_Save_Path)
        

def Reset():
    User_Answer=Import.INfo_Reset()
    if User_Answer == 'yes':
        DeleteAlldata()

def DeleteAlldata():
    global Place_Arrows_Only_Once,x_Position_Recalculated_For_Arrows_Buttons
    InitValues()
        # Reset Arrows button
    Place_Arrows_Only_Once = 0
    for btn in Arrows_Buttons:
        btn[0].place_forget()

    # Reset btn Reset et convertir
    Button_Reset.configure(state=Import.tk.DISABLED); Button_Convert.configure(state=Import.tk.DISABLED)
    Path_List.clear() #RESET de la liste Path_List
    File_Name.clear() #RESET de la liste File_Name
    x_Position_Recalculated_For_Arrows_Buttons = ArrowButtons_InitPositionCalculation() #Permet de reset la position des btns et donc d'éviter un décallage des btns à chaque reset

    #REset displayed data in Tableau
    table.delete(*table.get_children())
    

def SavePath():
    global Chemin
    Chemin = Import.filedialog.askdirectory()

def DisplaySelectedLineContent(event):
    global Selected_Line_Index
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
    global Files_Paths_Updated_List,Path_List
    Files_Paths_Updated_List=[]
    Files_Paths_Updated_List = [element[2] for element in All_Data_In_Table]
    Path_List = Files_Paths_Updated_List

def ButtonArrowDownAction():
    global Selected_Line_Index
    if (Selected_Line_Index is not None):
        Import.ChangePlaceDown(All_Data_In_Table,Selected_Line_Index)
        UpdateTable()
        Selected_Line_Index += 1
        NextLineToBeAutoSelected("Down")

def ButtonArrowUpAction():
    global Selected_Line_Index
    if (Selected_Line_Index is not None):
        Import.ChangePlaceUp(All_Data_In_Table,Selected_Line_Index)
        UpdateTable()
        Selected_Line_Index -= 1
        NextLineToBeAutoSelected("Up")

def DeleteSelectedLineFromTable():
    Import.DeleteSelectedLine(All_Data_In_Table,Selected_Line_Index-1)
    UpdateTable()
    GetFilesPathList()
    if (len(All_Data_In_Table)==0):
        DeleteAlldata()
    else:
        NextLineToBeAutoSelected("Delete")

def NextLineToBeAutoSelected(action):
    global Selected_Line_Index
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
    if((Selected_Line_Index==All_Data_In_Table[0][0]) and (Selected_Line_Index==All_Data_In_Table[-1][0])):
        Button_Arrow_Dow.configure(state=Import.tk.DISABLED)
        Button_Arrow_Up.configure(state=Import.tk.DISABLED)
    elif (Selected_Line_Index==All_Data_In_Table[-1][0]):
        Button_Arrow_Dow.configure(state=Import.tk.DISABLED)
        Button_Arrow_Up.configure(state=Import.tk.NORMAL)
    elif (Selected_Line_Index==All_Data_In_Table[0][0]):
        Button_Arrow_Dow.configure(state=Import.tk.NORMAL)
        Button_Arrow_Up.configure(state=Import.tk.DISABLED)
    else:
        Button_Arrow_Up.configure(state=Import.tk.NORMAL)
        Button_Arrow_Dow.configure(state=Import.tk.NORMAL)


def PicturesProcessing(Path_List, FileName, Selected_Save_Path):
    Many_Selected_Pictures_List = []
    IMG_Mult = []
    incrementation = 0

    for chemin in Path_List:
        # Vérifier si le fichier est au format .heic
        _, extension = Import.os.path.splitext(chemin)
        if extension.lower() == '.heic':
            # Convertir .heic en image lisible avec PIL
            img_heic = Import.ConvertHeicToPillowFormat(chemin)
            Many_Selected_Pictures_List.append(img_heic)
        else:
            # Pour les autres formats, ouvrir directement avec PIL
            Many_Selected_Pictures_List.append(Import.Image.open(chemin))

    for Selected_Picture in Many_Selected_Pictures_List:
        incrementation = incrementation + 1 
        # Convertir en mode RGB et ajouter à la liste IMG_Mult
        IMG_Mult.append(Selected_Picture.convert('RGB'))
        texttodisplay = (Texte_From_Json["Processing"]["PictureSaving"][Import.Language]).format(incrementation, len(Many_Selected_Pictures_List))
        Import.UpdateProcessing(texttodisplay)
        
    # Sauvegarder le fichier PDF
    Import.UpdateProcessing(Texte_From_Json["Processing"]["PdfSaving"][Import.Language])
    Import.UpdateProcessing("...")
    nom = Import.os.path.join(Selected_Save_Path, f"{FileName}.pdf")
    IMG_Mult[0].save(nom, save_all=True, append_images=IMG_Mult[1:])
    Import.UpdateProcessing(Texte_From_Json["Processing"]["FinishPdfSaving"][Import.Language])
    Import.Info_ProcessFinished(Files_Paths_Updated_List,FileName,Selected_Save_Path)
    Import.HideProcessing()

def PdfCreatorTab(master,root):
    global tab1
    global Texte_From_Json
    tab1 = Import.ttk.Frame(master)
    InitValues()
    Texte_From_Json=Import.LoadText()

    Icon_Add_File = Import.PhotoImage(file=Import.Ressource_Path("Pictures/AddFile.png"))
    Icon_Reset = Import.PhotoImage(file=Import.Ressource_Path("Pictures/Reset.png"))
    Icon_Convert_To_Pdf = Import.PhotoImage(file=Import.Ressource_Path("Pictures/ConvertInPdf.png"))
    Icon_Exit = Import.PhotoImage(file=Import.Ressource_Path("Pictures/Exit.png"))
    Icon_Test = Import.PhotoImage(file=Import.Ressource_Path("Pictures/test.png"))
    Icon_Arrow_Up = Import.PhotoImage(file=Import.Ressource_Path("Pictures/Icon_Arrow_Up.png"))
    Icon_Arrow_Down = Import.PhotoImage(file=Import.Ressource_Path("Pictures/Icon_Arrow_Down.png"))
    Icon_Delete_Selected_Line = Import.PhotoImage(file=Import.Ressource_Path("Pictures/Reset.png"))
    
    global Button_Select_Files,Button_Reset,Button_Exit,Button_Convert,Button_Test,Boutons_Controle,Arrows_Buttons,table,Button_Arrow_Up ,Button_Arrow_Dow, Button_Delete_Selected_Line 
    global TraitementConversion,x_Position_Recalculated_For_Arrows_Buttons
    #----------------------------------------
    #Nom Bouton, Texte, Image, Fonction

    Button_Select_Files = Import.tk.Button(tab1) ; Button_Reset = Import.tk.Button(tab1) ;
    Button_Convert = Import.tk.Button(tab1) ; Button_Exit = Import.tk.Button(tab1) ;
    Button_Test = Import.tk.Button(tab1) ;

    Boutons_Controle = [
        [Button_Select_Files,Texte_From_Json["Buttons"]["AddFiles"][Import.Language],Icon_Add_File, ChooseMultiFile,Import.tk.NORMAL ],
        [Button_Reset, Texte_From_Json["Buttons"]["Reset"][Import.Language],Icon_Reset, Reset,Import.tk.DISABLED],
        [Button_Convert, Texte_From_Json["Buttons"]["Convert"][Import.Language],Icon_Convert_To_Pdf, OpenDialogToSavePdf,Import.tk.DISABLED],
        [Button_Exit, Texte_From_Json["Buttons"]["Exit"][Import.Language],Icon_Exit, root.destroy,Import.tk.NORMAL],
        # [Button_Test, "Test",Icon_Test, HideProcessing, tk.NORMAL],
    ]

    # Boucle placement des bouttons
    Position_x_recalculee,Position_y_recalculee = Import.ControlsButtonsInitPositionCalculation(Boutons_Controle,Import.Tab1Table,offset=30)

    #Function which place buttons
    Import.PlaceButtonsAutomaticaly(Boutons_Controle,Position_y_recalculee,Import.Control_Button_Width,Import.Control_Button_Height,Import.Space_Between_Button,Import.Picture_Reducer_Value,Position_x_recalculee,Import.Police_Size,TextDisplay=1,Init_State=1)

    style = Import.ttk.Style()
    style.map('Treeview', background=[('selected', '#eb0000')])

    #tableau
    table = Import.ttk.Treeview(tab1, columns=(Texte_From_Json["Tab1"]["PannelHeader"]["Column1"][Import.Language], Texte_From_Json["Tab1"]["PannelHeader"]["Column2"][Import.Language],Texte_From_Json["Tab1"]["PannelHeader"]["Column3"][Import.Language]))
    headers = [(Texte_From_Json["Tab1"]["PannelHeader"]["Column1"][Import.Language],Texte_From_Json["Tab1"]["PannelHeader"]["Column1"][Import.Language], 80, 65), (Texte_From_Json["Tab1"]["PannelHeader"]["Column2"][Import.Language], Texte_From_Json["Tab1"]["PannelHeader"]["Column2"][Import.Language], 120, 200), (Texte_From_Json["Tab1"]["PannelHeader"]["Column3"][Import.Language], Texte_From_Json["Tab1"]["PannelHeader"]["Column3"][Import.Language], 120, 400)]
    for header in headers:
        table.heading(header[0], text=header[1])
        table.column(header[0], minwidth=header[2], width=header[3], stretch=Import.NO)
    table['show'] = 'headings' # sans ceci, il y avait une colonne vide à gauche qui a pour rôle d'afficher le paramètre "text" qui peut être spécifié lors du insert
    table.place(x=Import.Table_x_Position, y=Import.Table_y_Position, width=Import.Table_Width, height=Import.Table_Height)

    TraitementConversion = Import.tk.Label(tab1, text="", borderwidth=1, relief="solid")

    #----------------------------------------
    #Nom Bouton, Texte, Image, Fonction
    Button_Arrow_Up = Import.tk.Button(tab1) ; Button_Arrow_Dow = Import.tk.Button(tab1) ;  Button_Delete_Selected_Line = Import.tk.Button(tab1)

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