import SharedFunctions.imports as Import
from PIL import Image
from PIL import ImageTk  

Place_Zoom_Buttons_Only_Once = 0 #Should never reseted

def InitValues():
    global Selected_Picture, x_Position_Recalculated_For_Zoom_Buttons, Zoom_Incrementation, Rectangles_Coordonates_List, Rectangles_Ids_List, Current_Rectangle_Id, First_Clic_x_Location, First_Clic_y_Location,Display_Revert_Button
    global Extension,Format
    Selected_Picture = None
    x_Position_Recalculated_For_Zoom_Buttons = 0 
    Zoom_Incrementation = 0
    Rectangles_Coordonates_List = [] 
    Rectangles_Ids_List = [] # Store rectangle's id
    Current_Rectangle_Id = None # Store current rectangle's id
    First_Clic_x_Location = None #Store first clic x locatoin
    First_Clic_y_Location = None #Store first clic y locatoin
    Display_Revert_Button = 0
    Extension,Format = "","" #Used to share between function kind of selected picture

#Allows to displays print to debug
debug = 1
def test():
    print("test")

# When left clik on mouse,  start rectangle creation
def StartRectangleDrawing(event):
    global First_Clic_x_Location, First_Clic_y_Location, Current_Rectangle_Id
    First_Clic_x_Location = event.x + canvas.canvasx(0)
    First_Clic_y_Location = event.y + canvas.canvasy(0)
    Current_Rectangle_Id = canvas.create_rectangle(First_Clic_x_Location, First_Clic_y_Location, First_Clic_x_Location, First_Clic_y_Location, outline="red", fill="black")

# Update rectangle position during mouse mouvments
def UpdateRectangleDrawing(event):
    global First_Clic_x_Location, First_Clic_y_Location, Current_Rectangle_Id
    if First_Clic_x_Location is not None and First_Clic_y_Location is not None:
        x_image = event.x + canvas.canvasx(0)
        y_image = event.y + canvas.canvasy(0)
        canvas.coords(Current_Rectangle_Id, First_Clic_x_Location, First_Clic_y_Location, x_image, y_image)

# Finish rectangle build when left click is released
def FinishRectangleDrawing(event):
    global First_Clic_x_Location, First_Clic_y_Location, Rectangles_Ids_List,Rectangles_Coordonates_List,Display_Revert_Button
    if First_Clic_x_Location is not None and First_Clic_y_Location is not None:
        x_image = event.x + canvas.canvasx(0)
        y_image = event.y + canvas.canvasy(0)
        Rectangles_Ids_List.append(Current_Rectangle_Id)
        First_Clic_x_Location, First_Clic_y_Location,x_image,y_image = FixValues(First_Clic_x_Location, First_Clic_y_Location,x_image,y_image)
        Rectangles_Coordonates_List.append([First_Clic_x_Location, First_Clic_y_Location,x_image,y_image])
        print((Rectangles_Coordonates_List) if debug==1 else "")
    First_Clic_x_Location = None
    First_Clic_y_Location = None
    if(Display_Revert_Button==0):
        Zoom_Buttons[2][0].configure(state=Import.tk.NORMAL)
        Display_Revert_Button = 1 ; 

def RevertRectangles():
    global Rectangles_Coordonates_List,Rectangles_Ids_List,Display_Revert_Button

    if Rectangles_Ids_List:
        # Récupérer l'ID du dernier rectangle
        last_rectangle_id = Rectangles_Ids_List.pop()
        if not Rectangles_Ids_List:
            Zoom_Buttons[2][0].configure(state=Import.tk.DISABLED)
            Display_Revert_Button = 0 ; 
        # Supprimer le dernier rectangle du canvas
        canvas.delete(last_rectangle_id)
        # Supprimer les coordonnées du dernier rectangle de la liste
        Rectangles_Coordonates_List.pop()
        

        # Mettre à jour le canvas
        canvas.update()
        
#Fix issue if you created your rectangle from bottom to top (wihtout this function rectangle won't appears on save pictures)
def FixValues(First_Clic_x_Location, First_Clic_y_Location, x_image, y_image):
    if First_Clic_x_Location > x_image:
        First_Clic_x_Location, x_image = x_image, First_Clic_x_Location
    if First_Clic_y_Location > y_image:
        First_Clic_y_Location, y_image = y_image, First_Clic_y_Location
    return First_Clic_x_Location, First_Clic_y_Location, x_image, y_image

##-------Not in this milestone Scope, will be used later to calculate rectangle new siez and position depending on zoom
# def resize_image():
#     global Selected_Picture, photo
#     new_width = Selected_Picture.width // 2
#     new_height = Selected_Picture.height // 2
#     Selected_Picture = Selected_Picture.resize((new_width, new_height))
#     photo = ImageTk.PhotoImage(Selected_Picture)
#     canvas.config(width=new_width, height=new_height)
#     canvas.itemconfig(Updated_Picture, image=photo)
#     UpdateRectangleDrawings_positions(new_width, new_height)

##-------Not in this milestone Scope, will be used later to calculate rectangle new siez and position depending on zoom
# def UpdateRectangleDrawings_positions(state_ratio_zoom):
#     for rectangle_id in Rectangles_Ids_List:
#         coords = canvas.coords(rectangle_id)
#         new_coords = [coords[i] * state_ratio_zoom for i in range(4)]
#         canvas.coords(rectangle_id, *new_coords)

def ResetAllRectangles():
    global Rectangles_Coordonates_List,Rectangles_Ids_List,Display_Revert_Button
    if Display_Revert_Button == 1 :
        Display_Revert_Button = 0
        for rectangle in Rectangles_Ids_List:
            canvas.delete(rectangle)
        canvas.update()
        Rectangles_Coordonates_List = []
        Rectangles_Ids_List = []
        Answer = Import.Info_Reset_Tab2()
        if Answer == "yes":
            Reset()
    else:
        Reset()

def Reset():
    global Picture_Size, Picture_Resized,Picture_Reduction_Ratio
    InitValues()
    Picture_Size = None
    Picture_Resized = None
    Picture_Reduction_Ratio = None

    Button_Select_File.config(state="normal")
    Button_Reset.config(state="disabled")
    canvas.delete("all")

    HideScrollbars()
    #------BUTTON ZOOM +  ARE RESETED
    Zoom_Buttons[0][0].configure(state=Import.tk.DISABLED)
    Zoom_Buttons[1][0].configure(state=Import.tk.DISABLED)
    Boutons_ControleTab2[1][0].configure(state=Import.tk.DISABLED)
    Zoom_Buttons[2][0].configure(state=Import.tk.DISABLED)

def ReplacePixelRectangles(image, liste_coordonnees):
    Current_Rectangle = 0
    Number_Of_Rectangles = len(liste_coordonnees)
    for coordonnees in liste_coordonnees:
        Current_Rectangle = Current_Rectangle  + 1
        x1, y1, x2, y2 = coordonnees
        
        #If picture is narrower than canvas, we do not apply recalculation of the Rectangles_Ids_List positions
        if int(Picture_Reduction_Ratio) != 0: x1, y1, x2, y2 = [int(coord * Picture_Reduction_Ratio) for coord in (x1, y1, x2, y2)]
        # Loop de replace pixels under Rectangles_Ids_List
      
        for x in range(int(x1), int(x2) + 1):
            for y in range(int(y1), int(y2) + 1):
                # modify pixels by black pixels
                image.putpixel((x, y), (0, 0, 0))  # Met les pixels en vert
        Process_Text = (str(Current_Rectangle)+" zones d'offuscation traitées sur " + str(Number_Of_Rectangles) + " zones créés")
        print((Process_Text) if debug ==1 else "")
        Import.UpdateProcessing(Process_Text)
    return image

def Save(Extension,Format):
    if (Selected_Picture is None):
        Import.messagebox.showinfo("Erreur", "Selectionnez une image")
    else :
        global File_Path,Final_File_Name, Picture_Size
        Final_Saved_Picture = Image.open(File_Path)
        largeur, hauteur = Final_Saved_Picture.size
        print((largeur, hauteur) if debug == 1 else "")
        Import.DisplayProcessing(Import.Tab2DisplayWindow_x_position,Import.Tab2DisplayWindow_y_position,Import.Tab2DisplayWindow_width,Import.Tab2DisplayWindow_Height,tab2) #Call process
        Final_Saved_Picture = ReplacePixelRectangles(Selected_Picture, Rectangles_Coordonates_List)
        Import.UpdateProcessing("Enregistrement du fichier ...")
        Final_Saved_Picture.save(Final_File_Name+ Extension, Format)
        Import.UpdateProcessing("Fichier enregistré !")
        Import.Info_FileSaved()
        Import.HideProcessing()

#Function Zoom is called when both button zoom + or button -. They send "*" or // depend on zoom + or zoom -
def Zoom(op):
    global Picture_Width, Picture_Height, canvas, Picture_Size
    global Picture_Best_Height,Picture_Best_Width #share new size of picture
    global Zoom_Incrementation,Picture_Zoom_Ratio #know zoom on picture

    Picture_Zoom_Ratio=2
    
    if Selected_Picture is not None:
        if(op == "//"):
            Zoom_Incrementation = Zoom_Incrementation  - 2
            Picture_Best_Width = Picture_Best_Width // Picture_Zoom_Ratio 
            Picture_Best_Height = Picture_Best_Height // Picture_Zoom_Ratio

        elif(op=="*"):
           
            Zoom_Incrementation = Zoom_Incrementation  + 2
            
            Picture_Best_Width = Picture_Best_Width * Picture_Zoom_Ratio 
            Picture_Best_Height = Picture_Best_Height * Picture_Zoom_Ratio 
        if(Zoom_Incrementation<=-2):
            Zoom_Buttons[0][0].configure(state=Import.tk.NORMAL)
            Zoom_Buttons[1][0].configure(state=Import.tk.DISABLED)
        elif(Zoom_Incrementation>=6):
            Zoom_Buttons[0][0].configure(state=Import.tk.DISABLED)
            Zoom_Buttons[1][0].configure(state=Import.tk.NORMAL)
        else:
            Zoom_Buttons[0][0].configure(state=Import.tk.NORMAL)
            Zoom_Buttons[1][0].configure(state=Import.tk.NORMAL)

        # Redimensionner l'image
        print("Zoom_Incrementation: ",Zoom_Incrementation)
        Picture_Zoomed = Selected_Picture.resize((Picture_Best_Width, Picture_Best_Height))
        Picture_Width, Picture_Height = Picture_Zoomed.size
        print("Picture_Width: ", Picture_Width,"Picture_Height: ", Picture_Height)

        # Convertir l'image redimensionnée en PhotoImage
        Picture_Size = ImageTk.PhotoImage(Picture_Zoomed)

        # Mettre à jour l'image dans le canevas
        canvas.itemconfig(Updated_Picture, image=Picture_Size)
        ScrollBarLenghCalculation()

# Enregistrement du module d'ouverture pour le format HEIC
Import.register_heif_opener()


def DisplaySelectedPicture(result):
    global Updated_Picture, canvas, Picture_Size  # Assurez-vous d'avoir déclaré la variable Picture_Size comme globale
    global Selected_Picture,Picture_Size,Picture_Resized, Picture_Width, Picture_Height
    global Picture_Best_Width,Picture_Best_Height # Share init size of the picture we are displaying. Values will be use by zooms functions
    global Picture_Reduction_Ratio,Zoom_Incrementation # use for pixel selection scalling 

    Selected_Picture = Image.open(result)

    #Get selected picture size.
    Picture_Width, Picture_Height = Selected_Picture.size

    #Calculate how to ajust the picture size in the UI
    Picture_Reduction_Ratio = (Picture_Width/Import.Tab2DisplayWindow_width)
    # Zoom_Incrementation = Picture_Reduction_Ratio
    print(("Picture_Reduction_Ratio brut : ",Picture_Reduction_Ratio) if debug ==1 else "")
    print(("Picture_Reduction_Ratio int() : ",int(Picture_Reduction_Ratio)) if debug ==1 else "")
    #If picture width is already smaller than table width, picture size is not modifed.
    if int(Picture_Reduction_Ratio)==0:
        Picture_Best_Width = Picture_Width 
        Picture_Best_Height = Picture_Height
    #Else Picture is ajusted
    else:
        Picture_Best_Width = int(Picture_Width // Picture_Reduction_Ratio)
        Picture_Best_Height = int(Picture_Height // Picture_Reduction_Ratio)
    Picture_Resized = Selected_Picture.resize((Picture_Best_Width, Picture_Best_Height))

    # Convert the resized image to a PhotoImage object
    Picture_Size = ImageTk.PhotoImage(Picture_Resized)

    # Add the image to the Canvas
    Updated_Picture = canvas.create_image(0, 0, anchor="nw", image=Picture_Size)
    ScrollBarLenghCalculation()
        
def ScrollBar():
    global Scrollbar_x_Direction,Scrollbar_y_Direction
        # Add horizontal scrollbar
    Scrollbar_x_Direction = Import.tk.Scrollbar(canvas, orient="horizontal", command=canvas.xview)
    canvas.configure(xscrollcommand=Scrollbar_x_Direction.set)

    # Add vertical scrollbar
    Scrollbar_y_Direction = Import.tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=Scrollbar_y_Direction.set)

def ScrollBarLenghCalculation():
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

def MouseMouvement(event):
    global Last_x_Mouse_Position, Last_y_Mouse_Position
    x = event.x_root
    y = event.y_root
    delta_x = x - Last_x_Mouse_Position
    delta_y = y - Last_y_Mouse_Position
    if delta_x > 0:
        canvas.xview_scroll(-1, "units")  # Défilement vers la gauche
    elif delta_x < 0:
        canvas.xview_scroll(1, "units")   # Défilement vers la droite
    if delta_y > 0:
        canvas.yview_scroll(-1, "units")  # Défilement vers le haut
    elif delta_y < 0:
        canvas.yview_scroll(1, "units")   # Défilement vers le bas
    Last_x_Mouse_Position = x
    Last_y_Mouse_Position = y

def MousewheelMouvement(event):
    if event.delta > 0:
        canvas.yview_scroll(-1, "units")  # Défilement vers le haut
    else:
        canvas.yview_scroll(1, "units")   # Défilement vers le bas
    

def ChooseFile():
    global canvas, txt,tab2SelectedImg,Button_Reset,Button_Select_File
    global Place_Zoom_Buttons_Only_Once #Know if zoom btns have already been positionned
    global File_Path,Final_File_Name # use for save function
    global Extension,Format # Use to send format and extension to save modified picture with same format as original picture
    result = Import.filedialog.askopenfilename(title="Sélectionner une image", filetypes= Import.filetypes)
    print("Mon resulat : ", result)
    # Vérifier si le fichier est au format .heic
    _, extension = Import.os.path.splitext(result)
        
    if(result==''):
        print("pas d'image selectionnées")
        tab2SelectedImg = 0 
        Button_Reset.config(state="disabled")
    
    else : 
        Button_Reset.config(state="normal")
        Button_Select_File.config(state="disabled")
        tab2SelectedImg = 1 
        File_Path=result

    #-------Selection du nom sans extension .png ou .jpg
        File_Name_Splited = result.split('.')
        File_Name_Without_Format = File_Name_Splited[0]
    #-------Nom identique lors de la sauvegadre avec ajout de "- Transparent"
        Final_File_Name= File_Name_Without_Format + " - Obfuscated"
        if extension.lower() == '.heic':
            Extension,Format = ".heic" , "png"
        elif extension.lower() == '.jpg':
            Extension,Format = ".jpg" , "png"
        else:
            Extension,Format = ".png" , "png"

        DisplaySelectedPicture(result)
        canvas.delete(txt) #Suppression de l'écriture bleu en cas de chargement d'une image transparente
        ScrollBarLenghCalculation()
        ShowScrollbars()

        Zoom_Buttons[0][0].configure(state=Import.tk.NORMAL)
        Zoom_Buttons[1][0].configure(state=Import.tk.NORMAL)
        Boutons_ControleTab2[1][0].configure(state=Import.tk.NORMAL)
        #Disable zoom For current Milestone
        Zoom_Buttons[0][0].configure(state=Import.tk.DISABLED)
        Zoom_Buttons[1][0].configure(state=Import.tk.DISABLED)

        if (Place_Zoom_Buttons_Only_Once == 0 ): #Bloquer la repetitiuon d'ajoute  des boutons zoom
            Import.PlaceButtonsAutomaticaly(Zoom_Buttons,Import.Zoom_Buttons_Init_y_Position,Import.Zoom_Buttons_Width,Import.Zoom_Buttons_Height,Import.Space_Between_Zoom_Buttons,Import.Picture_Reducer_Value,x_Position_Recalculated_For_Zoom_Buttons,Import.Police_Size,TextDisplay=0,Init_State=0)
            Place_Zoom_Buttons_Only_Once = 1

def ZoomButtonsPositionCalculation():
    global x_Position_Recalculated_For_Zoom_Buttons
    Number_Of_Buttons = len(Zoom_Buttons)
    Space_Took_By_Zoom_Buttons = Number_Of_Buttons * (Import.Zoom_Buttons_Width+Import.Space_Between_Zoom_Buttons)
    Free_Space = Import.Tab2DisplayWindow_width - (Space_Took_By_Zoom_Buttons)
    if(Free_Space>0):
        x_Position_Recalculated_For_Zoom_Buttons = Import.Tab2DisplayWindow_x_position + (Free_Space / 2)

    else:
        Extra_Buttons_Space = Space_Took_By_Zoom_Buttons - Import.Tab2DisplayWindow_x_position
        x_Position_Recalculated_For_Zoom_Buttons = Import.Tab2DisplayWindow_x_position - (Extra_Buttons_Space / 2)

    return x_Position_Recalculated_For_Zoom_Buttons

def PictureOffuscationTab(master,root):
    InitValues()
    global canvas, txt
    global Button_Reset,Button_Select_File,Button_Revert
    global tab2
    global Zoom_Buttons,x_Position_Recalculated_For_Zoom_Buttons
    global Boutons_ControleTab2 # Used to active or disable button depend on UI actions
    tab2 = Import.ttk.Frame(master)

    Icon_Add_File = Import.PhotoImage(file=Import.Ressource_Path("Pictures/AddFile.png"))
    Icon_Reset = Import.PhotoImage(file=Import.Ressource_Path("Pictures/Reset.png"))
    Icon_Exit = Import.PhotoImage(file=Import.Ressource_Path("Pictures/Exit.png"))
    Icon_Test = Import.PhotoImage(file=Import.Ressource_Path("Pictures/test.png"))
    Icon_Validate = Import.PhotoImage(file=Import.Ressource_Path("Pictures/Valider.png"))

    Icon_Zoom_More = Import.PhotoImage(file=Import.Ressource_Path("Pictures/zoomPlus.png"))
    Icon_Zoom_Less = Import.PhotoImage(file=Import.Ressource_Path("Pictures/zoomMoins.png"))
    Icon_Revert = Import.PhotoImage(file=Import.Ressource_Path("Pictures/Revert.png"))

    Button_Select_File = Import.tk.Button(tab2) ; Button_Validate = Import.tk.Button(tab2) 
    Button_Test = Import.tk.Button(tab2) ; Button_Reset=Import.tk.Button(tab2)
    Button_Exit = Import.tk.Button(tab2) 
    Button_Zoom_More = Import.tk.Button(tab2) ; Button_Zoom_Less = Import.tk.Button(tab2) 
    Button_Revert = Import.tk.Button(tab2)

    canvas = Import.tk.Canvas(tab2, highlightthickness=1, highlightbackground="black")
    canvas.place(x=Import.Tab2DisplayWindow_x_position, y=Import.Tab2DisplayWindow_y_position,width=Import.Tab2DisplayWindow_width, height=Import.Tab2DisplayWindow_Height)
    # canvas.bind("<Button-1>", click_on_canvas)
    txt = canvas.create_text(300, 200, text="Selectionnez une image", font="Arial 16 italic", fill="blue")

    ScrollBar()
    Boutons_ControleTab2 = [
        [Button_Select_File, "Add file",Icon_Add_File, ChooseFile,Import.tk.NORMAL ],
        [Button_Validate, "Valider",Icon_Validate, lambda: Save(Extension,Format),Import.tk.DISABLED],
        # [Btn_ConvertirTab2, "Convertir",img_ConvertTab2, test,tk.DISABLED],
        [Button_Reset, "Reset",Icon_Reset, ResetAllRectangles,Import.tk.DISABLED],
        [Button_Exit, "Quitter",Icon_Exit, root.destroy,Import.tk.NORMAL],        
        # [Button_Test, "Test",Icon_Test, HideProcessing, tk.NORMAL],
    ]

    # Boucle placement des bouttons
    Position_x_recalculeeTab2,Position_y_recalculeeTab2 = Import.ControlsButtonsInitPositionCalculation(Boutons_ControleTab2,Import.Tab2Canvas,offset=30)
    Import.PlaceButtonsAutomaticaly(Boutons_ControleTab2,Position_y_recalculeeTab2,Import.Control_Button_Width,Import.Control_Button_Height,Import.Space_Between_Button,Import.Picture_Reducer_Value,Position_x_recalculeeTab2,Import.Police_Size,TextDisplay=1,Init_State=1)

    Zoom_Buttons = [
        [Button_Zoom_More, "Zoomer",Icon_Zoom_More, lambda: Zoom("*") ],
        [Button_Zoom_Less, "Dézoomer",Icon_Zoom_Less, lambda: Zoom("//")],
        [Button_Revert, "Revert",Icon_Revert, RevertRectangles],
    ]

    x_Position_Recalculated_For_Zoom_Buttons = ZoomButtonsPositionCalculation()
    print(("x_Position_Recalculated_For_Zoom_Buttons :", x_Position_Recalculated_For_Zoom_Buttons) if debug == 1 else "")

    canvas.bind("<MouseWheel>", MousewheelMouvement)
    canvas.bind("<Button-2>", HorizontalMouvement)
    canvas.bind("<B2-Motion>", MouseMouvement)
    canvas.bind("<Motion>", UpdateRectangleDrawing)
    canvas.bind("<Button-1>", StartRectangleDrawing)
    canvas.bind("<ButtonRelease-1>", FinishRectangleDrawing)

    return tab2
    