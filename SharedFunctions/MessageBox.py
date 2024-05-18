from tkinter import messagebox


def Error_NoTitle(Texte_From_Json,Language):
    messagebox.showinfo(Texte_From_Json["MessageBox"]["Type"]["Error"][Language], Texte_From_Json["MessageBox"]["Message"]["NoTitle"][Language])
def Error_BadSavePath(Texte_From_Json,Language):
    messagebox.showinfo(Texte_From_Json["MessageBox"]["Type"]["Error"][Language], Texte_From_Json["MessageBox"]["Message"]["BadSavePath"][Language])
def Error_NoPicture(Texte_From_Json,Language):
    messagebox.showinfo(Texte_From_Json["MessageBox"]["Type"]["Error"][Language], Texte_From_Json["MessageBox"]["Message"]["NoPicture"][Language])
def Error_Cancelation(Texte_From_Json,Language):
    messagebox.showinfo(Texte_From_Json["MessageBox"]["Type"]["Error"][Language], Texte_From_Json["MessageBox"]["Message"]["Error_Cancelation"][Language])
def Info_ProcessFinished(liste_chemin,FileName,chemin_final,Texte_From_Json,Language):
    message = "Fichier pdf créé avec succès\n\nDétails:\n- Nombre d'images : "+ str(len(liste_chemin)) +"\n- Nom du fichier : "+FileName+"\n- Chemin : "+chemin_final
    message = Texte_From_Json["MessageBox"]["Message"]["Info_ProcessFinished"]["part1"][Language]+ str(len(liste_chemin)) +Texte_From_Json["MessageBox"]["Message"]["Info_ProcessFinished"]["part2"][Language]+FileName+Texte_From_Json["MessageBox"]["Message"]["Info_ProcessFinished"]["part3"][Language]+chemin_final
    messagebox.showinfo(Texte_From_Json["MessageBox"]["Type"]["Info"][Language], message)
def Info_Reset(Texte_From_Json,Language):
    reponse = messagebox.askquestion(Texte_From_Json["MessageBox"]["Type"]["Confirmation"][Language], Texte_From_Json["MessageBox"]["Message"]["Info_Reset"][Language])
    return reponse
def Info_Reset_Tab2(Texte_From_Json,Language):
    reponse = messagebox.askquestion(Texte_From_Json["MessageBox"]["Type"]["Confirmation"][Language], Texte_From_Json["MessageBox"]["Message"]["Info_Reset_Tab2"][Language])
    return reponse
def Info_FileSaved(Texte_From_Json,Language):
    messagebox.showinfo(Texte_From_Json["MessageBox"]["Type"]["Info"][Language], Texte_From_Json["MessageBox"]["Message"]["Info_FileSaved"][Language])
