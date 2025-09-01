from tkinter import *
import math
from tkinter import messagebox
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
marks = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    global marks
    marks = ""
    global reps
    reps = 1
    check_mark.config(text=marks)
    label.config(text="TIMER", font=(FONT_NAME,35,"bold"),fg="#D84040", bg="#F8F2DE")
    canva.itemconfig(timer_text, text = f"00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    if reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        label.config(text="BREAK TIME", fg="#6DE1D2")
        messagebox.showinfo(title="BREAK TIME!!", message="you can take a break now")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN* 60)
        label.config(text="BREAK TIME", fg="#FFA955")
        messagebox.showinfo(title="BREAK TIME!!", message="you can take a break now")

    elif not reps % 2 == 0:
        count_down(WORK_MIN* 60)
        label.config(text="WORK TIME", fg="#FFD63A")
        if reps == 1:
            pass
        else:
            messagebox.showinfo(title="work time", message= "you gotta get to work")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(n):

    count_min = math.floor(n/60)
    count_sec = n % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canva.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if n > 0:
        global timer
        timer =  window.after(1000,count_down,n-1)
    else:
        global reps
        if reps == 8:
            reps = 0
        reps += 1
        start_timer()
        global marks
        if reps % 2 == 0:
            marks += "✔"
            check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(pady=100, padx=100, bg="#F8F2DE")


#tomato
canva = Canvas(width=203, height=226, bg="#F8F2DE", highlightthickness=0)
img = PhotoImage(file= "tomato.png")
canva.create_image(102,112, image = img)
timer_text = canva.create_text(103, 130, text="00:00", font= (FONT_NAME,22,"bold"), fill="#ECDCBF",)
canva.grid(column=1, row=1)

#timer label
label = Label(text="TIMER", font=(FONT_NAME,35,"bold"),fg="#D84040", bg="#F8F2DE")
label.grid(column=1, row=0)

#star and reset button
start = Button(text="start",fg="#A31D1D", bg="#F8F2DE", command= start_timer)
start.grid(column = 0, row = 3)
reset = Button(text="reset", fg = "#A31D1D", bg="#F8F2DE", command= reset)
reset.grid(column = 2, row = 3)

#lable
check_mark = Label(fg=GREEN, bg="#F8F2DE", font=(FONT_NAME, 12, "bold"))
check_mark.grid(column=1, row=4)


window.mainloop()