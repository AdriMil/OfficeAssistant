from SharedFunctions.imports import *
#-----------Chargment des onglets-----------------#
from Tabs.Tab_PdfCreator.PdfCreator import *
from Tabs.Tab_PictureObfuscation.PictureOffuscation import *

def MyUserInterface(root):
    frame = tk.Frame(root)
    version = '1.0.0.0'
    root.title("Office Assistant V " + version )

root = tk.Tk()             #Creation de la fenetre
root.resizable(width=False, height=False) #blocage de la taille de la fenetre

tabControl = ttk.Notebook(root)
tab1 = PdfCreatorTab(tabControl,root)
tab2 = PictureOffuscationTab(tabControl,root)
tabControl.add(tab1, text='Pdf Creator')
tabControl.add(tab2, text='Picture Offuscation')
tabControl.pack(expand=1, fill="both")
MyUserInterface(root)

window_height,window_width =  WindowsSizeSendData()

root.iconbitmap(resource_path("Pictures/OfficeAssistanticone.ico"))

root.geometry(str(window_width) + "x" + str(window_height))  # Taille de la fenetre
root.mainloop()
