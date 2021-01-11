print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

both = name1.lower() + " " + name2.lower()

true = "true"
love = "love"

count_true = 0
count_love = 0


for i in range(len(true)):
    count_true += both.count(true[i])
for j in range(len(love)):
    count_love += both.count(love[j])
print(count_true)
print(count_love)

score = str(count_true) + str(count_love)
_score = int(score)

if _score < 10 or _score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif _score > 40 and _score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
