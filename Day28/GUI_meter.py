from tkinter import *

window = Tk()
window.title("Meter Calculator")
window.minsize(height=400, width=400)

entry = Entry(width=30)
entry.grid(column=1, row=0)
value = 0

def action():
    value = entry.get()
    result = float(value) * 1.60934
    l3.config(text=result, font=("Arial", 20))

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.grid(column=1, row=2)



l1 = Label(text="Miles", font=("Arial", 20))
l1.grid(column=2, row=0)
l2 = Label(text="is equal to:", font=("Arial", 20))
l2.grid(column=0, row=1)
l3 = Label(text=0, font=("Arial", 20))
l3.grid(column=1, row=1)
l4 = Label(text="Km", font=("Arial", 20))
l4.grid(column=2, row=1)


mainloop()