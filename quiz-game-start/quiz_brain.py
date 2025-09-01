#ask the user a question
#check if the answer to the question is right
class QuizBrian():
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
         current_question = self.question_list[self.question_number]
         self.question_number +=1
         user_input =input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
         self.check_answer(user_input, current_question.answer)

    def still_has_questions(self):
        if len(self.question_list) == self.question_number:
            print("you've completed the quiz")
            print(f"you're Final score is : {self.score}/{self.question_number}")
            return False
        else:
            print("you've completed the quiz")
            print(f"you're Final score is : {self.score}/{self.question_number}")
            return True

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("you're right")
        else:
            print("you're wrong")
        print(f"you're current score is: {self.score}/{self.question_number}")
        print(f"the correct answer was {correct_answer}\n")