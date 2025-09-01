import random

# names = ["Eren", "Mikasa", "Armin"]

# # list = {new_key:new_value for item in list}
# student_scores = {student: random.randint(50,100) for student in names}
# print(student_scores)
#
# # list = {new_key:new_value for (key,value) in dictionary.items()}
# passed_students  = {student :score for (student,score) in student_scores.items() if score > 90}
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# new_sentences = sentence.split()
#
# result = {words: len(words) for words in new_sentences}
# print(result)

import pandas

student_dict = {
    "anime" : ["aot", "bleach", "erased"],
    "ratings": [10, 9, 9]
}

student_data = pandas.DataFrame(student_dict)
# for (key, value) in student_data.items():
#     print(value)
for (index, data) in student_data.iterrows():
    if data.anime == "bleach":
        print(data.ratings)