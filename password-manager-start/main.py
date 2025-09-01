from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))] + [choice(symbols) for _ in range(randint(2, 4))] + [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, f"{password}")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    new_data = {
        website:{
            "email" : email,
            "password": password
        }
    }

    if len(website) > 1 and len(password) > 1:
        is_ok = messagebox.askokcancel(title="confirm", message=f"website: {website}\n email: {email}\n password: {password}\n is it ok to save?")

        while is_ok:
            try:
                with open("data.json", "r") as file_data:
                    #reading the exsisting json file
                    data = json.load(file_data)
                    #updating the exsisting json file
                    data.update(new_data)

            except JSONDecodeError:
                with open("data.json", "w") as file:
                    json.dump(new_data,file,indent=4)
            else:

                with open("data.json", "w") as file:
                    #writing the updated json file
                        json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0, END)
                website_entry.focus()
                break
    else:
        messagebox.showerror(title="INVALID", message="please enter the fields")
# ---------------------------- SEARCH ------------------------------- #

def search():
    try:
        with open("data.json", "r") as data:
            value = json.load(data)
            if website_entry.get() in value:
                user_needs = value[website_entry.get()]
                messagebox.showinfo(title=website_entry.get(), message=f"email: {user_needs['email']}\n password: {user_needs['password']}")
            elif len(website_entry.get()) < 1:
                messagebox.showerror(title="error", message="please dont leave the field empty")
            else:
                messagebox.showerror(title="error", message="the website you have search for does not exsit")

    except JSONDecodeError:
        messagebox.showerror(title="error", message="the website you have search for does not exsit")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=60)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
Label(text="Website:").grid(row=1, column=0)
Label(text="Email/Username:").grid(row=2, column=0)
Label(text="Password:").grid(row=3, column=0)

# Entries
# website_entry = Entry(width=40)
# website_entry.focus()
# website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=40)
email_entry.insert(END, "vignesh13006@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

# Frame for website entry + button
website_frame = Frame(window)
website_frame.grid(row = 1, column = 1, columnspan=2, sticky= "w")

website_entry = Entry(website_frame, width= 25)
website_entry.pack(side = LEFT)
website_entry.focus()

search_button = Button(website_frame,text="Search",width=11, command=search)
search_button.pack(side = LEFT)

# Frame for password entry + button
password_frame = Frame(window)
password_frame.grid(row=3, column=1, columnspan=2, sticky="w")

password_entry = Entry(password_frame, width=21)
password_entry.pack(side=LEFT)

generate_password_button = Button(password_frame, text="Generate Password", command=generate)
generate_password_button.pack(side=LEFT)

# Add Button
add_button = Button(text="Add", width=33,command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
