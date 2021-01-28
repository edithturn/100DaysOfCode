def prime_checker(number):
    c = 1
    if number == 1  or number == 2:
        c = 6
    while c <= 5:
        c = c + 1
        if c == number:
            c = c + 1
        if number % c == 0:
            print(f"{number} - No primo")
            break
    if c == 6:
        print(f"{number} - Is prime!")
#n = int(input("Check this number: "))
#prime_checker(number=n)

for number in range (1, 101):
    prime_checker(number)