import random

word_list = ["aardvark", "baboon", "camel"]
word_to_guess = random.choice(word_list)

print(f'Pssst, the solution is {word_to_guess}.')


display = []
for i in range(len(word_to_guess)):
    display.append("_")

guess = input("Guess a letter: ").lower()

for position in range(len(word_to_guess)):
    letter = word_to_guess[position]
    if letter == guess:
        display[position] = letter

print(display)
