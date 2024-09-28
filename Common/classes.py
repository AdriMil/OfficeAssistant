import tkinter as tk
from app.myImports import root

class Chrono:
    def __init__(self):
        self.value = 82800
        self.state = "Pause"
        self.negative_count = 82801
        self.running = False

GlobalSeanceChrono = Chrono()
MainChrono = Chrono()

class Button:
    id = 0
    police_size = 8

    def __init__(self,component,text,icone,width,height):
        self.id = id ; Button.id += 1; 
        self.text = text
        self.icone = icone
        self.width = width
        self.height = height
        self.function = None
        self.xposition = None
        self.yposition = None
        self.click_number = 0
    
        self.button = tk.Button(component,font=("Helvetica", self.police_size), text=self.text)
        self.button.config(image=self.icone, compound=tk.TOP,width=self.width, height=self.height)

    def update_button_position(self,xposition,yposition):
        print("In update_button_position")
        self.button.place(x=xposition,y=yposition)
        self.xposition = xposition
        self.yposition = yposition
    
    def associate_a_function(self,function):
        self.button.configure(command=function)
        self.function = function
    
    def availability(self,state):
        if state == "lock":
            self.button.config(state=tk.DISABLED)
        elif state == "unlock":
            self.button.config(state=tk.NORMAL)
        else :
            print("Bad arguments, try 'lock' or 'unlock'")
    
    def action_click(self):
        self.click_number = self.click_number + 1
        print(self.click_number)

    @classmethod
    def count_instances(cls):
        return (cls.id)


class Listbox:
    def __init__(self,component,content: list):
        self.object = tk.Listbox(component, selectmode=tk.SINGLE)
        self.xposition = None
        self.yposition = None
        self.display_status = "Close"

        for item in content:
            self.object.insert(tk.END, item)

        self.object.select_set(0)
    
    def place_listbox(self, x_position_button, y_position_button, width, height):
        self.object.place(x=x_position_button, y=y_position_button, width=width, height= height)
        self.display_status = "Open"

    def hide_listbox(self):
        self.object.place_forget()
        self.display_status = "Close"
