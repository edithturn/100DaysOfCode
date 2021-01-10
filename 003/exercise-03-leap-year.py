year = input("Which year do you want to check?")

_year = int(year)

flag_leap = 0
if _year % 4 == 0:
    flag_leap += 1
    if _year % 100 > 0:
        flag_leap += 1
        if _year % 400 == 0:
            flag_leap += 1
        else:
            flag_leap = 0
    else:
        flag_leap = 0
        if _year % 400 == 0:
            flag_leap += 1
        else:
            flag_leap = 0
else:
    flag_leap = 0

if flag_leap > 0:
    print("Leap!")
else:
    print("No Leap!")