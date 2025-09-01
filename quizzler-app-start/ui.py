from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class Quizzler():
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg= THEME_COLOR, padx=20,pady=20)
        self.window.wm_minsize(width=350,height=500)

        self.lable = Label(text=f"score: {self.quiz.score}",bg=THEME_COLOR, fg="white", font=("Arial", 12))
        self.lable.grid(column=1, row=0, pady = 30)

        self.canva = Canvas(width=300, height=250, highlightthickness= 0, bd= 0)
        self.canva.grid(column=0, row=1,columnspan=2)
        self.question_text = self.canva.create_text(150,
                                                    125,
                                                    text="text",
                                                    width = 290,
                                                    font=("Arial", 20, "italic"))

        self.canva_correct_image =  PhotoImage(file="images/true.png")
        self.canva_wrong_image = PhotoImage(file="images/false.png")

        self.correct_button = Button(image = self.canva_correct_image, highlightthickness=0, bd = 0,command=self.right_button)
        self.correct_button.grid(column=0,row=2, pady = 30)

        self.wrong_button = Button(image = self.canva_wrong_image, highlightthickness=0, bd = 0,command=self.wrong_button)
        self.wrong_button.grid(column=1,row=2,pady = 30)

        self.next_question_ui()

        self.window.mainloop()

    def next_question_ui(self):
        self.canva.config(bg="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canva.itemconfig(self.question_text, text= f"{question}")
            self.lable.config(text = f"score: {self.quiz.score}")
        else:
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            self.canva.itemconfig(self.question_text, text="You've reached the end of quiz")

    def right_button(self):
        self.check_answer_ui(self.quiz.check_answer("True"))

    def wrong_button(self):
        self.check_answer_ui(self.quiz.check_answer("True"))

    def check_answer_ui(self, is_right = True):
        if is_right:
            self.canva.config(bg="green" )
            self.window.after(1000,self.next_question_ui)

        else:
            self.canva.config(bg="red")
            self.window.after(1000, self.next_question_ui)
