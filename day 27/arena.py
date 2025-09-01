from tkinter import *

window = Tk()
window.title("my first gui")
window.minsize(width=800, height=700)

#label
lable = Label(text = "bang me daddy 🥵🥵🥵🥵", font = ("bookman", 32))
lable.pack()

def button_on_click():
    lable.config(text = "ahhhh 🥵🥵🥵🥵🥵")
    print(entry.get())
#button
button = Button(text = "bang me", command= button_on_click)
button.pack()

#entry
entry = Entry()
entry.insert(END,"text to bang her harder")
entry.pack()

#text
text = Text(width= 40, height=10)
text.focus()
text.insert(END, "example of multiline inputs")
text.get(text.get("1.0"), END)
text.pack()

#spinbox
def spinbox_inoput():
    print(spinbox.get())
spinbox = Spinbox(from_= 10, to=20, width=10, command= spinbox_inoput)
spinbox.pack()

#scale
scale = Scale()
scale.pack()

#checkbox
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#radio button

check = IntVar()
radiobutton1 = Radiobutton(text="smtg1", variable= check, value=1)
radiobutton2 = Radiobutton(text="smtg2", variable= check, value=2)
radiobutton1.pack()
radiobutton2.pack()

#listbox
def listed(event):
    print(list_box.get(list_box.curselection()))
list_box = Listbox(height=4)
anime = ["aot", "bleach", "erased", "haikyuu"]
for i in anime:
    list_box.insert(anime.index(i), i)
list_box.bind("<<ListboxSelect>>",listed)
list_box.pack()

window.mainloop()