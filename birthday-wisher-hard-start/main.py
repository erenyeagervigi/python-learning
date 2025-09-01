##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import pandas
import random
import datetime as dt
import smtplib

data = pandas.read_csv("birthdays.csv")

smtg = dt.datetime.now()
day = smtg.day
month = smtg.month

for index,i in data.iterrows():
    if i['day'] == day and i['month'] == month:
        name = i['name']
        # to_email = i['email']
        #
        # print(to_email)

        letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
        chosen_one = random.choice(letters)
        with open(chosen_one) as file:
            file1 = file.read()
            data_list = file1.replace("[NAME]", name)

        my_email = "vignesh13006@gmail.com"
        password = "ucda taxb moxo afpo"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password = password)
            connection.sendmail(from_addr= my_email, to_addrs = "for.signuporlogin@gmail.com", msg = f"Subject: WISHES!!!! \n\n {data_list}" )

