from imports import *
#-----------Chargment des onglets-----------------#
from Tab1PdfCreator import *
from Tab2PictureOffuscation import *

def gui(root):
    frame = tk.Frame(root)
    version = 'v10.50.105'
    root.title("Office Assistant V " + version )

root = tk.Tk()             #Creation de la fenetre
root.resizable(width=False, height=False) #blocage de la taille de la fenetre

tabControl = ttk.Notebook(root)
tab1 = Tab1PdfCreator(tabControl,root)
tab2 = Tab2PictureOffuscation(tabControl)
tabControl.add(tab1, text='Pdf Creator')
tabControl.add(tab2, text='Picture Offuscation')
tabControl.pack(expand=1, fill="both")
gui(root)

window_height,window_width =  WindowsSizeSendData()

root.iconbitmap(resource_path("Pictures/OfficeAssistanticone.ico"))

root.geometry(str(window_width) + "x" + str(window_height))  # Taille de la fenetre
root.mainloop()
