import tkinter
from tkinter import *

window = Tk()
window.title("TKInter2 GUI")
window.minsize(width=500, height=300)

#labels
label_1 = Label(text="default_1", font=("Arial", 24, "bold "))
label_1.grid(column=0, row=0)

label_2 = Label(text="default_2", font=("Arial", 24, "bold "))
label_2.grid(column=1, row=1)

label_3 = Label(text="default_3", font=("Arial", 24, "bold "))
label_3.grid(column=2, row=0)

label_4 = Label(text="default_4", font=("Arial", 24, "bold "))
label_4.grid(column=3, row=3)


mainloop()