from datetime import datetime
import random
import re
# def get_days_from_today(date):
#     current_time= datetime.today()
#     earn_date= datetime.strptime(date,"%Y-%m-%d")

#     return (current_time-earn_date).days

# print(get_days_from_today("2026-10-09"))


# def get_numbers_ticket(min, max, quantity):
#    if min < 1 or max > 1000 or quantity < min and quantity > max:
#       print("Enter min > 1 and max < 1000")
#       return
   
#    n =0
#    unique_numbers = set()

#    while n< quantity:
#       counters = random.randint(min,max)
#       n+=1
#       unique_numbers.add(counters)  

#    nums = list(unique_numbers)
#    nums.sort()
#    return nums 

# print(get_numbers_ticket(1,42,6))


def normalize_phone(phone_number):
    find_number= r'[^0-9+]'

    normalize_number = re.sub(find_number,'',phone_number)

    if normalize_number.startswith("380"):
        return "+38" + normalize_number[2:]
      
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
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)