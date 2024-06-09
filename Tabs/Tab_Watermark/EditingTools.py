import SharedFunctions.imports as Import
from tkinter import colorchooser
from Tabs.Tab_Watermark.CreateWatermarkLayer import DisplayText
from SharedFunctions.imports import AppLanguages

Texte_From_Json=Import.LoadText()

class EditingCanvas:
    IsDiplayed = 0



def AddEditingCanvas(master,x_Position,y_Position,Width,Height):
    global Cursors_Transparency, Cursors_Font_Size, Text_Input_Watermark_Text, Cursors_Space_Between_Text
    global Editing_Canvas
    global Color_Button
    Editing_Canvas = Import.tk.Canvas(master, width=Width, height=Height, bg='lightgray',highlightthickness=1, highlightbackground="black")
    Editing_Canvas.place(x=x_Position,y=y_Position)

    # Créer un cadre pour les widgets
    frame = Import.tk.Frame(Editing_Canvas, bg='lightgray')
    frame.place(relx=0.5, rely=0.5, anchor=Import.tk.CENTER)
    # Editing_Canvas.create_window(Import.Tab3DisplayWindow_width, 200, window=frame)
    # frame.pack(pady=20, padx=20)

    # Ajouter le premier curseur (Cursors_Transparency) au cadre
    Cursors_Transparency_label = Import.tk.Label(frame, text=Texte_From_Json["Tab3"]["Edit_Watermark_Text"]["WaterMark_Transparency"][AppLanguages.Language], bg='lightgray')
    Cursors_Transparency = Import.tk.Scale(frame, from_=5, to=100, orient=Import.tk.HORIZONTAL, bg='lightgray',resolution=5)

    # Ajouter le deuxième curseur (Cursors_Font_Size) au cadre
    Cursors_Font_Size_label = Import.tk.Label(frame, text=Texte_From_Json["Tab3"]["Edit_Watermark_Text"]["WaterMark_FontSize"][AppLanguages.Language], bg='lightgray')
    Cursors_Font_Size = Import.tk.Scale(frame, from_=10, to=100, orient=Import.tk.HORIZONTAL, bg='lightgray',resolution=5)

    Cursors_Space_Between_Text_label = Import.tk.Label(frame, text=Texte_From_Json["Tab3"]["Edit_Watermark_Text"]["WaterMark_Space_Between_Text"][AppLanguages.Language], bg='lightgray')
    Cursors_Space_Between_Text = Import.tk.Scale(frame, from_=20, to=300, orient=Import.tk.HORIZONTAL, bg='lightgray',resolution=10)

    # Ajouter une entrée de texte (TexteInput) au cadre
    Text_Input_Watermark_Text_label = Import.tk.Label(frame, text=Texte_From_Json["Tab3"]["Edit_Watermark_Text"]["WaterMark_Text"][AppLanguages.Language], bg='lightgray')
    Text_Input_Watermark_Text = Import.tk.Text(frame, height=2, width=15)

    # Ajouter les boutons Annuler et Valider au cadre
    Cancel_Button = Import.tk.Button(frame,text=Texte_From_Json["Tab3"]["Edit_Watermark_Buttons"]["Cancel"][AppLanguages.Language], command=CancelCanvasEditing)
    Validate_Button = Import.tk.Button(frame, text=Texte_From_Json["Tab3"]["Edit_Watermark_Buttons"]["Preview"][AppLanguages.Language],width=8,height=2, command=valider_clicked )
    Close_Button = Import.tk.Button(frame, text=Texte_From_Json["Tab3"]["Edit_Watermark_Buttons"]["Close"][AppLanguages.Language],width=8,height=2, command=HideEditingCanvas)
    Color_Button = Import.tk.Button(frame, text=Texte_From_Json["Tab3"]["Edit_Watermark_Text"]["WaterMark_Color"][AppLanguages.Language],width=16, command=choose_color, bg= Import.Watermark.Display_Color)
 # Arrange widgets in the frame
    Text_Input_Watermark_Text_label.grid(row=0, column=0)
    Text_Input_Watermark_Text.grid(row=1, column=0, rowspan=2, sticky="n")

    Cursors_Transparency_label.grid(row=0, column=1)
    Cursors_Font_Size_label.grid(row=0, column=2)
    Cursors_Space_Between_Text_label.grid(row=0, column=3)

    Cursors_Transparency.grid(row=1, column=1)
    Cursors_Font_Size.grid(row=1, column=2)
    Cursors_Space_Between_Text.grid(row=1, column=3)

    Color_Button.grid(row=0,columnspan=3, column=4, sticky="n")

    # Cancel_Button.grid(row=0, column=5, sticky="n")
    Validate_Button.grid(row=1, column=5,rowspan=2, sticky="n")
    Close_Button.grid(row=1, column=6,rowspan=2, sticky="n")

    InitEditingCanvas()

def HideEditingCanvas():
    Editing_Canvas.place_forget()
    EditingCanvas.IsDiplayed=0
 
# Function that will be invoked when the
# button will be clicked in the main window
def choose_color():
    global Color_Input_Watermark_Color
    # variable to store hexadecimal code of color
    Color_Input_Watermark_Color = colorchooser.askcolor(title ="Choose color") 
    if Import.debug==1 :print(Color_Input_Watermark_Color)
    if Import.debug==1 :print(type(Color_Input_Watermark_Color))
    Import.Watermark.Display_Color = Color_Input_Watermark_Color[1]
    Color_Button.config(bg=Import.Watermark.Display_Color)

def InitEditingCanvas():
    global Color_Input_Watermark_Color
    Color_Input_Watermark_Color = Import.Watermark.Color
    Cursors_Transparency.set(Import.TransparencyCrossProduct(Import.Watermark.Transparency,"From_RealValue"))
    Cursors_Font_Size.set(Import.Watermark.Font_Size)
    Cursors_Space_Between_Text.set(Import.Watermark.Space_Between_Text)
    Text_Input_Watermark_Text.insert(Import.tk.END, Import.Watermark.Text)
    
def CancelCanvasEditing():  
    InitEditingCanvas()
    HideEditingCanvas()
    EditingCanvas.IsDiplayed=0

def valider_clicked():
    Import.DisplayProcessing(Import.Tab3DisplayWindow_x_position,Import.Tab3DisplayWindow_y_position,Import.Tab3DisplayWindow_width,Import.Tab3DisplayWindow_Height,Import.tab3) #Call process
    Import.UpdateProcessing(Texte_From_Json["MessageBox"]["Message"]["LoadingTime"][AppLanguages.Language])
    Import.Watermark.Lines_Coordonate = []
    Import.Watermark.Transparency = Import.TransparencyCrossProduct(Cursors_Transparency.get(),"From_Slider")
    Import.Watermark.Font_Size = Cursors_Font_Size.get()
    # Import.Watermark.Text = Text_Input_Watermark_Text.get()
    Import.Watermark.Text = Text_Input_Watermark_Text.get("1.0", Import.tk.END).strip() # strip() to remove any extra newlines # pécifient les positions du texte que vous souhaitez récupérer. Pour récupérer tout le contenu du widget Text, vous pouvez utiliser "1.0" (le début du texte) et "end" (la fin du texte).

    if Color_Input_Watermark_Color != Import.Watermark.Color : 
        Import.Watermark.Color = Color_Input_Watermark_Color[0]  
        Import.Watermark.Display_Color = Color_Input_Watermark_Color[1]  

    Import.Watermark.Space_Between_Text = Cursors_Space_Between_Text.get()
    DisplayText(Import.Watermark.Canvas)
    EditingCanvas.IsDiplayed=0
    Import.HideProcessing()
