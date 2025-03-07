questions = ( ("is eren ? "),
              ("who is luffy ? "),
              ("assiasins sydicate is based on ? "))
options = (("A. hero","B. villain","C. neither"),
           ("A. pirate","B. civilian","C. marine"),
           ("A. egypt ","B. london","C. india"))
answers = ("A","A","B")
given_answers = []
score = 0
question_num = 0

for question in questions:
    print("---------------")
    print(question)
    for option in options[question_num]:
        print(option)

    given_answer = input("enter the correct options: ").upper()
    given_answers.append(given_answers)
    if given_answer == answers[question_num]:
        score +=1
        print("correct")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer ")
    question_num += 1
