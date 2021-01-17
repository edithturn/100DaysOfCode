
student_heights = input("Input a list of student heights ").split()
sum = 0
counter = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    sum += student_heights[n]
    counter = n

print((round(sum/(counter + 1))))
