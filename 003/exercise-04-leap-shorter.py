"""
on every year that is evenly divisible by 4 **except** every year that is evenly divisible by 100 **unless** the year is also evenly divisible by 400
"""

# _year = input("Year to analize:")
# year = int(_year)
# if(year%4==0) and not(year%100==0) or (year%400==0):
#     leap=True
# else:
#     leap=False
# print(leap)


year = input("Year to analize:")
_year = int(year)
if (_year % 4 == 0) and not(_year % 100 == 0) or (_year % 400 == 0):
    print(True)
else:
    print(False)