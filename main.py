from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk()
root.title("Make Elements")
root.geometry("600x600")
listv = ["Button" , "Label" , "Dropdown"]
creatorcombo = ttk.Combobox(root,state="readonly",values=listv)
creatorcombo.pack()
class CreateElements:
    def __init__(self):
        print("This is CreateElements class")
    def createLabel(self):
        label = Label(root,text="This Label Is Created Using Class",fg="blue")
        label.pack()
    def createButton(self):
        button = Button(root,text="The Button Made By Class('Click Me')",command=self.message)
        button.pack()
    def createDropdown(self):
        numlist = [1,2,3,4,5,6,7,8,9,0]
        combobox = ttk.Combobox(root,state="readonly",values=numlist)
        combobox.pack()
    def choose(self):
        selectedval = creatorcombo.get()
        if selectedval == "Label":
            self.createLabel()
        if selectedval == "Button":
            self.createButton()
        if selectedval == "Dropdown":
            self.createDropdown()
    def message(self):
        messagebox.showinfo("Message!","You clicked the button created using class")
btn = Button(root,text="Create Element",command=CreateElements().choose)
btn.pack()
root.mainloop()