from Common.myImports import *
from Common.classes import Button
from Common.init import root

#-------------App Languages--------------------#
from Common.SharedFunctions.AppStringsTranslated import My_App_Strings

def LoadText():
    data = json.loads(My_App_Strings)
    return data

class AppLanguages:
    Language = "fr"
    languages = ["Français", "English", "Español","German"]

class Watermark:
    Canvas = None
    Text = ""
    Transparency = 75 #Value between 0 and 254
    Font_Size = 50
    Color = (255, 0, 0)
    Display_Color = '#fa5047' 
    Space_Between_Text = 200
    Width =None
    Height = None
    Lines_Coordonate = []
#Allows to displays print, only for debug purpose
debug = 1

#TAB3
tab3 = None

#------------langage Menu Shape-------------#
Language_Button_Width = 20 ; Language_Button_Height = 1 ;

#------------Design UI VARIABLE SPACE-------------#
#Tableau Tab1:
Table_x_Position = 50 ; Table_y_Position = 200
Table_Width = 600 ; Table_Height = 250
Tab1Table = [Table_x_Position,Table_y_Position,Table_Width,Table_Height]

#Tab2
Tab2DisplayWindow_x_position = 50 ; Tab2DisplayWindow_y_position = 100
Tab2DisplayWindow_width = 600 ; Tab2DisplayWindow_Height = 400
Tab2Canvas = [Tab2DisplayWindow_x_position,Tab2DisplayWindow_y_position,Tab2DisplayWindow_width,Tab2DisplayWindow_Height]

#Tab3
Tab3DisplayWindow_x_position = 50 ; Tab3DisplayWindow_y_position = 100
Tab3DisplayWindow_width = 600 ; Tab3DisplayWindow_Height = 400
Tab3Canvas = [Tab3DisplayWindow_x_position,Tab3DisplayWindow_y_position,Tab3DisplayWindow_width,Tab3DisplayWindow_Height]

#Commun buttons parameters
Control_Button_Width = 50 ; Control_Button_Height = 50 ; Space_Between_Button = 10
Control_Button_Init_x_Position = 0 ; Control_Button_Init_y_Position = Table_y_Position - Control_Button_Height - 30
Window_Height = Table_Height + Control_Button_Init_y_Position + Table_y_Position + (Language_Button_Height + 30)
Police_Size = 10

#Arrows Boutons Tab 1 parameters
Arrows_Buttons_Width = 25 ; Arrows_Buttons_Height = 25 ; Space_Between_Arrows_Buttons = 10
Arrows_Buttons_Init_y_Position = Table_y_Position + Table_Height + 10

#Arrows Boutons Tab 2 parameters
Zoom_Buttons_Width = 25 ; Zoom_Buttons_Height = 25 ; Space_Between_Zoom_Buttons = 10
Zoom_Buttons_Init_y_Position = Tab2DisplayWindow_y_position + Tab2DisplayWindow_Height + 10

#Police
Police_Typo  = "Helvetica"
Font_Path = "arial.ttf"  # Remplacez par le chemin de votre police si nécessaire

def exit():
    root.destroy()

#Buttons Pictures
def InitButtonsIcones():
    global Icon_Add_File, Icon_Reset,Icon_Exit,Icon_Test,Icon_Validate,Icon_Zoom_More,Icon_Zoom_Less,Icon_Revert
    global Icon_Convert_To_Pdf,Icon_Arrow_Up,Icon_Arrow_Down,Icon_Delete_Selected_Line
    global Icon_Text_Modifications

    Icon_Add_File = PhotoImage(file=Ressource_Path("Pictures/AddFile.png"))
    Icon_Reset = PhotoImage(file=Ressource_Path("Pictures/Reset.png"))
    Icon_Exit = PhotoImage(file=Ressource_Path("Pictures/Exit.png"))
    Icon_Test = PhotoImage(file=Ressource_Path("Pictures/test.png"))
    Icon_Validate = PhotoImage(file=Ressource_Path("Pictures/Valider.png"))
    Icon_Zoom_More = PhotoImage(file=Ressource_Path("Pictures/zoomPlus.png"))
    Icon_Zoom_Less = PhotoImage(file=Ressource_Path("Pictures/zoomMoins.png"))
    Icon_Revert = PhotoImage(file=Ressource_Path("Pictures/Revert.png"))
    Icon_Convert_To_Pdf = PhotoImage(file=Ressource_Path("Pictures/ConvertInPdf.png"))
    Icon_Arrow_Up = PhotoImage(file=Ressource_Path("Pictures/Icon_Arrow_Up.png"))
    Icon_Arrow_Down = PhotoImage(file=Ressource_Path("Pictures/Icon_Arrow_Down.png"))
    Icon_Delete_Selected_Line = PhotoImage(file=Ressource_Path("Pictures/Reset.png"))
    Icon_Text_Modifications = PhotoImage(file=Ressource_Path("Pictures/TextModification.png"))

#Icone reducer - Will zoom on icone. 1 = 100%. 2= 200% ...
Picture_Reducer_Value =  1

#Available Formats user will see when selecting files to import
Texte_From_Json = LoadText()
filetypes = [(Texte_From_Json["Common"]["FilesTypeSelection"][AppLanguages.Language], "*.png;*.jpg;*.heic")]

#Gestion chemin fichier #Format adapté pour pyinstaller :
def Ressource_Path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

print(Ressource_Path("Pictures/AddFile.png"))

# Work with HEIC Picture
def ConvertHeicToPillowFormat(heic_path):
    # Enregistrement du module d'ouverture pour le format HEIC
    register_heif_opener()
    # Ouverture de l'image HEIC et conversion en mode RGB
    with Image.open(heic_path) as im:
        return im.convert("RGB")

#---------------Calcul de la position des boutons ----------------------#
def ControlsButtonsInitPositionCalculation(Liste_Boutons_De_Control,TableForYourTab,offset):
    
    global  Control_Button_Width, Control_Button_Height,Space_Between_Button,Control_Button_Init_x_Position,Control_Button_Init_y_Position,Window_Width
    #Tous les boutons vont être collés et centré sur le tableau
    Number_Of_Buttons = len(Liste_Boutons_De_Control)
    Buttons_Total_Lenght = Number_Of_Buttons * (Control_Button_Width+Space_Between_Button)
    Free_Space = TableForYourTab[2] - (Buttons_Total_Lenght)
    if(Free_Space>0):
        Control_Button_Init_x_Position = TableForYourTab[0] + (Free_Space / 2)

        Window_Width = TableForYourTab[2] + TableForYourTab[0] *2

    else:
        Extra_Buttons_Space = Buttons_Total_Lenght - TableForYourTab[2]
        Control_Button_Init_x_Position = TableForYourTab[0] - (Extra_Buttons_Space / 2)
        Window_Width = TableForYourTab[2] + Extra_Buttons_Space

    # Calcul de Control_Button_Init_y_Position
    Control_Button_Init_y_Position = TableForYourTab[1] - Control_Button_Height - offset

    return Control_Button_Init_x_Position,Control_Button_Init_y_Position


####Will be deleted
def PlaceButtonsAutomaticaly(Button_List,Position_y_recalculee,Button_Width,Button_Height,Space_Between_Button,Picture_Reducer_Value,Position_x_recalculee,Police_Size,TextDisplay,Init_State):
    for i in range(0,len(Button_List)):
        Button_List[i][2] = Button_List[i][2].subsample(Picture_Reducer_Value, Picture_Reducer_Value) #Réduction de la taille de l'image
        Button_List[i][0].configure( width=Button_Width, height= Button_Height, font=(Police_Typo, Police_Size),image=Button_List[i][2], command=Button_List[i][3] )
        Button_List[i][0].place(x=Position_x_recalculee, y=Position_y_recalculee)
        if(TextDisplay==1):Button_List[i][0].configure(text = Button_List[i][1],compound=tk.TOP)
        if(Init_State==1):Button_List[i][0].configure(state=Button_List[i][4])
        Position_x_recalculee = Position_x_recalculee + Button_Width + Space_Between_Button
        Button_List[i].append(Position_x_recalculee) #Sauvegarde de la valeur x du bouton à la fin de la liste
        Button_List[i].append(Position_y_recalculee) #Sauvegarde de la valeur y du bouton à la fin de la liste


def buttons_position(buttons_list :list, reference_x : int, refence_y :int, reference_width :int) -> float:
    """
    This function will be use to place an amount of buttons on a given width. If the amount of button is too high for line width, then a new line will be created.

    Args:
        buttons_list (list): List with all buttons which should be placed
        reference_x (int): x point used to calculate button centering
        refence_y (int): y point used to calculate button centering
        reference_width (int): width substarcted to x position to know length where button will be centered

    Returns:
        float: 1st button x position calculated to allow centering of all buttons
    """
    global place
    button_number = len(buttons_list)
    if debug==1 : print(button_number, "Button in my list")
    
    free_space = reference_width - (button_number * (Button.WIDTH + Button.SPACE_BETWEEN_BUTTON))

    place = reference_x + (free_space / 2)                                                #Buttons will be centered on reference, without line break
    calculate_button_position(buttons_list, place, refence_y) 
  
    return place
    

    
def calculate_button_position(buttons_list :list, x_position: int,y_position: int):           #Update button position.
    """
    Will be call to place an amount of button centered on one line.

    Args:
        buttons_list (list): all button which should be placed on one line
        x_position (int): x position for the first button of the buttons_list
        y_position (int): y position for the first button of the buttons_list
    """
    for mybutton in buttons_list:
        mybutton.update_button_position(xposition=x_position,yposition=y_position)
        if debug == 1 : print("My x position is : ",x_position, " My y position is : ", y_position)
        x_position = x_position + mybutton.width + mybutton.space_between_button

#Processing information
def DisplayProcessing(Display_Window_x_position,Displa_yWindow_y_position,Display_Window_Width,Display_Window_Height,tab):
    global cadre, texte, ascenseur
    cadre = tk.Frame(tab,borderwidth=1, relief="solid")
    cadre.place(x=Display_Window_x_position, y=Displa_yWindow_y_position, width=Display_Window_Width, height=Display_Window_Height)
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

#Give number and language depend the input
def ConvertLanguage(Current_Language):
    if Current_Language=="Français" or Current_Language=="fr" or Current_Language==0:
        Converted_language="fr"
        Language_Number = 0 
    elif Current_Language=="English" or Current_Language=="en" or Current_Language==1:
        Converted_language="en"
        Language_Number = 1
    elif Current_Language=="Español" or Current_Language=="es" or Current_Language==2:
        Converted_language="es"
        Language_Number = 2 
    elif Current_Language=="German" or Current_Language=="ge" or Current_Language==3:
        Converted_language="ge"
        Language_Number = 3 

    return Converted_language,Language_Number

def TransparencyCrossProduct(Selected_Value,Step):
    if Step == "From_Slider":
        Transparency_Value = (Selected_Value*254)//100
    elif Step == "From_RealValue":
        Transparency_Value = (Selected_Value*100)//254
    return Transparency_Value


#--------------Scroll Bar-----------------------
def ScrollBar(Import,canvas):
    global Scrollbar_x_Direction,Scrollbar_y_Direction
        # Add horizontal scrollbar
    Scrollbar_x_Direction = Import.tk.Scrollbar(canvas, orient="horizontal", command=canvas.xview)
    canvas.configure(xscrollcommand=Scrollbar_x_Direction.set)

    # Add vertical scrollbar
    Scrollbar_y_Direction = Import.tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=Scrollbar_y_Direction.set)

def ScrollBarLenghCalculation(Import,canvas):
    canvas.config(scrollregion=canvas.bbox(Import.tk.ALL))

def HideScrollbars():
    Scrollbar_x_Direction.pack_forget()
    Scrollbar_y_Direction.pack_forget()

def ShowScrollbars():
    Scrollbar_x_Direction.pack(side="bottom", fill="x")
    Scrollbar_y_Direction.pack(side="right", fill="y")

def HorizontalMouvement(event):
    global Last_x_Mouse_Position, Last_y_Mouse_Position
    Last_x_Mouse_Position = event.x_root
    Last_y_Mouse_Position = event.y_root

def MousewheelMouvement(event,canvas):
    if event.delta > 0:
        canvas.yview_scroll(-1, "units")  # Défilement vers le haut
    else:
        canvas.yview_scroll(1, "units")   # Défilement vers le bas