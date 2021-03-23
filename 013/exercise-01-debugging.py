############DEBUGGING#####################

# Describe Problem
"""The problem is in range function, it takes from 1 until [ 20 - 1 ], It will never going to arrive 20. So It will never print nothing"""
def my_function():
    for i in range(1, 20):
        if i == 19:
            print("You got it")
my_function()


