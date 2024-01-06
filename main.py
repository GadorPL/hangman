import random

word_list = ["aardvark", "baboon", "camel"]
word_to_guess = random.choice(word_list)

print(f'Pssst, the solution is {word_to_guess}.')


display = []
for i in range(len(word_to_guess)):
    display.append("_")

letter = input("Guess a letter: ").lower()

index = -1
for i in word_to_guess:
    index += 1
    if letter == i:
        print("Right")
        display[index] = letter
    else:
        print("Wrong")

print(display)
