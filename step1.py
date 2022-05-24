import random

# Step 1

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


# 1

result = []
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
for x in range(word_length ):
    result.append('_')

guess = input("Guess a letter: ").lower()

for x in range(word_length):
    letter = chosen_word[x]
    if letter == guess:
        result[x] = guess

print(result)

