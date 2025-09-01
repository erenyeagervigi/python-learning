import pandas
import random
import datetime as dt
import smtplib

data = pandas.read_csv("birthdays.csv")

name = data['name'][0]
year = data['year'][0]
month = data['month'][0]
day = data['day'][0]

letters = ["letter_templates/letter_1.txt","letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

let = random.choice(letters)

with open(let) as file:
    data = file.read()

    data_list = data.replace("[NAME]", name)

    smtg = dt.datetime.now()
    time = dt.datetime(year= year, month= month, day= day)

    my_email = "vignesh13006@gmail.com"
    password = "ucda taxb moxo afpo"

    if smtg.month == time.month and smtg.year == time.year and smtg.day == time.day:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email,password = password)
            connection.sendmail(from_addr= my_email, to_addrs = "for.signuporlogin@gmail.com", msg = f"Subject: WISHES!!!! \n\n {data_list}" )
