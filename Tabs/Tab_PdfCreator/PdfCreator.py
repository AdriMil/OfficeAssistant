import Common.SharedFunctions.sharedFunctions as Import
from Common.SharedFunctions.sharedFunctions import AppLanguages, Texte_From_Json
from Tabs.Tab_PdfCreator.initComponents import tab1, myMainButtons, Button_Select_Files, Button_Reset, Button_Convert, Button_Exit,control_arrows, Button_Arrow_Up, Button_Arrow_Down, Button_Delete_Selected_Line
from Common.classes import Button


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
    global x_Position_Recalculated_For_Arrows_Buttons,Window_Width
    Buttons_Number = len(control_arrows)
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
    global Selected_Files,Place_Arrows_Only_Once,table
    Selected_Files = Import.filedialog.askopenfilenames(title=Texte_From_Json["Tab1"]["SelectFiles"][AppLanguages.Language], filetypes= Import.filetypes)
    if Selected_Files:
        Button_Reset.availability("unlock")
        Button_Convert.availability("unlock")
        for file in Selected_Files:
            Path_List.append(file)
            print(("Liste des chemin selectionnés : ", Path_List) if Import.debug == 1 else "")
            words = file.split('/')
            File_Name.append(words[-1]) #On prend la dernière valeur qui correspond au nom du fichier
            table.insert( '', 'end',values=(len(Path_List),words[-1],file))
            All_Data_In_Table.append([len(Path_List),words[-1],file]) #Give list of all data in tab -> will use do modify file order

        if (Place_Arrows_Only_Once == 0 ): #Bloquer la repetitiuon d'ajoute  des boutons fleches
            Import.buttons_position(control_arrows,Import.Tab1Table[0],Import.Tab1Table[1]+(Import.Tab1Table[3]),Import.Tab1Table[2])
            Place_Arrows_Only_Once = 1
        DisableButtonIfNecessery()

    else:
        Import.Error_Cancelation(Texte_From_Json,AppLanguages.Language)

def OpenDialogToSavePdf():
    user_input = Import.simpledialog.askstring(Texte_From_Json["Tab1"]["SaveFile"]["WindowName"][AppLanguages.Language], Texte_From_Json["Tab1"]["SaveFile"]["Instruction"][AppLanguages.Language])
    if user_input is None:
        print(("L'utilisateur a cliqué sur Cancel.")if Import.debug == 1 else "")
    elif user_input:
        FileName = user_input
        ConvertPictureToPdf(FileName)
    else:
        Import.Error_NoTitle(Texte_From_Json,AppLanguages.Language)
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
        Import.DisplayProcessing(Import.Table_x_Position,Import.Table_y_Position,Import.Table_Width,Import.Table_Height,tab1.frame) #Call process
        PicturesProcessing(Files_Paths_Updated_List, FileName, Selected_Save_Path)
        

def Reset():
    User_Answer=Import.Info_Reset(Texte_From_Json,AppLanguages.Language)
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
    # x_Position_Recalculated_For_Arrows_Buttons = ArrowButtons_InitPositionCalculation() #Permet de reset la position des btns et donc d'éviter un décallage des btns à chaque reset

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
        Button_Arrow_Down.availability("lock")
        Button_Arrow_Up.availability("lock")
    elif (Selected_Line_Index==All_Data_In_Table[-1][0]):
        Button_Arrow_Down.availability("lock")
        Button_Arrow_Up.availability("unlock")
    elif (Selected_Line_Index==All_Data_In_Table[0][0]):
        Button_Arrow_Down.availability("unlock")
        Button_Arrow_Up.availability("lock")
    else:
        Button_Arrow_Up.availability("unlock")
        Button_Arrow_Down.availability("unlock")


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
        texttodisplay = (Texte_From_Json["Processing"]["PictureSaving"][AppLanguages.Language]).format(incrementation, len(Many_Selected_Pictures_List))
        Import.UpdateProcessing(texttodisplay)
        
    # Sauvegarder le fichier PDF
    Import.UpdateProcessing(Texte_From_Json["Processing"]["PdfSaving"][AppLanguages.Language])
    Import.UpdateProcessing("...")
    nom = Import.os.path.join(Selected_Save_Path, f"{FileName}.pdf")
    IMG_Mult[0].save(nom, save_all=True, append_images=IMG_Mult[1:])
    Import.UpdateProcessing(Texte_From_Json["Processing"]["FinishPdfSaving"][AppLanguages.Language])
    Import.Info_ProcessFinished(Files_Paths_Updated_List,FileName,Selected_Save_Path,Texte_From_Json,AppLanguages.Language)
    Import.HideProcessing()


def PdfCreatorTab(master,root):
    InitValues()
    
    Import.InitButtonsIcones() #Load button icones
    
    global Arrows_Buttons,table,Button_Arrow_Up ,Button_Arrow_Down, Button_Delete_Selected_Line 
    global TraitementConversion,x_Position_Recalculated_For_Arrows_Buttons
    #----------------------------------------
    #Nom Bouton, Texte, Image, Fonction

    Import.buttons_position(myMainButtons,Import.Tab1Table[0],Import.Tab1Table[1]-(1.3*Button.HEIGHT),Import.Tab1Table[2])

    Button_Select_Files.associate_a_function(ChooseMultiFile)
    Button_Reset.associate_a_function(Reset)
    Button_Convert.associate_a_function(OpenDialogToSavePdf)
    Button_Exit.associate_a_function(Import.exit)

    Button_Arrow_Up.associate_a_function(ButtonArrowUpAction)
    Button_Arrow_Down.associate_a_function(ButtonArrowDownAction)
    Button_Delete_Selected_Line.associate_a_function(DeleteSelectedLineFromTable)

    style = Import.ttk.Style()
    style.map('Treeview', background=[('selected', '#eb0000')])

    #tableau
    table = Import.ttk.Treeview(tab1.frame, columns=(Texte_From_Json["Tab1"]["PannelHeader"]["Column1"][AppLanguages.Language], Texte_From_Json["Tab1"]["PannelHeader"]["Column2"][AppLanguages.Language],Texte_From_Json["Tab1"]["PannelHeader"]["Column3"][AppLanguages.Language]))
    headers = [(Texte_From_Json["Tab1"]["PannelHeader"]["Column1"][AppLanguages.Language],Texte_From_Json["Tab1"]["PannelHeader"]["Column1"][AppLanguages.Language], 80, 65), (Texte_From_Json["Tab1"]["PannelHeader"]["Column2"][AppLanguages.Language], Texte_From_Json["Tab1"]["PannelHeader"]["Column2"][AppLanguages.Language], 120, 200), (Texte_From_Json["Tab1"]["PannelHeader"]["Column3"][AppLanguages.Language], Texte_From_Json["Tab1"]["PannelHeader"]["Column3"][AppLanguages.Language], 120, 400)]
    for header in headers:
        table.heading(header[0], text=header[1])
        table.column(header[0], minwidth=header[2], width=header[3], stretch=Import.NO)
    table['show'] = 'headings' # sans ceci, il y avait une colonne vide à gauche qui a pour rôle d'afficher le paramètre "text" qui peut être spécifié lors du insert
    table.place(x=Import.Table_x_Position, y=Import.Table_y_Position, width=Import.Table_Width, height=Import.Table_Height)

    TraitementConversion = Import.tk.Label(tab1.frame, text="", borderwidth=1, relief="solid")

    #----------------------------------------
    #Nom Bouton, Texte, Image, Fonction
    # Button_Arrow_Up = Import.tk.Button(tab1.frame) ; Button_Arrow_Down = Import.tk.Button(tab1.frame) ;  Button_Delete_Selected_Line = Import.tk.Button(tab1.frame)

    # Arrows_Buttons = [
    #     [Button_Arrow_Up, "Monter",Import.Icon_Arrow_Up, ButtonArrowUpAction ],
    #     [Button_Delete_Selected_Line, "Supprimer",Import.Icon_Delete_Selected_Line, DeleteSelectedLineFromTable],
    #     [Button_Arrow_Down, "Descendre",Import.Icon_Arrow_Down, ButtonArrowDownAction],
    # ]

    # Boucle placement des bouttons
    # x_Position_Recalculated_For_Arrows_Buttons = ArrowButtons_InitPositionCalculation()

    # Associer la fonction DisplaySelectedLineContent à l'événement de clic sur une ligne
    table.bind('<ButtonRelease-1>', DisplaySelectedLineContent)

    return tab1.frame