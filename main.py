import random
import smtplib
import datetime as dt

MY_EMAIL = "nikolalatesting@gmail.com"
MY_PASSWORD = "qwer/.,m1234"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt", encoding="utf-8") as data_quotes:
        all_quotes = data_quotes.readlines()
        quote = random.choice(all_quotes)
    en_quote = quote.encode('ascii', 'ignore')
    print(en_quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="lyvireakdara@gmail.com",
                         msg=f"Subject:Monday Motivation\n\n{en_quote}")
else:
    print("You got mail")




# import smtplib
#
# my_email = "nikolalatesting@gmail.com"
# password = "qwer/.,m1234"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="vichekakhat001@gmail.com",
#                         msg="Subject:Python\n\n Testing")

# import datetime as dt
#
# now = dt.datetime.now()
# print(now.weekday())
