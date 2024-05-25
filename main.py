
#-----------Chargment des onglets-----------------#
import Tabs.Tab_PdfCreator.PdfCreator as PdfCreatorFunctions
import Tabs.Tab_PictureObfuscation.PictureOffuscation as PictureOffuscationFunctions
import SharedFunctions.imports as Import
from Tabs.Tab_PictureObfuscation.PictureOffuscation import Tab2UpdateLangages
from SharedFunctions.imports import AppLanguages
import Tabs.Tab_Filigram.TabFiligram as AddFiligram

#Init Soft version, will be overwrite by Pipelines process
def MyUserInterface(root):
    version = '1.0.0'
    root.title("Office Assistant V " + version )
#Tab init Function, used at the begining and when language is changed
def InitTabs(root):
    global tabControl,tab1,tab2,tab3
    tabControl = Import.ttk.Notebook(root)
    tab1 = PdfCreatorFunctions.PdfCreatorTab(tabControl,root)
    tab2 = PictureOffuscationFunctions.PictureOffuscationTab(tabControl,root)
    tab3 = AddFiligram.AddFiligram(tabControl,root)
    tabControl.add(tab1, text=Texte_From_Json["Tab1"]["TabName"][AppLanguages.Language])
    tabControl.add(tab2, text=Texte_From_Json["Tab2"]["TabName"][AppLanguages.Language])
    tabControl.add(tab3, text=Texte_From_Json["Tab2"]["TabName"][AppLanguages.Language])
    tabControl.pack(expand=1, fill="both")

def LanguageChanged(Current_Language):
    global tab1,tab2,tab3,tabControl, language_menu
    global Old_Language,Old_Number_Language
    AppLanguages.Language,_ = Import.ConvertLanguage(Current_Language)
    #Ask question if you are sure to change language
    User_answer = Import.Info_Change_Language(Texte_From_Json,AppLanguages.Language)

    if User_answer == "yes":
        tabControl.destroy(); tab1.destroy(); tab2.destroy(); tab3.destroy(); language_menu.destroy() #Destroy all table
        InitTabs(root)  #REstore All tables 
        InitLanguageMenu() #Restore Menu languages
        Old_Language,Old_Number_Language = Import.ConvertLanguage(AppLanguages.Language) #Current Language is store as Old, then save for next language update.
    else:
        #If no, need to remember an display n-1 selected language.
        AppLanguages.Language = Old_Language
        selected_language.set(AppLanguages.languages[Old_Number_Language])

# Création du menu déroulant pour les langues
def InitLanguageMenu():
    global language_menu
    language_menu = Import.tk.OptionMenu(root, selected_language, *AppLanguages.languages, command=LanguageChanged )
    language_menu.config(width=Import.Language_Button_Width, height=Import.Language_Button_Height)
    language_menu.pack()

#Import string from json file.
Texte_From_Json=Import.LoadText()

# WindowCreation
root = Import.tk.Tk()
root.resizable(width=False, height=False) #blocage de la taille de la fenetre
MyUserInterface(root)
InitTabs(root)
Window_Height,Window_Width =  PdfCreatorFunctions.WindowsSizeSendData()
root.iconbitmap(Import.Ressource_Path("Pictures/OfficeAssistanticone.ico"))

#Menu to display language selection
selected_language = Import.tk.StringVar(root)
selected_language.set(AppLanguages.languages[0])
#need to remember an display n-1 selected languag. By default fr when starting
Old_Language,Old_Number_Language = Import.ConvertLanguage(selected_language.get())

InitLanguageMenu()

root.geometry(str(Window_Width) + "x" + str(Window_Height))  # Taille de la fenetre
root.mainloop()
