from tkinter import *

window = Tk()
window.title("my first gui")
window.minsize(width=800, height=500)
window.config(bg="black", padx=10, pady=10)

#label
lable = Label(text = "TITLE", font = ("bookman", 32), fg="gold", bg="black")
lable.grid(column=1, row=1)

def button_on_click():
    lable.config(text = entry.get() )

#button
button = Button(text = "click me", command= button_on_click, fg="gold", bg="black")
button.grid(column=2,row=2)

button1 = Button(text = "click me", command= button_on_click, fg="gold", bg="black")
button1.grid(column=3,row=1)
#entry
entry = Entry()
entry.insert(END,"text to input smtg")
entry.grid(column=4,row=4)
entry.config(fg="yellow",bg="black")


window.mainloop()