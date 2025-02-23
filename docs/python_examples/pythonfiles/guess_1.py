import random

# Version 1: Simple one-guess game
print("I have selected a number between 1 and 9. Can you guess it?")
secret_num = random.randint(1, 9)
guess = int(input("Enter your guess: "))
if guess == secret_num:
    print("Congratulations! You guessed correctly.")
else:
    print("Wrong guess. The number was:", secret_num)
