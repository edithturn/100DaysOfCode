print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Applying lower case for both text and concatenating
both = name1.lower() + " " + name2.lower()

# Defining the words to compare with the names
true = "true"
love = "love"

# Initializaing the counters
count_true = 0
count_love = 0

# Searching each letter of the word "true" in both names
for i in range(len(true)):
# Counting the number of letters mached
    count_true += both.count(true[i])
# Searching each letter of the word "love" in both names
for j in range(len(love)):
# Counting the number of letters mached
    count_love += both.count(love[j])

# Concatenating both numbers in a single digit
score = int(str(count_true) + str(count_love))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score > 40) and (score < 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
