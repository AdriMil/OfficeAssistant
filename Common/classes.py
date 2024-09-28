from Common.myImports import tk,ttk
# from app.myImports import root

class Tab:
    def __init__(self, notebook, name):
        self.notebook = notebook
        self.name = name
        self.frame = ttk.Frame(self.notebook)
        self.notebook.add(self.frame, text=self.name)

class Button:

    id = 0
    POILCE_SIZE = 8
    HEIGHT = 40
    WIDTH = 40
    SPACE_BETWEEN_BUTTON = 10

    def __init__(self,component,text,icone, width= None, height= None, avaibable= True):
        self.id = id ; Button.id += 1; 
        self.text = text
        self.icone = icone
        self.width = Button.WIDTH if not width else width
        self.height = Button.HEIGHT if not height else height
        self.space_between_button = Button.SPACE_BETWEEN_BUTTON
        self.function = None
        self.xposition = None
        self.yposition = None
        self.click_number = 0
        
    
        self.btn = tk.Button(component,font=("Helvetica", self.POILCE_SIZE), text=self.text)
        self.btn.config(image=self.icone, compound=tk.TOP,width=self.width, height=self.height)
        if not avaibable:
            self.btn.config(state=tk.DISABLED)

    def update_button_position(self,xposition,yposition):
        print("In update_button_position")
        self.btn.place(x=xposition,y=yposition)
        self.xposition = xposition
        self.yposition = yposition
    
    def associate_a_function(self,function):
        self.btn.configure(command=function)
        self.function = function
    
    def availability(self,state):
        if state == "lock":
            self.btn.config(state=tk.DISABLED)
        elif state == "unlock":
            self.btn.config(state=tk.NORMAL)
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
