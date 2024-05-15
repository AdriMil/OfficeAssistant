
#-----------Chargment des onglets-----------------#
import Tabs.Tab_PdfCreator.PdfCreator as PdfCreatorFunctions
import Tabs.Tab_PictureObfuscation.PictureOffuscation as PictureOffuscationFunctions
import SharedFunctions.imports as Import

def MyUserInterface(root):
    version = '1.0.0'
    root.title("Office Assistant V " + version )

root = Import.tk.Tk()             #Creation de la fenetre
root.resizable(width=False, height=False) #blocage de la taille de la fenetre

tabControl = Import.ttk.Notebook(root)
tab1 = PdfCreatorFunctions.PdfCreatorTab(tabControl,root)
tab2 = PictureOffuscationFunctions.PictureOffuscationTab(tabControl,root)
tabControl.add(tab1, text='Pdf Creator')
tabControl.add(tab2, text='Picture Offuscation')
tabControl.pack(expand=1, fill="both")
MyUserInterface(root)

Window_Height,Window_Width =  PdfCreatorFunctions.WindowsSizeSendData()

root.iconbitmap(Import.Ressource_Path("Pictures/OfficeAssistanticone.ico"))

root.geometry(str(Window_Width) + "x" + str(Window_Height))  # Taille de la fenetre
root.mainloop()
