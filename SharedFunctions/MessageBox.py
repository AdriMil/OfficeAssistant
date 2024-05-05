from tkinter import messagebox

def Error_BadSavePath():
    messagebox.showinfo("Erreur", "Chemin de sauvegarde manquant")
def Error_NoPicture():
    messagebox.showinfo("Erreur", "Pas d'image selectionnée")
def Error_Cancelation():
    messagebox.showinfo("Erreur", "Vous avez annulé")
def Info_ProcessFinished(liste_chemin,FileName,chemin_final):
    message = "Fichier pdf créé avec succès\n\nDétails:\n- Nombre d'images : "+ str(len(liste_chemin)) +"\n- Nom du fichier : "+FileName+"\n- Chemin : "+chemin_final
    messagebox.showinfo("Pdf créé ! ", message)
def INfo_Reset():
    reponse = messagebox.askquestion("Confirmation", "Voulez-vous faire un reset des images selectionnées ?")
    return reponse
