import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


chosen_word = word_list[random.randrange(0, (len(word_list)))]
print(chosen_word)

guess = input("Type a letter:").lower()
print(guess)

for letter in chosen_word:
    if guess == letter:
        print(guess)