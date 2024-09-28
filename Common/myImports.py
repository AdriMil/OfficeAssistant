#-------------Pour_IG--------------------#
from tkinter import PhotoImage, NO, ttk,simpledialog,filedialog
import tkinter as tk
from PIL import Image
from pillow_heif import register_heif_opener
from Tabs.Tab_PdfCreator.UpdatePosition import ChangePlaceUp,ChangePlaceDown,DeleteSelectedLine
#MessageBox import
from Common.SharedFunctions.MessageBox import Error_NoTitle,Error_BadSavePath,Error_NoPicture,Error_Cancelation,Info_ProcessFinished,Info_Reset,Info_Reset_Tab2,Info_FileSaved, Info_Change_Language,Error_EmptyField
from PIL import Image
from PIL import ImageTk  
import datetime
#-------------PYINSTALLER--------------------#
import os
import sys
#Create a .exe file : pyinstaller main.spec

import json