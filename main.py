import random
from words import word_list
from art import logo, stages


word_to_guess = random.choice(word_list)
lives = 6

print(logo)

display = []
for i in range(len(word_to_guess)):
    display.append("_")

game_over = False

user_guesses = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in user_guesses:
        print(f"You already tried {guess}. Try different letter.")
        continue

    user_guesses.append(guess)

    for position in range(len(word_to_guess)):
        letter = word_to_guess[position]
        if letter == guess:
            display[position] = letter
    if guess not in word_to_guess:
        lives -= 1
        print("You lose a life")
        if lives == 0:
            game_over = True
            print("You lose.")

    print(f"{' '.join(display)}")
    print(stages[lives])

    if "_" not in display:
        game_over = True
        print("You win.")

print(f"The word was {word_to_guess}.")

