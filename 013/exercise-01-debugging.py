############DEBUGGING#####################

# Describe Problem [ SOLVED ]
# """The problem is in range function, it takes from 1 until [ 20 - 1 ],
#  It will never going to arrive 20. So It will never print nothing"""
# def my_function():
#     for i in range(1, 20):
#         if i == 19:
#             print("You got it")
# my_function()


# Reproduce the Bug 

# """The function randint(start, stop), 
# takes two arguments, start = 1 and stop = 6, 
# if we want to print dice_imgs[6] this will give us list index out of range in an error """
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_num)
# print(dice_imgs[dice_num])


# Play Computer
# """To take the values 1980 and 1994 we should include then in the interval """
# year = int(input("What's your year of birth? "))
# if year >= 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year >  1994:
#   print("You are a Gen Z.")

# Fix the Errors
"""To use age as a number, we should convert into a int"""
age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])