from datetime import datetime

def get_days_from_today(date):
    current_time= datetime.today()
    earn_date= datetime.strptime(date,"%Y-%m-%d")

    return (current_time-earn_date).days

print(get_days_from_today("2026-10-09"))
