import SharedFunctions.imports as Import
from tkinter import colorchooser
from Tabs.Tab_Watermark.CreateWatermarkLayer import DisplayText
from SharedFunctions.imports import AppLanguages

Texte_From_Json=Import.LoadText()

class EditingCanvas:
    IsDiplayed = 0

def AddEditingCanvas(master,Display_Window_x_position,Displa_yWindow_y_position,Display_Window_Width,Display_Window_Height,tab):
    global Cursors_Transparency, Cursors_Font_Size, Text_Input_Watermark_Text, Cursors_Space_Between_Text
    global Editing_Canvas
    Editing_Canvas = Import.tk.Canvas(master, width=Display_Window_Width, height=Display_Window_Height, bg='lightgray')
    Editing_Canvas.place(x=Display_Window_x_position,y=Displa_yWindow_y_position)

    # Créer un cadre pour les widgets
    frame = Import.tk.Frame(Editing_Canvas, bg='lightgray')
    Editing_Canvas.create_window(200, 200, window=frame)
    frame.pack(pady=20, padx=20)

    # Ajouter le bouton au cadre
    button = Import.tk.Button(frame, text=Texte_From_Json["Tab3"]["Edit_Watermark_Text"]["WaterMark_Color"][AppLanguages.Language], command=choose_color)
    button.grid(row=0, column=0, columnspan=2, pady=10)

    # Ajouter le premier curseur (Cursors_Transparency) au cadre
    curseur1_label = Import.tk.Label(frame, text=Texte_From_Json["Tab3"]["Edit_Watermark_Text"]["WaterMark_Transparency"][AppLanguages.Language], bg='lightgray')
    curseur1_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
    Cursors_Transparency = Import.tk.Scale(frame, from_=1, to=100, orient=Import.tk.HORIZONTAL, bg='lightgray')
    Cursors_Transparency.grid(row=1, column=1, padx=5, pady=5, sticky='w')

    # Ajouter le deuxième curseur (Cursors_Font_Size) au cadre
    curseur2_label = Import.tk.Label(frame, text=Texte_From_Json["Tab3"]["Edit_Watermark_Text"]["WaterMark_FontSize"][AppLanguages.Language], bg='lightgray')
    curseur2_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')
    Cursors_Font_Size = Import.tk.Scale(frame, from_=0, to=100, orient=Import.tk.HORIZONTAL, bg='lightgray')
    Cursors_Font_Size.grid(row=2, column=1, padx=5, pady=5, sticky='w')

    curseur3_label = Import.tk.Label(frame, text=Texte_From_Json["Tab3"]["Edit_Watermark_Text"]["WaterMark_Space_Between_Text"][AppLanguages.Language], bg='lightgray')
    curseur3_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')
    Cursors_Space_Between_Text = Import.tk.Scale(frame, from_=25, to=300, orient=Import.tk.HORIZONTAL, bg='lightgray')
    Cursors_Space_Between_Text.grid(row=3, column=1, padx=5, pady=5, sticky='w')

    # Ajouter une entrée de texte (TexteInput) au cadre
    texte_input_label = Import.tk.Label(frame, text=Texte_From_Json["Tab3"]["Edit_Watermark_Text"]["WaterMark_Text"][AppLanguages.Language], bg='lightgray')
    texte_input_label.grid(row=4, column=0, padx=5, pady=5, sticky='e')
    Text_Input_Watermark_Text = Import.tk.Entry(frame)
    Text_Input_Watermark_Text.grid(row=4, column=1, padx=5, pady=5, sticky='w')

    # Ajouter les boutons Annuler et Valider au cadre
    annuler_button = Import.tk.Button(frame,text=Texte_From_Json["Tab3"]["Edit_Watermark_Buttons"]["Cancel"][AppLanguages.Language], command=CancelCanvasEditing)
    annuler_button.grid(row=5, column=0, padx=10, pady=10)

    valider_button = Import.tk.Button(frame, text=Texte_From_Json["Tab3"]["Edit_Watermark_Buttons"]["Validate"][AppLanguages.Language], command=valider_clicked)
    valider_button.grid(row=5, column=1, padx=10, pady=10)

    close_button = Import.tk.Button(frame, text=Texte_From_Json["Tab3"]["Edit_Watermark_Buttons"]["Close"][AppLanguages.Language], command=HideEditingCanvas)
    close_button.grid(row=5, column=2, padx=10, pady=10)

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
    print(Color_Input_Watermark_Color)
    print(type(Color_Input_Watermark_Color))


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
    
    Import.Watermark.Lines_Coordonate = []
    Import.Watermark.Transparency = Import.TransparencyCrossProduct(Cursors_Transparency.get(),"From_Slider")
    Import.Watermark.Font_Size = Cursors_Font_Size.get()
    Import.Watermark.Text = Text_Input_Watermark_Text.get()

    if Color_Input_Watermark_Color != Import.Watermark.Color : Import.Watermark.Color = Color_Input_Watermark_Color[0]
    Import.Watermark.Space_Between_Text = Cursors_Space_Between_Text.get()
    DisplayText(Import.Watermark.Canvas)
    EditingCanvas.IsDiplayed=0
