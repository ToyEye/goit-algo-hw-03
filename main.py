from datetime import datetime
import random
def get_days_from_today(date):
    current_time= datetime.today()
    earn_date= datetime.strptime(date,"%Y-%m-%d")

    return (current_time-earn_date).days

print(get_days_from_today("2026-10-09"))


def get_numbers_ticket(min, max, quantity):
   if min < 1 or max > 1000:
      print("Enter min > 1 and max < 1000")
      return
   
   n =0
   unique_numbers = set()

   while n< quantity:
      counters = random.randint(min,max)
      n+=1
      unique_numbers.add(counters)  

   nums = list(unique_numbers)
   nums.sort()
   return nums 

print(get_numbers_ticket(1,42,6))