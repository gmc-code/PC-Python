import random


# Version 4: game with replay option
total_guesses = 0
total_games = 0

while True:
    secret_num = random.randint(1, 9)
    game_guesses = 0
    print("\nI have selected a number between 1 and 9. Can you guess it?")
    while True:
        try:
            guess = int(input("Enter your guess (1-9): "))
            if 1 <= guess <= 9:
                game_guesses += 1
                total_guesses += 1
                if guess == secret_num:
                    print("Congratulations! You guessed the number in",
                          game_guesses, "guesses.")
                    break
                elif guess > secret_num:
                    print("Too high!")
                else:
                    print("Too low!")
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    total_games += 1
    avg_guesses = round(total_guesses / total_games, 1)
    print(
        f"Average guesses per game: {avg_guesses} over {total_games} game(s).")
    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again != "y":
        print("Thanks for playing!")
        break
