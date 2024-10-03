import random
import os

# Function to clear the terminal screen
def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

# Dictionary of premiers with full team names
premiers = {
    "Essendon": 16,
    "Collingwood": 16,
    "Carlton": 16,
    "Melbourne": 13,
    "Richmond": 13,
    "Hawthorn": 13,
    "Geelong": 10,
    "Sydney Swans": 5,  # Linked to South Melbourne
    "Brisbane Lions": 4,  # Linked to Fitzroy
    "West Coast Eagles": 4,
    "North Melbourne": 4,
    "Western Bulldogs": 2,
    "Adelaide": 2,
    "Port Adelaide": 1,
    "St Kilda": 1,
    "Fremantle": 0,
    "Greater Western Sydney": 0,
    "Gold Coast": 0,
    "Fitzroy": 8,
    "South Melbourne": 3
}

def play_game():
    # Randomly sort the list of teams
    teams = list(premiers.keys())
    random.shuffle(teams)

    score = 0
    for team in teams:
        # Ask the user to guess the number of premierships
        user_guess = input(f"How many premierships has {team} won? ").strip()

        # Get the correct number of premierships
        correct_premierships = premiers[team]

        # Check if the user's guess is correct
        if user_guess.isdigit() and int(user_guess) == correct_premierships:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. {team} has won {correct_premierships} premierships.\n")
            break

    if score == len(teams):
        print(f"Congratulations! You answered all {score} questions correctly and are a winner!\n")
    else:
        print(f"You answered {score} questions correctly in a row.\n")

clear_screen()
# Print the rules of the game
print("\nWelcome to the AFL Premiership Quiz Game!\n")
print("Rules:")
print("1. You will be asked to guess the number of premierships won by a randomly sorted list of AFL teams.")
print("2. If you guess correctly, you will be asked another question.")
print("3. The game continues until you answer incorrectly or all teams are done.")
print("4. Your score is the number of consecutive correct answers. Answer all correctly to win!\n")

# Main game loop
while True:
    # Prompt to start the quiz
    start_quiz = input("Do you want to start the quiz? (Y/N): ").strip().upper()

    if start_quiz == "Y":
        clear_screen()  # Clear the terminal screen before starting the quiz
        play_game()
    else:
        print("Exiting the program.")
        break

print("Thank you for playing the AFL Premiership Quiz Game!")
