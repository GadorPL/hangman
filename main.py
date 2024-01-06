import random

word_list = ["aardvark", "baboon", "camel"]

word_to_guess = list(random.choice(word_list))


letter = input("Guess a letter: ").lower()

if letter in word_to_guess:
    print("Right")
else:
    print("Wrong")
