from PIL import Image
from pillow_heif import register_heif_opener
import os

def convert_heic_to_pil(heic_path):
    # Enregistrement du module d'ouverture pour le format HEIC
    register_heif_opener()

    # Ouverture de l'image HEIC et conversion en mode RGB
    with Image.open(heic_path) as im:
        return im.convert("RGB")

def process_images(liste_chemin, FileName, chemin_final):
    Images_Multiple = []
    IMG_Mult = []

    for chemin in liste_chemin:
        # Vérifier si le fichier est au format .heic
        _, extension = os.path.splitext(chemin)
        if extension.lower() == '.heic':
            # Convertir .heic en image lisible avec PIL
            img_heic = convert_heic_to_pil(chemin)
            Images_Multiple.append(img_heic)
        else:
            # Pour les autres formats, ouvrir directement avec PIL
            Images_Multiple.append(Image.open(chemin))

    for img in Images_Multiple:
        # Convertir en mode RGB et ajouter à la liste IMG_Mult
        IMG_Mult.append(img.convert('RGB'))

    # Sauvegarder le fichier PDF
    nom = os.path.join(chemin_final, f"{FileName}.pdf")
    IMG_Mult[0].save(nom, save_all=True, append_images=IMG_Mult[1:])
