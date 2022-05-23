import random

# Step 1

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


# 1

chosen_word = random.choice(word_list)

for x in chosen_word:
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        print("해당 알파벳은 포함되어있습니다.")
    else:
        print("해당 알파벳은 포함되어 있지 않습니다.")


