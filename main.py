import datetime as dt
import pandas
from random import *

today = (dt.datetime.now().month, dt.datetime.now().day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for index, data_row in data.iterrows()}

if today in birthdays_dict:
    file_path = f"letter_templates/letter_{randint(1,3)}.txt"
    with open(file_path) as letter_template:
        contents = letter_template.read()
        contents.replace("[NAME]", birthdays_dict[today]["name"])
