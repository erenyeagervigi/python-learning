from tkinter import *

FONT = ("Comic Sans MS",16)

window = Tk()
window.minsize(width=400, height=100)
window.title("kg to pounds converter")
window.config(bg="black", pady=10, padx=10)
#input table
lable = Label(text="kilogram",font= FONT, fg="gold", bg="black")
lable.grid(column=2, row= 0)

entry = Entry()
entry.insert(END,"0")
entry.grid(column=1, row=0)
entry.config(fg="gold", bg="black")
#output table

lable1 = Label(text="is equal to",font=FONT, fg="gold", bg="black")
lable1.grid(column=0, row= 1)

lable2 = Label(text="pounds",font=FONT, fg="gold", bg="black")
lable2.grid(column=2, row= 1)

lable3 = Label(text= "0", font=FONT, fg="gold", bg="black")
lable3.grid(column=1, row= 1)

#converter
def converter():
    pounds = float(entry.get()) * 2.20462
    lable3.config(text = round(pounds,1))

button = Button(text="covert", command=converter, fg="gold", bg="black")
button.grid(column=1, row= 3)

window.mainloop()