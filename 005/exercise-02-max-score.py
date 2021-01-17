student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
    
# Defining the first value for the variable max_score
max_score = student_scores[0]

# First Way:
# Iterating all the elements of the studen_score, iterating by index
for n in range(1, len(student_scores)):
# Converting to int data type to do calculations
    student_scores[n] = int(student_scores[n])
# Comparing the next element in student_scores with the first value
# If the next element is grather than max_score, then max_score will take the new value.
    if student_scores[n] > max_score:
        max_score = student_scores[n]

print(f"The highest score in the class is {max_score}")

# Second Way
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is {highest_score}")
