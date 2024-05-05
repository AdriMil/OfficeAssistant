from SharedFunctions.imports import *
from PIL import Image
from PIL import ImageTk  

def InitValues():
    global Selected_Picture, Place_Zoom_Buttons_Only_Once, x_Position_Recalculated_For_Zoom_Buttons, Zoom_Incrementation, Rectangles_Coordonates_List, Rectangles_Ids_List, Current_Rectangle_Id, First_Clic_x_Location, First_Clic_y_Location
    Selected_Picture = None
    Place_Zoom_Buttons_Only_Once = 0 #
    x_Position_Recalculated_For_Zoom_Buttons = 0 
    Zoom_Incrementation = 0
    Rectangles_Coordonates_List = [] 
    Rectangles_Ids_List = [] # Store rectangle's id
    Current_Rectangle_Id = None # Store current rectangle's id
    First_Clic_x_Location = None #Store first clic x locatoin
    First_Clic_y_Location = None #Store first clic y locatoin

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
    global First_Clic_x_Location, First_Clic_y_Location, Rectangles_Ids_List,Rectangles_Coordonates_List
    if First_Clic_x_Location is not None and First_Clic_y_Location is not None:
        x_image = event.x + canvas.canvasx(0)
        y_image = event.y + canvas.canvasy(0)
        Rectangles_Ids_List.append(Current_Rectangle_Id)
        First_Clic_x_Location, First_Clic_y_Location,x_image,y_image = FixValues(First_Clic_x_Location, First_Clic_y_Location,x_image,y_image)
        Rectangles_Coordonates_List.append([First_Clic_x_Location, First_Clic_y_Location,x_image,y_image])
        print((Rectangles_Coordonates_List) if debug==1 else "")
    First_Clic_x_Location = None
    First_Clic_y_Location = None

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

def Reset():
    global Selected_Picture, Picture_Size, Picture_Resized,Picture_Reduction_Ratio
    InitValues()
    Picture_Size = None
    Picture_Resized = None
    Picture_Reduction_Ratio

    Button_Select_File.config(state="normal")
    Button_Reset.config(state="disabled")
    canvas.delete("all")

    HideScrollbars()
    #------BUTTON ZOOM +  ARE RESETED
    Zoom_Buttons[0][0].configure(state=tk.DISABLED)
    Zoom_Buttons[1][0].configure(state=tk.DISABLED)
    Boutons_ControleTab2[1][0].configure(state=tk.DISABLED)

def ReplacePixelRectangles(image, liste_coordonnees):
    for coordonnees in liste_coordonnees:
        x1, y1, x2, y2 = coordonnees
        
        #If picture is narrower than canvas, we do not apply recalculation of the Rectangles_Ids_List positions
        if int(Picture_Reduction_Ratio) != 0: x1, y1, x2, y2 = [int(coord * Picture_Reduction_Ratio) for coord in (x1, y1, x2, y2)]
        # Loop de replace pixels under Rectangles_Ids_List
        for x in range(int(x1), int(x2) + 1):
            for y in range(int(y1), int(y2) + 1):
                # modify pixels by black pixels
                image.putpixel((x, y), (0, 0, 0))  # Met les pixels en vert
    return image

def Save():
    global Selected_Picture
    if (Selected_Picture is None):
        messagebox.showinfo("Erreur", "Selectionnez une image")
    else :
        global File_Path,Final_File_Name, Picture_Size
        Final_Saved_Picture = Image.open(File_Path)
        largeur, hauteur = Final_Saved_Picture.size
        print((largeur, hauteur) if debug == 1 else "")

        Final_Saved_Picture = ReplacePixelRectangles(Selected_Picture, Rectangles_Coordonates_List)
        Final_Saved_Picture.save(Final_File_Name+".png", "PNG")

#Function Zoom is called when both button zoom + or button -. They send "*" or // depend on zoom + or zoom -
def Zoom(op):
    global Selected_Picture, Picture_Width, Picture_Height, canvas, Updated_Picture, Picture_Size
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
            Zoom_Buttons[0][0].configure(state=tk.NORMAL)
            Zoom_Buttons[1][0].configure(state=tk.DISABLED)
        elif(Zoom_Incrementation>=6):
            Zoom_Buttons[0][0].configure(state=tk.DISABLED)
            Zoom_Buttons[1][0].configure(state=tk.NORMAL)
        else:
            Zoom_Buttons[0][0].configure(state=tk.NORMAL)
            Zoom_Buttons[1][0].configure(state=tk.NORMAL)

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


def DisplaySelectedPicture(result):
    global Updated_Picture, canvas, Picture_Size  # Assurez-vous d'avoir déclaré la variable Picture_Size comme globale
    global Selected_Picture,Picture_Size,Picture_Resized, Picture_Width, Picture_Height
    global Picture_Best_Width,Picture_Best_Height # Share init size of the picture we are displaying. Values will be use by zooms functions
    global Picture_Reduction_Ratio,Zoom_Incrementation # use for pixel selection scalling 
    # Load an image from the file path
    Selected_Picture = Image.open(result)

    #Get selected picture size.
    Picture_Width, Picture_Height = Selected_Picture.size

    #Calculate how to ajust the picture size in the UI
    Picture_Reduction_Ratio = (Picture_Width/Tab2DisplayWindow_width)
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
    Scrollbar_x_Direction = tk.Scrollbar(canvas, orient="horizontal", command=canvas.xview)
    canvas.configure(xscrollcommand=Scrollbar_x_Direction.set)

    # Add vertical scrollbar
    Scrollbar_y_Direction = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=Scrollbar_y_Direction.set)

def ScrollBarLenghCalculation():
    canvas.config(scrollregion=canvas.bbox(tk.ALL))

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
        canvas.Scroll_On_x_Direction(-1, "units")  # Défilement vers la gauche
    elif delta_x < 0:
        canvas.Scroll_On_x_Direction(1, "units")   # Défilement vers la droite
    if delta_y > 0:
        canvas.Scroll_On_y_Direction(-1, "units")  # Défilement vers le haut
    elif delta_y < 0:
        canvas.Scroll_On_y_Direction(1, "units")   # Défilement vers le bas
    Last_x_Mouse_Position = x
    Last_y_Mouse_Position = y

def MousewheelMouvement(event):
    if event.delta > 0:
        canvas.Scroll_On_y_Direction(-1, "units")  # Défilement vers le haut
    else:
        canvas.Scroll_On_y_Direction(1, "units")   # Défilement vers le bas
    

def ChooseFile():
    global canvas, txt,tab2SelectedImg,Button_Reset,Button_Select_File
    global Place_Zoom_Buttons_Only_Once #Know if zoom btns have already been positionned
    global File_Path,Final_File_Name # use for save function
    result = filedialog.askopenfilename()
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

        DisplaySelectedPicture(result)
        canvas.delete(txt) #Suppression de l'écriture bleu en cas de chargement d'une image transparente
        ScrollBarLenghCalculation()
        ShowScrollbars()

        Zoom_Buttons[0][0].configure(state=tk.NORMAL)
        Zoom_Buttons[1][0].configure(state=tk.NORMAL)
        Boutons_ControleTab2[1][0].configure(state=tk.NORMAL)
        #Disable zoom For current Milestone
        Zoom_Buttons[0][0].configure(state=tk.DISABLED)
        Zoom_Buttons[1][0].configure(state=tk.DISABLED)

        if (Place_Zoom_Buttons_Only_Once == 0 ): #Bloquer la repetitiuon d'ajoute  des boutons zoom
            PlaceButtonsAutomaticaly(Zoom_Buttons,Zoom_Buttons_Init_y_Position,Zoom_Buttons_Width,Zoom_Buttons_Height,Space_Between_Zoom_Buttons,Picture_Reducer_Value,x_Position_Recalculated_For_Zoom_Buttons,Police_Size,TextDisplay=0,Init_State=0)
            Place_Zoom_Buttons_Only_Once = 1

def ZoomButtonsPositionCalculation():
    global x_Position_Recalculated_For_Zoom_Buttons
    Number_Of_Buttons = len(Zoom_Buttons)
    Space_Took_By_Zoom_Buttons = Number_Of_Buttons * (Zoom_Buttons_Width+Space_Between_Zoom_Buttons)
    Free_Space = Tab2DisplayWindow_width - (Space_Took_By_Zoom_Buttons)
    if(Free_Space>0):
        x_Position_Recalculated_For_Zoom_Buttons = Tab2DisplayWindow_x_position + (Free_Space / 2)

    else:
        Extra_Buttons_Space = Space_Took_By_Zoom_Buttons - Tab2DisplayWindow_x_position
        x_Position_Recalculated_For_Zoom_Buttons = Tab2DisplayWindow_x_position - (Extra_Buttons_Space / 2)

    return x_Position_Recalculated_For_Zoom_Buttons

def PictureOffuscationTab(master,root):
    InitValues()
    global canvas, txt
    global Button_Reset,Button_Select_File
    global tab2
    global Zoom_Buttons,x_Position_Recalculated_For_Zoom_Buttons
    global Boutons_ControleTab2 # Used to active or disable button depend on UI actions
    tab2 = ttk.Frame(master)

    Icon_Add_File, Icon_Reset, Icon_Convert_To_Pdf, Icon_Exit, Icon_Test, Icon_Validate, Icon_Zoom_More, Icon_Zoom_Less, Icon_Arrow_Up, Icon_Arrow_Down, Icon_Delete_Selected_Line = IconsDeclaration() #Icons Declaration, cannot be perfomed above, must wait line tab2 = ttk.Frame(master) to get tkinter instance

    canvas = tk.Canvas(tab2, bg="white")
    canvas.place(x=Tab2DisplayWindow_x_position, y=Tab2DisplayWindow_y_position,width=Tab2DisplayWindow_width, height=Tab2DisplayWindow_Height)


    Button_Select_File = tk.Button(tab2) ; Button_Validate = tk.Button(tab2) 
    Button_Test = tk.Button(tab2) ; Button_Reset=tk.Button(tab2)
    Button_Exit = tk.Button(tab2) 

    canvas = tk.Canvas(tab2, highlightthickness=1, highlightbackground="black")
    canvas.place(x=Tab2DisplayWindow_x_position, y=Tab2DisplayWindow_y_position,width=Tab2DisplayWindow_width, height=Tab2DisplayWindow_Height)
    # canvas.bind("<Button-1>", click_on_canvas)
    txt = canvas.create_text(300, 200, text="Selectionnez une image", font="Arial 16 italic", fill="blue")

    ScrollBar()
    Boutons_ControleTab2 = [
        [Button_Select_File, "Add file",Icon_Add_File, ChooseFile,tk.NORMAL ],
        [Button_Validate, "Valider",Icon_Validate, Save,tk.DISABLED],
        # [Btn_ConvertirTab2, "Convertir",img_ConvertTab2, test,tk.DISABLED],
        [Button_Reset, "Reset",Icon_Reset, Reset,tk.DISABLED],
        [Button_Exit, "Quitter",Icon_Exit, root.destroy,tk.NORMAL],        
        # [Button_Test, "Test",Icon_Test, HideProcessing, tk.NORMAL],
    ]

    # Boucle placement des bouttons
    Position_x_recalculeeTab2,Position_y_recalculeeTab2 = ControlsButtonsInitPositionCalculation(Boutons_ControleTab2,Tab2Canvas,offset=30)
    
    PlaceButtonsAutomaticaly(Boutons_ControleTab2,Position_y_recalculeeTab2,Control_Button_Width,Control_Button_Height,Space_Between_Button,Picture_Reducer_Value,Position_x_recalculeeTab2,Police_Size,TextDisplay=1,Init_State=1)

    Button_Zoom_More = tk.Button(tab2) ; Button_Zoom_Less = tk.Button(tab2) 

    Zoom_Buttons = [
        [Button_Zoom_More, "Zoomer",Icon_Zoom_More, lambda: Zoom("*") ],
        [Button_Zoom_Less, "Dézoomer",Icon_Zoom_Less, lambda: Zoom("//")],
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
    