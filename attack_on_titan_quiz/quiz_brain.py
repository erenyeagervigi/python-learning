class Quizbrain():
    def __init__(self, question_list):
        self.q_list = question_list
        self.question_number = 0
        self.score = 0

    def ask_questions(self):
        current_question = self.q_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}: {current_question.question} (True / False): ").lower()
        if user_input == "t":
            user_input = "true"
        elif user_input == "f":
            user_input = "false"
        if user_input.lower() == current_question.answer.lower():
            self.score += 1
            print("you're right! 😎 ")
        else:
            print("you're wrong! :C")
        print(f"you're score is: {self.score}/{self.question_number}")
        print(f"The correct answer is {current_question.answer}")

    def is_continue(self):
        if len(self.q_list) == self.question_number:
            print("you've completed the quiz!!!")
            print(f"you're total score is: {self.score}/{self.question_number}")
            return False
        else:
            return True
