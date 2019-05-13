from datetime import datetime

def calculationBirthdayDistance(birthday):
    month = birthday.month
    day = birthday.day
    year = birthday.year
    now = datetime.now()
    year_now = now.year
    month_now = now.month
    day_now = now.day
    year = year_now if month > month_now or ( month == month_now and day >= day_now ) else year_now + 1
    distance = datetime(year, month, day) - datetime.now() 
    days = distance.days + 1
    return days