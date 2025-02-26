import random
import tkinter as tk

# Initialize global variables
total_guesses = 0
total_games = 0
secret_num = None
game_guesses = 0


def generate_secret_number():
    """
    Generates and returns a random integer between 1 and 9.
    """
    return random.randint(1, 9)


def play_game():
    """
    Starts a new game round by generating a secret number and resetting guess count.
    """
    global secret_num, game_guesses
    secret_num = generate_secret_number()
    game_guesses = 0
    feedback_label.config(text="I have selected a number between 1 and 9. Can you guess it?")
    guess_entry.delete(0, tk.END)


def get_guess():
    """
    Retrieves the user's guess from the entry field.
    Validates that it's an integer between 1 and 9.
    """
    try:
        guess = int(guess_entry.get())
        if 1 <= guess <= 9:
            return guess
        else:
            feedback_label.config(text="Please enter a number between 1 and 9.")
    except ValueError:
        feedback_label.config(text="Invalid input. Please enter a number.")
    return None


def check_guess():
    """
    Compares the user's guess to the secret number and updates feedback.
    Tracks number of guesses and shows results on win.
    """
    global game_guesses, total_guesses, total_games
    guess = get_guess()
    if guess is None:
        return

    game_guesses += 1
    total_guesses += 1

    if guess == secret_num:
        total_games += 1
        avg_guesses = round(total_guesses / total_games, 1)
        feedback_label.config(text=f"Congratulations! You guessed the number in {game_guesses} guesses.\nAverage guesses per game: {avg_guesses}")
    elif guess > secret_num:
        feedback_label.config(text="Too high! Try again.")
    else:
        feedback_label.config(text="Too low! Try again.")


def main():
    """
    Initializes the game and sets up the Tkinter GUI.
    """
    global root, feedback_label, guess_entry
    root = tk.Tk()
    root.title("Number Guessing Game")

    tk.Label(root, text="Guess a number between 1 and 9:").pack(pady=10)
    guess_entry = tk.Entry(root)
    guess_entry.pack(pady=5)

    tk.Button(root, text="Submit Guess", command=check_guess).pack(pady=5)
    feedback_label = tk.Label(root, text="")
    feedback_label.pack(pady=10)

    tk.Button(root, text="Play Again", command=play_game).pack(pady=5)
    tk.Button(root, text="Quit", command=root.quit).pack(pady=5)

    play_game()  # Start the first game
    root.mainloop()


if __name__ == "__main__":
    main()
