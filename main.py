import datetime as dt
import pandas
from random import *
import smtplib

today = (dt.datetime.now().month, dt.datetime.now().day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day)
                   : data_row for index, data_row in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{randint(1,3)}.txt"
    with open(file_path) as letter_template:
        contents = letter_template.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

        my_email = "testie.testermann@gmail.com"
        my_password = "****************"  # not actual password

        # Connection to email provider SMTP
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:

            # Connection encryption:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday!\n\n{contents}")
