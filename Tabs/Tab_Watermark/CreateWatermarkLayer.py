import SharedFunctions.imports as Import
from PIL import Image, ImageTk, ImageDraw, ImageFont

#This funcction create a transparency picture with text. This picture will be put above the loaded picture. 
def create_text_image(Filigram_Text, Font_Path,font_size,Space_Between_Lines, Color, Transparency, Filigram_y_Start, Picture_Width, Picture_Height,Coordonate_Liste,Step):
    image = Image.new("RGBA", (Picture_Width, Picture_Height), (255, 255, 255, 0)) #Create transparency picture to put above loaded picture
    draw = ImageDraw.Draw(image)
    
    # Load font  and #Color + transparency
    font = ImageFont.truetype(Font_Path, font_size)
    text_color = (*Color, Transparency)

    # When visualisation step, save filigram texts coordonates for displayed picture (which is reduced in canvas)
    if Step == "visualisation":
        
        for i in range(0, Picture_Height, Space_Between_Lines):
            x = 0
            y = Filigram_y_Start + i
            draw.text((x, y), Filigram_Text, font=font, fill=text_color)
            Coordonate_Liste.append([x, y])
        if Import.debug == 1: print("Visualisation sptep texte coordonates : ", Coordonate_Liste)

    # When saving step, apply filigram coordonates for real picture (which is greater than the one displayed in canvas)
    elif Step == "saving":
        for coordonates in Coordonate_Liste:
            x,y = coordonates
            draw.text((x, y), Filigram_Text, font=font, fill=text_color)
    return image
Superposed_Picture = None
def DisplayText(canvas):
    
    global text_image  # Déclarez text_image comme variable globale pour pouvoir l'utiliser dans save_image
    global Superposed_Picture
    # Création de l'image du texte avec transparence
    text_image = create_text_image(Import.Watermark.Text,Import.Font_Path, Import.Watermark.Font_Size, Import.Watermark.Space_Between_Text,Import.Watermark.Color, Import.Watermark.Transparency, 0, Import.Watermark.Width, Import.Watermark.Height,Import.Watermark.Lines_Coordonate,Step="visualisation")
    text_image_tk = ImageTk.PhotoImage(text_image)
    # Affichage de l'image du texte sur le canvas
    if Superposed_Picture is not None: canvas.delete(Superposed_Picture)

    Superposed_Picture  = canvas.create_image(0, 0, anchor="nw", image=text_image_tk)
    # Stocker l'image pour éviter qu'elle soit garbage collected
    canvas.text_image_tk = text_image_tk
