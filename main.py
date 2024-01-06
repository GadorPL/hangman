import random

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
word_to_guess = random.choice(word_list)
lives = 6

print(f'Pssst, the solution is {word_to_guess}.')


display = []
for i in range(len(word_to_guess)):
    display.append("_")

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    for position in range(len(word_to_guess)):
        letter = word_to_guess[position]
        if letter == guess:
            display[position] = letter
    if guess not in word_to_guess:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")

    print(f"{' '.join(display)}")
    print(stages[lives])

    if "_" not in display:
        game_over = True
        print("You win.")



