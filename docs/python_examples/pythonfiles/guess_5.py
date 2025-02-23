import random


def play_game():
    """
    Plays a single round of the number guessing game.
    Generates a random number and prompts the user to guess until correct.
    Returns the number of guesses made.
    """
    secret_num = generate_secret_number()
    game_guesses = 0
    print("\nI have selected a number between 1 and 9. Can you guess it?")

    while True:
        guess = get_guess()
        game_guesses += 1
        if check_guess(secret_num, guess, game_guesses):
            return game_guesses


def check_guess(secret_num, guess, game_guesses):
    """
    Compares the user's guess to the secret number.
    Provides feedback if the guess is too high, too low, or correct.
    Returns True if the guess is correct, otherwise False.
    """
    if guess == secret_num:
        print("Congratulations! You guessed the number in", game_guesses, "guesses.")
        return True
    elif guess > secret_num:
        print("Too high!")
    else:
        print("Too low!")
    return False


def get_guess():
    """
    Prompts the user for a guess and validates input.
    Ensures the guess is an integer between 1 and 9.
    Returns the valid guess.
    """
    while True:
        try:
            guess = int(input("Enter your guess (1-9): "))
            if 1 <= guess <= 9:
                return guess
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def generate_secret_number():
    """
    Generates and returns a random integer between 1 and 9.
    """
    return random.randint(1, 9)


def main():
    """
    Main function to run the number guessing game.
    Tracks total games played and calculates average guesses per game.
    Offers the option to replay or exit the game.
    """
    total_guesses = 0
    total_games = 0

    while True:
        game_guesses = play_game()
        total_guesses += game_guesses
        total_games += 1
        avg_guesses = round(total_guesses / total_games, 1)
        print(f"Average guesses per game: {avg_guesses} over {total_games} game(s).")

        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
