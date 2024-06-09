import SharedFunctions.imports as Import
from SharedFunctions.imports import AppLanguages
from Tabs.Tab_Watermark.EditingTools import AddEditingCanvas, HideEditingCanvas , EditingCanvas
from Tabs.Tab_Watermark.CreateWatermarkLayer import create_text_image, DisplayText
from PIL import Image, ImageTk, ImageDraw, ImageFont


#Define init Watermark text with today date
def WaterMarkInitText():
    current_date = Import.datetime.date.today()
    formatted_date = current_date.strftime("%d/%m/%Y")
    Import.Watermark.Text = (Texte_From_Json["Tab3"]["Init_Watermark_Text"][AppLanguages.Language] + formatted_date)



def TOBEDEFINEDAFRTERCANVASEDITING():
    user_input = Import.simpledialog.askstring(Texte_From_Json["Tab3"]["Edit_Watermark_Text"]["WindowName"][AppLanguages.Language], Texte_From_Json["Tab3"]["Edit_Watermark_Text"]["Instruction"][AppLanguages.Language], initialvalue=Import.Watermark.Text)
    if user_input is None:
        print(("L'utilisateur a cliqué sur Cancel.")if Import.debug == 1 else "")
    elif user_input:
        Import.DisplayProcessing(Import.Tab3DisplayWindow_x_position,Import.Tab3DisplayWindow_y_position,Import.Tab3DisplayWindow_width,Import.Tab3DisplayWindow_Height,tab3) #Call process
        Import.UpdateProcessing(Texte_From_Json["MessageBox"]["Message"]["LoadingTime"][AppLanguages.Language])

        Import.Watermark.Text = user_input
        canvas.delete(Superposed_Picture)
        Import.HideProcessing()
        DisplayText(canvas)
    else:
        Import.Error_EmptyField(Texte_From_Json,AppLanguages.Language)
        EditWatermarkText()


def EditWatermarkText():
    if EditingCanvas.IsDiplayed == 0 : 
        EditingCanvas.IsDiplayed = 1
        AddEditingCanvas(tab3,Import.Tab3DisplayWindow_x_position,Import.Tab3DisplayWindow_y_position,Import.Tab3DisplayWindow_width,Import.Tab3DisplayWindow_Height,tab3) #Call process
    else : 
        EditingCanvas.IsDiplayed = 0
        HideEditingCanvas()


def ReplacePixelRectangles(image, liste_coordonnees):
    global space_between_text_recalculated
    Current_Rectangle = 0 ; text_coordinates_recalculate = []
    Number_Of_Rectangles = len(liste_coordonnees)
    font_size_recalculated = int(Import.Watermark.Font_Size * Picture_Reduction_Ratio) if int(Picture_Reduction_Ratio) != 0 else Import.Watermark.Font_Size
    space_between_text_recalculated = int(Import.Watermark.Space_Between_Text * Picture_Reduction_Ratio) if int(Picture_Reduction_Ratio) != 0 else Import.Watermark.Space_Between_Text

    for coordonnees in liste_coordonnees:
        Current_Rectangle = Current_Rectangle  + 1
        x1, y1 = coordonnees
        
        #If picture is narrower than canvas, we do not apply recalculation of text positions
        if int(Picture_Reduction_Ratio) != 0: x1, y1 = [int(coord * Picture_Reduction_Ratio) for coord in (x1, y1)]
        text_coordinates_recalculate.append([x1,y1])
    print("Saving sptep texte coordonates recalculée: ", text_coordinates_recalculate)
    text_image = create_text_image(Import.Watermark.Text, Import.Font_Path, font_size_recalculated,Import.Watermark.Space_Between_Text, Import.Watermark.Color, Import.Watermark.Transparency, 100, Picture_Width, Picture_Height,text_coordinates_recalculate,Step= "saving")
    
    Process_Text = (str(Current_Rectangle)+Texte_From_Json["Processing"]["AreasProcessing"][AppLanguages.Language] + str(Number_Of_Rectangles) + Texte_From_Json["Processing"]["AreasNumber"][AppLanguages.Language])
    Import.UpdateProcessing(Process_Text)
    return text_image

def Save(Extension,Format):
    if (Selected_Picture is None):
        Import.Error_NoPicture(Texte_From_Json,AppLanguages.Language)
    else :
        Import.DisplayProcessing(Import.Tab3DisplayWindow_x_position,Import.Tab3DisplayWindow_y_position,Import.Tab3DisplayWindow_width,Import.Tab3DisplayWindow_Height,tab3) #Call process
        Import.UpdateProcessing(Texte_From_Json["Processing"]["FileSaving"][AppLanguages.Language])
        Final_Saved_Picture = Import.Image.open(File_Path)
        largeur, hauteur = Final_Saved_Picture.size
        print((largeur, hauteur) if Import.debug == 1 else "")
        Final_Saved_Picture = ReplacePixelRectangles(Selected_Picture, Import.Watermark.Lines_Coordonate)
        combined_image = Image.alpha_composite(Selected_Picture.convert("RGBA"), Final_Saved_Picture)
        Import.UpdateProcessing(Texte_From_Json["Processing"]["UpdateProcessing"][AppLanguages.Language])
        combined_image.save(Final_File_Name+ Extension, Format)
        Import.UpdateProcessing(Texte_From_Json["Processing"]["FinishFileSaving"][AppLanguages.Language])
        Import.Info_FileSaved(Texte_From_Json,AppLanguages.Language)
        Import.HideProcessing()

def Tab2UpdateLangages(Current_Language):
    Boutons_ControleTab3[0][0].update()
    
def InitValues():
    global Selected_Picture, text_coordinates
    global Extension,Format,text_coordinates_recalculate
    global space_between_text_recalculated
    global Picture_Size, Picture_Resized,Picture_Reduction_Ratio
    global Superposed_Picture
    Selected_Picture = None
    text_coordinates  = [] ; text_coordinates_recalculate  = [] 
    space_between_text_recalculated = None
    Picture_Size = None ; Picture_Resized = None ; Picture_Reduction_Ratio = None
    Extension,Format = "","" #Used to share between function kind of selected picture
    Superposed_Picture = None #Will be the displayed layer with watermark visible
    WaterMarkInitText() #Define init Watermark text with today date

def Reset():
    global Picture_Size, Picture_Resized,Picture_Reduction_Ratio
    InitValues()
    Button_Select_File.config(state="normal")
    Button_Reset.config(state="disabled")
    Button_Validate.config(state="disabled")
    Button_Text_Modification.config(state="disabled")
    canvas.delete("all")
    Import.HideScrollbars() 



# Enregistrement du module d'ouverture pour le format HEIC
Import.register_heif_opener()


def DisplaySelectedPicture(result):
    global Updated_Picture, canvas, Picture_Size  # Assurez-vous d'avoir déclaré la variable Picture_Size comme globale
    global Selected_Picture,Picture_Size,Picture_Resized, Picture_Width, Picture_Height
    global Picture_Best_Width,Picture_Best_Height # Share init size of the picture we are displaying. Values will be use by zooms functions
    global Picture_Reduction_Ratio # use for pixel selection scalling 

    Selected_Picture = Import.Image.open(result)

    #Get selected picture size.
    Picture_Width, Picture_Height = Selected_Picture.size
    Import.Watermark.Width = Picture_Width
    Import.Watermark.Height = Picture_Height

    if Import.debug==1 : print("Picture Width: ",Picture_Width, "Picture Height: ", Picture_Height)
    #Calculate how to ajust the picture size in the UI
    Picture_Reduction_Ratio = (Picture_Width/Import.Tab2DisplayWindow_width)
    print(("Picture_Reduction_Ratio brut : ",Picture_Reduction_Ratio) if Import.debug ==1 else "")
    print(("Picture_Reduction_Ratio int() : ",int(Picture_Reduction_Ratio)) if Import.debug ==1 else "")
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
    Picture_Size = Import.ImageTk.PhotoImage(Picture_Resized)

    # Add the image to the Canvas
    Updated_Picture = canvas.create_image(0, 0, anchor="nw", image=Picture_Size)
    Import.ScrollBarLenghCalculation(Import,canvas)

def ChooseFile():
    global canvas, txt,tab2SelectedImg,Button_Reset,Button_Select_File
    global File_Path,Final_File_Name # use for save function
    global Extension,Format # Use to send format and extension to save modified picture with same format as original picture
    result = Import.filedialog.askopenfilename(title="Sélectionner une image", filetypes= Import.filetypes)
    print(("Mon resulat : ", result)if Import.debug == 1 else "")
    # Vérifier si le fichier est au format .heic
    _, extension = Import.os.path.splitext(result)
        
    if(result==''):
        print(("pas d'image selectionnées") if Import.debug == 1 else "")
        tab2SelectedImg = 0 
        Button_Reset.config(state="disabled")
        Import.Error_Cancelation(Texte_From_Json,AppLanguages.Language)
    
    else : 
        Import.DisplayProcessing(Import.Tab3DisplayWindow_x_position,Import.Tab3DisplayWindow_y_position,Import.Tab3DisplayWindow_width,Import.Tab3DisplayWindow_Height,tab3) #Call process
        Import.UpdateProcessing(Texte_From_Json["MessageBox"]["Message"]["LoadingTime"][AppLanguages.Language])

        Button_Reset.config(state="normal")
        Button_Select_File.config(state="disabled")
        Button_Text_Modification.config(state="normal")
        Button_Validate.config(state="normal")
        
        tab2SelectedImg = 1 
        File_Path=result

    #-------Selection du nom sans extension .png ou .jpg
        File_Name_Splited = result.split('.')
        File_Name_Without_Format = File_Name_Splited[0]
    #-------Nom identique lors de la sauvegadre avec ajout de "- Transparent"
        Final_File_Name= File_Name_Without_Format + " -" + Texte_From_Json["File_Extension"]["Watermark"][AppLanguages.Language]
        if extension.lower() == '.heic':
            Extension,Format = ".heic" , "png"
        elif extension.lower() == '.jpg':
            Extension,Format = ".jpg" , "png"
        else:
            Extension,Format = ".png" , "png"
        Import.HideProcessing()
        DisplaySelectedPicture(result)
        canvas.delete(txt) #Suppression de l'écriture bleu en cas de chargement d'une image transparente
        Import.ScrollBarLenghCalculation(Import,canvas)
        Import.ShowScrollbars()

        DisplayText(canvas)
        



def AddWatermark(master,root):
    global Texte_From_Json
    global canvas, txt
    global Button_Reset,Button_Select_File,Button_Validate,Button_Text_Modification
    global tab3
    global Boutons_ControleTab3 # Used to active or disable button depend on UI actions
    tab3 = Import.ttk.Frame(master)
    InitValues()
    Texte_From_Json=Import.LoadText()
    Import.InitButtonsIcones() #Load button icones

    Button_Select_File = Import.tk.Button(tab3) ; Button_Validate = Import.tk.Button(tab3) 
    Button_Test = Import.tk.Button(tab3) ; Button_Reset=Import.tk.Button(tab3)
    Button_Exit = Import.tk.Button(tab3) ; Button_Text_Modification = Import.tk.Button(tab3)

    canvas = Import.tk.Canvas(tab3, highlightthickness=1, highlightbackground="black")
    Import.Watermark.Canvas = canvas
    canvas.place(x=Import.Tab2DisplayWindow_x_position, y=Import.Tab2DisplayWindow_y_position,width=Import.Tab2DisplayWindow_width, height=Import.Tab2DisplayWindow_Height)
    # canvas.bind("<Button-1>", click_on_canvas)
    txt = canvas.create_text(300, 200, text=Texte_From_Json["Tab2"]["Instruction"][AppLanguages.Language], font="Arial 16 italic", fill="blue")



    Import.ScrollBar(Import,canvas)
    Boutons_ControleTab3 = [
        [Button_Select_File, Texte_From_Json["Buttons"]["OpenFile"][AppLanguages.Language],Import.Icon_Add_File, ChooseFile,Import.tk.NORMAL ],
        [Button_Text_Modification, Texte_From_Json["Buttons"]["TextModification"][AppLanguages.Language],Import.Icon_Text_Modifications, EditWatermarkText,Import.tk.DISABLED],
        [Button_Validate, Texte_From_Json["Buttons"]["Validate"][AppLanguages.Language],Import.Icon_Validate, lambda: Save(Extension,Format),Import.tk.DISABLED],
        [Button_Reset, Texte_From_Json["Buttons"]["Reset"][AppLanguages.Language],Import.Icon_Reset, Reset,Import.tk.DISABLED],       
        [Button_Exit, Texte_From_Json["Buttons"]["Exit"][AppLanguages.Language],Import.Icon_Exit, root.destroy,Import.tk.NORMAL],        

        # [Button_Test, "Test",Import.Icon_Test, test, Import.tk.NORMAL],
    ]

    # Boucle placement des bouttons
    Position_x_recalculeeTab2,Position_y_recalculeeTab2 = Import.ControlsButtonsInitPositionCalculation(Boutons_ControleTab3,Import.Tab2Canvas,offset=30)
    Import.PlaceButtonsAutomaticaly(Boutons_ControleTab3,Position_y_recalculeeTab2,Import.Control_Button_Width,Import.Control_Button_Height,Import.Space_Between_Button,Import.Picture_Reducer_Value,Position_x_recalculeeTab2,Import.Police_Size,TextDisplay=1,Init_State=1)

    canvas.bind("<MouseWheel>", lambda event: Import.MousewheelMouvement(event, canvas))
    canvas.bind("<Button-2>", Import.HorizontalMouvement)

    return tab3
    