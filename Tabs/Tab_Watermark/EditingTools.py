import SharedFunctions.imports as Import
from tkinter import colorchooser

class EditingCanvas:
    IsDiplayed = 0

def AddEditingCanvas(master,Display_Window_x_position,Displa_yWindow_y_position,Display_Window_Width,Display_Window_Height,tab):
    # Créer un canevas
    global Editing_Canvas
    Editing_Canvas = Import.tk.Canvas(master, width=Display_Window_Width, height=Display_Window_Height, bg='lightgray')
    Editing_Canvas.place(x=Display_Window_x_position,y=Displa_yWindow_y_position)

    # Ajouter un bouton au canevas
    button_on_canvas = Import.tk.Button(Editing_Canvas, text="Click Me", command=choose_color)
    Editing_Canvas.create_window(100, 100, window=button_on_canvas)

def HideEditingCanvas():
    Editing_Canvas.place_forget()


 
# Function that will be invoked when the
# button will be clicked in the main window
def choose_color():
 
    # variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title ="Choose color") 
    print(color_code)