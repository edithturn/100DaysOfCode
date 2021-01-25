import random
#Step 1 

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


chosen_word = word_list[random.randrange(0, (len(word_list)))]
#chosen_word = random.choice(word_list)
print(chosen_word)

new_list = []
points_to_won = len(chosen_word)
current_points = 0
gallow_steps = len(stages)
stages.reverse()
len_gallow = len(stages)
lost_points = 0


for i in range(0, len(chosen_word)):
    new_list.append("_")

while "_" in  new_list:
    guess = input("Type a letter:").lower()
    attempt = 0
    for index in range(0, len(chosen_word)):
        if guess == chosen_word[index]:
            new_list[index] = guess
            attempt = 1
    print(new_list)
    if attempt == 0 and lost_points < len(chosen_word):
        print(stages[lost_points])
        lost_points += 1
    if lost_points >= len(chosen_word):
        print(lost_points)
        print(len(chosen_word))
        print("You lost")
        print(stages[-1])
        break        
    if attempt == 1:
        current_points += 1
        if  current_points == len(chosen_word):
            print("You Win!")
            break

        
        






    