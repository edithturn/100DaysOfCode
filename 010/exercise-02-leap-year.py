"""
Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

https://www.youtube.com/watch?v=xX96xng7sAE

This is how you work out whether if a particular year is a leap year.

on every year that is evenly divisible by 4 **except** every year that is evenly divisible by 100 **unless** the year is also evenly divisible by 400

e.g. The year 2000:

2000 ÷ 4 = 500 (Leap)

2000 ÷ 100 = 20 (Not Leap)

2000 ÷ 400 = 5 (Leap!)

"""

def is_leap(year):
    
    _year = int(year)

    flag_leap = 0
    if _year % 4 == 0:
        flag_leap += 1
        if _year % 100 == 0:
            flag_leap = 0
            if _year % 400 == 0:
                flag_leap += 1
            else:
                flag_leap = 0
        else:
            flag_leap += 1
            if _year % 400 == 0:
                flag_leap += 1
            else:
                flag_leap = 0
        
    else:
        flag_leap = 0

    if flag_leap > 0:
        return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    _len = len(month_days) -1
    
    for i in range(0, _len):
        if i == month - 1:
            days = month_days[i]
            if is_leap(year) == True:
                days += 1
            break
    return days



year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
