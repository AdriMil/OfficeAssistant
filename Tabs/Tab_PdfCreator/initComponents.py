from Common.classes import Button, Tab
from Common.init import tabControl
from Common.SharedFunctions.sharedFunctions import AppLanguages,Texte_From_Json
from Common.SharedFunctions.sharedComponents import Icon_Add_File, Icon_Reset, Icon_Convert_To_Pdf, Icon_Exit, Icon_Arrow_Down, Icon_Arrow_Up, Icon_Delete_Selected_Line

tab1 = Tab(tabControl,"texte")

myMainButtons = []

Button_Select_Files = Button(component=tab1.frame,text=Texte_From_Json["Buttons"]["AddFiles"][AppLanguages.Language],icone=Icon_Add_File)
Button_Reset = Button(component=tab1.frame,text=Texte_From_Json["Buttons"]["Reset"][AppLanguages.Language],icone=Icon_Reset,avaibable=False)
Button_Convert = Button(component=tab1.frame,text=Texte_From_Json["Buttons"]["Convert"][AppLanguages.Language],icone=Icon_Convert_To_Pdf,avaibable=False)
Button_Exit = Button(component=tab1.frame,text=Texte_From_Json["Buttons"]["Exit"][AppLanguages.Language],icone=Icon_Exit)

myMainButtons=[Button_Select_Files,Button_Reset,Button_Convert,Button_Exit]


control_arrows = []
width = 35
height = 35
Button_Arrow_Up = Button(component=tab1.frame,text="MoveUp",icone=Icon_Arrow_Up,width=width,height=height)
Button_Delete_Selected_Line = Button(component=tab1.frame,text="Delete",icone=Icon_Delete_Selected_Line,width=width,height=height)
Button_Arrow_Down = Button(component=tab1.frame,text="MoveDown",icone=Icon_Arrow_Down,width=width,height=height)
control_arrows = [Button_Arrow_Up,Button_Delete_Selected_Line,Button_Arrow_Down]