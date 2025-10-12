import smtplib
import datetime as dt
import random
my_email = "[email]"
password = "[password]"

time = dt.datetime.now()
week = time.weekday()
if week == 2:

    with open("quotes.txt",'r') as file:
        data = file.readlines()

    rando_word = random.choice(data)

    with smtplib.SMTP("smtp.gmail.com") as email:
        email.starttls()
        email.login(user = my_email, password = password)
        email.sendmail(from_addr= my_email, to_addrs="for.erenyeagervigi@yahoo.com", msg=f"Subject: quotes\n\n{rando_word}")

