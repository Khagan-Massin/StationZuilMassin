from tkinter import *
from main import comment

def click():
        mylabel = Label(text="Jij hebt gewonnen🤪🥳")
        mylabel.pack()

def dombo_click():
        dombo_label = Label(text="Jij bent dom")
        dombo_label.pack()
root = Tk()


veld = Button(root, text="Button", command = click)

dombo_knop = Button(root, text="Click als je dom bent", command = dombo_click)

veld.pack()
dombo_knop.pack()

root.mainloop()