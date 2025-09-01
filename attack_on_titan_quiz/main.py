from data import question_data
from question_model import Question
from quiz_brain import Quizbrain

question_bank = []
for questions in question_data:
     q_question = questions['text']
     q_answer = questions['answer']
     q_list = Question(q_question, q_answer)
     question_bank.append(q_list)

quiz = Quizbrain(question_bank)
while quiz.is_continue():
     quiz.ask_questions()