import random

# Version 2: Repeated guessing until correct
print("\nI have selected a number between 1 and 9. Keep guessing until you get it right!")
secret_num = random.randint(1, 9)
while True:
    guess = int(input("Enter your guess: "))
    if guess == secret_num:
        print("Congratulations! You guessed correctly.")
        break
    elif guess > secret_num:
        print("Too high!")
    else:
        print("Too low!")
