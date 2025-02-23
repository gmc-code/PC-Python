====================================================
Guess the number
====================================================

| The code below shows an example of step-by-step progressions in coding a guessing game.
| The process of making these step-by-step progressions in coding is often called incremental development or iterative development.

| Incremental development focuses on building and improving the program in small, manageable steps, adding features or complexity gradually.
| Iterative development involves repeatedly refining and revisiting the code, testing and adjusting with each version.

----

Version 1
--------------

| This is a simple number guessing game where the program randomly selects a number between 1 and 9.
| The player gets one chance to guess the number.
| If the guess is correct, a congratulatory message is displayed; otherwise, the correct number is revealed.
| This is the most basic version of the game, with no loops or additional features — just a single guess and an immediate result.

.. code-block:: python

    import random

    # Version 1: Simple one-guess game
    print("I have selected a number between 1 and 9. Can you guess it?")
    secret_num = random.randint(1, 9)
    guess = int(input("Enter your guess: "))
    if guess == secret_num:
        print("Congratulations! You guessed correctly.")
    else:
        print("Wrong guess. The number was:", secret_num)

----

Version 2
--------------

| This improved version of the number guessing game introduces a loop, allowing the player to keep guessing until they correctly identify the secret number (between 1 and 9).
| After each incorrect guess, the program provides a hint — either "Too high!" or "Too low!" — guiding the player closer to the correct answer.
| The game ends only when the player guesses correctly, at which point a congratulatory message is displayed.

.. code-block:: python

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

----

Version 3
--------------

| This version of the number guessing game adds a **guess counter**.
| The player continues guessing until they correctly identify the secret number (between 1 and 9).
| Each guess increases the counter by one, and when the correct guess is made, the program congratulates the player and displays the total number of guesses they took.
| This adds a sense of progress and challenge, encouraging the player to guess efficiently.

.. code-block:: python

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

----

Version 4
--------------

| This version of the number guessing game adds a **replay option** and **game statistics**.
| The player guesses a number between 1 and 9 until they get it right, with each guess counted.
| After each game, the total number of games played and the average guesses per game are displayed.
| Players can choose whether to play again or exit.
| Input validation ensures guesses are within range and handles invalid inputs gracefully.
| This version introduces more interactivity and feedback, making the game more dynamic and user-friendly.

.. code-block:: python

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

----


Version 5
--------------

| This version of the number guessing game introduces **modularization and documentation **:

1. **Modular design**:
   - The game logic is split into clearly defined functions:
     - `play_game()`: Handles a single round of the game.
     - `get_guess()`: Manages user input and validation.
     - `generate_secret_number()`: Generates a random number.
     - `check_guess()`: Compares the user's guess to the secret number and provides feedback.
     - `main()`: Oversees game flow, tracking stats and replay options.

2. **Docstrings**:
   - Each function includes a clear docstring explaining its purpose, inputs, and outputs.
   - This enhances maintainability and makes the codebase easier to understand for future development.

Compared to the previous version, this update emphasizes better structure by separating feedback logic from the main game loop. The code is now more modular, extendable, and professional — a solid foundation for future improvements.


.. code-block:: python

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
