import random


# Version 3: Adding a guess counter
print("\nI have selected a number between 1 and 9. How many guesses will you need?")
secret_num = random.randint(1, 9)
guesses = 0
while True:
    guess = int(input("Enter your guess: "))
    guesses += 1
    if guess == secret_num:
        print(f"Congratulations! You guessed correctly in {guesses} guesses.")
        break
    elif guess > secret_num:
        print("Too high!")
    else:
        print("Too low!")


