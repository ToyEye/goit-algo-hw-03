
import datetime as dt
from datetime import datetime as dtdt
import random
import re


# Task 1

def get_days_from_today(date):
    try:
        current_time= dtdt.today()
        earn_date= dtdt.strptime(date,"%Y-%m-%d")

        return (current_time-earn_date).days
    except ValueError:
        return "Invalid date format. Please provide the date in the format 'YYYY-MM-DD'."

print(get_days_from_today("2026-10-09"))


#Task 2

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or min > max or quantity <= min or quantity >= max:
      print("Enter min > 1 and max < 1000")
      return []
   

    n =0
    unique_numbers = set()

    while n< quantity:
      counters = random.randint(min,max)

      if counters not in unique_numbers:  
        n+=1
        unique_numbers.add(counters)  

    nums = list(unique_numbers)
    nums.sort()
    return nums 

print(get_numbers_ticket(4, 14, 5))

# Task 3

def normalize_phone(phone_number):
    find_number= r'[^0-9+]'

    normalize_number = re.sub(find_number,'',phone_number)

    if normalize_number.startswith("380"):
        return "+38" + normalize_number[2:]
    
    elif len(normalize_number)==12:
        return "+" + normalize_number
      
    elif not normalize_number.startswith("+"):
        return "+38" + normalize_number
    
    
    return normalize_number
 

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "432 11 222 22 22"
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


# Task 4

def get_upcoming_birthdays(users=None):
    tdate=dtdt.today().date() # беремо сьогоднішню дату
    birthdays=[] 

    for user in users: # перебираємо користувачів
        bdate=user["birthday"] 
        bdate=str(tdate.year)+bdate[4:] # Замінюємо рік на поточний
       
        bdate=dtdt.strptime(bdate, "%Y.%m.%d").date() # перетворюємо дату народження в об’єкт date
        week_day=bdate.isoweekday() # Отримуємо день тижня (1-7)
        days_between=(bdate-tdate).days 

        if 0<=days_between<7:

            if(week_day<6):
                birthdays.append({'name':user["name"],"congratulation_date":bdate.strftime("%Y.%m.%d")}) # Додаємо вітання у список, якщо списко випадає на робочі дні

            else:
                if(bdate+dt.timedelta(days=1)).weekday()==0:
                    birthdays.append({"name":user['name'],"congratulation_date":(bdate+dt.timedelta(days=1)).strftime("%Y.%m.%d")}) # Додаємо вітання у список, якщо списко випадає на неділю 

                elif(bdate+dt.timedelta(days=2)).weekday()==0:
                    birthdays.append({"name":user["name"],"congratulation_date":(bdate+dt.timedelta(days=2)).strftime("%Y.%m.%d")}) # Додаємо вітання у список, якщо списко випадає на суботу        
       

    return birthdays


# users = [
#     {"name": "John Doe", "birthday": "2027.01.23"},
#     {"name": "Jane Smith", "birthday": "2024.03.27"},
#     {"name": "Alex", "birthday": "2024.02.17"},
# ]

users = [
    {"name": "Mohel Smith", "birthday": "1995.02.16"},
    {"name": "John Dark", "birthday": "1985.02.17"},
    {"name": "Mary Dark", "birthday": "1985.02.18"},
    {"name": "Derek Dark", "birthday": "1985.02.19"},
    {"name": "Jane Smith", "birthday": "1990.02.20"}
    ]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
