import tkinter


window = tkinter.Tk()


window.title("1st title")
window.minsize(width=500, height=300)


#labels
my_label = tkinter.Label(text="default", font=("Arial", 24, "bold "))
my_label.pack()

label = "default"

def click_command():
    input_text = input.get()
    my_label.config(text=f"{input_text}")
    my_label.pack()

buttom = tkinter.Button(text="edson_buttom", command=click_command)
buttom.pack()

input = tkinter.Entry()
input.pack()


window.mainloop()


# def add(*args):
#     numbers = [args]
#     numbers = sum(list(numbers)[0])
#     return numbers
#
# print(add(1,2,3))


# def calculate(**kwargs):
#     pass
#
#
# calculate()