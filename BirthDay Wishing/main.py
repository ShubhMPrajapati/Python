import random
from datetime import datetime
import pandas as pd
import smtplib
import ssl
user = "user email"
password = "password generated by you email provider"

today = (datetime.now().day, datetime.now().month)

data = pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
def birthday_check():
    if today in birthdays_dict:
        name = birthdays_dict[today]["name"]
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
            letter = file.read()
            content = letter.replace("[NAME]", name)

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls(context=ssl.create_default_context())
                connection.login(user, password)
                connection.sendmail(user,
                                    birthdays_dict[today]["email"],
                                    msg=f"Subject:Happy Birthday\n\n{content}")
                print(f"Email sent successfully!\nand the message was {content}")

        except smtplib.SMTPServerDisconnected as e:
            print(f"Failed to connect to the server: {e}")
        except smtplib.SMTPAuthenticationError as e:
            print(f"Authentication error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

from tkinter import *
windows = Tk()
windows.config(width=800,height=600)
windows.title("BirthDay Reminder App")
button = Button(text="Click Me")
button.grid(row=2,column=2)
image = PhotoImage()
canvas = Canvas(height=400, width=300)
canvas.grid(row=0,column=2)
canvas.create_image()
button.config()








windows.mainloop()