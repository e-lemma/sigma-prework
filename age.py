
from datetime import datetime


def age_calculator(given_date_str):

    current_date = datetime.now().date()
    given_date = datetime.strptime(given_date_str, "%d-%m-%Y")

    age = current_date.year - given_date.year - \
        ((current_date.month, current_date.day)
         < (given_date.month, given_date.day))

    print(f"Age is: {age} years!")


age_calculator("26-06-2000")
