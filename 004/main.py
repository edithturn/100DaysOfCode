import random
import my_module

i = 1
j = 50

a = random.randrange(i, j)
try:
    b = random.randrange(i, j)
except ValueError:
    print('ValueError on randrange() since start > stop')


print('i =', i, 'and j = ', j)
print('randrange() generated number: ' , a)
print('randint() generated number:', b)

print(my_module.pi*a*b)
random_float = random.random() * 5
print(random_float)