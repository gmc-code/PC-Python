====================================================
Dictionary Question and Answer
====================================================

| This Python code is a quiz program about AFL premierships.
| It includes a function to clear the terminal screen, a dictionary of AFL teams and their premiership counts, and displays this list to the user.
| The user is then prompted to start a quiz where they guess the number of premierships won by randomly selected teams.
| The program checks the user's guess, provides feedback, and allows the user to continue or exit the quiz.
| Finally, it prints the list of teams and their premierships again after the quiz ends.

.. code-block:: python

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

    # Display the list of premiers for study
    print("List of AFL Premiers:\n")
    for team, premierships in premiers.items():
        print(f"{team}: {premierships} premierships")

    # Prompt to start the quiz
    start_quiz = input("\nDo you want to start the quiz? (Y/N): ").strip().upper()

    if start_quiz == "Y":
        clear_screen()  # Clear the terminal screen before starting the quiz
        while True:
            # Randomly select a team
            team = random.choice(list(premiers.keys()))

            # Ask the user to guess the number of premierships
            user_guess = input(f"How many premierships has {team} won? ").strip()

            # Get the correct number of premierships
            correct_premierships = premiers[team]

            # Check if the user's guess is correct
            if user_guess.isdigit() and int(user_guess) == correct_premierships:
                print("Correct!\n")
            else:
                print(f"Incorrect. {team} has won {correct_premierships} premierships.\n")

            # Ask the user if they want to continue or exit
            user_input = input("Press Enter to continue or any other key to exit: ").strip()
            if user_input != "":
                print("Exiting the program.\n")
                break

    print("\nFinal list of teams and their premierships:\n", premiers,"\n")

----

**Importing Modules**:
-----------------------------------------------------------------------

.. code-block:: python

   import random
   import os

- `random`: This module is used to generate random numbers or select random items.
- `os`: This module provides a way to interact with the operating system, such as clearing the terminal screen.

**Function to Clear the Terminal Screen**:
-----------------------------------------------------------------------

.. code-block:: python

   def clear_screen():
       if os.name == 'nt':
           _ = os.system('cls')
       else:
           _ = os.system('clear')


- `clear_screen()`: This function clears the terminal screen. It checks the operating system (`os.name`) and uses the appropriate command (`cls` for Windows and `clear` for macOS/Linux).

**Dictionary of AFL Premiers**:
-----------------------------------------------------------------------

.. code-block:: python

   premiers = {
       "Essendon": 16,
       "Collingwood": 16,
       "Carlton": 16,
       "Melbourne": 13,
       "Richmond": 13,
       "Hawthorn": 13,
       "Geelong": 10,
       "Sydney Swans": 5,
       "Brisbane Lions": 4,
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


- This dictionary stores AFL teams as keys and their respective number of premierships as values.

**Displaying the List of Premiers**:
-----------------------------------------------------------------------

.. code-block:: python

   print("List of AFL Premiers:\n")
   for team, premierships in premiers.items():
       print(f"{team}: {premierships} premierships")


- This code prints the list of AFL teams and their premiership counts.

**Prompt to Start the Quiz**:
-----------------------------------------------------------------------

.. code-block:: python

   start_quiz = input("\nDo you want to start the quiz? (Y/N): ").strip().upper()


- The user is asked if they want to start the quiz. The input is stripped of any leading/trailing whitespace and converted to uppercase.

**Quiz Logic**:
-----------------------------------------------------------------------

.. code-block:: python

   if start_quiz == "Y":
       clear_screen()
       while True:
           team = random.choice(list(premiers.keys()))
           user_guess = input(f"How many premierships has {team} won? ").strip()
           correct_premierships = premiers[team]

           if user_guess.isdigit() and int(user_guess) == correct_premierships:
               print("Correct!\n")
           else:
               print(f"Incorrect. {team} has won {correct_premierships} premierships.\n")

           user_input = input("Press Enter to continue or any other key to exit: ").strip()
           if user_input != "":
               print("Exiting the program.\n")
               break


- If the user chooses to start the quiz (`start_quiz == "Y"`), the screen is cleared.
- A loop begins where a random team is selected.
- The user is prompted to guess the number of premierships for the selected team.
- The guess is checked against the correct number of premierships.
- Feedback is provided based on the user's guess.
- The user can choose to continue or exit the quiz.

**Final Display**:
-----------------------------------------------------------------------

.. code-block:: python

   print("\nFinal list of teams and their premierships:\n", premiers,"\n")

- After the quiz ends, the final list of teams and their premierships is printed again.



