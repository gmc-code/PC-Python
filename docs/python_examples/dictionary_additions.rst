====================================================
User additions to dictionary
====================================================

| The code below maintains a dictionary of the top Australian Football League (AFL) teams and their premiership counts.
| It repeatedly prompts the user to input a team's short name and checks if the team is in the dictionary.
| If the team is found, it displays the number of premierships won.
| If not, it asks the user to input the number of premierships for the new team and updates the dictionary.
| The loop continues until the user decides to stop, after which the final dictionary is printed.


.. code-block:: python

    premiers = {"ESS": 16, "COLL": 16, "CARL": 16, "MELB": 13, "RICH": 13, "HAW": 13, "GEE": 10}

    while True:
        user_team = input("What team (short name)? ").upper().strip()

        # Check if the input is valid (not empty and only letters)
        if not user_team.isalpha():
            print("Invalid input. Please enter a valid team short name consisting of letters only.")
            continue

        team_premierships = premiers.get(user_team)
        if team_premierships is None:
            print(f"{user_team} is not in the dictionary")
            while True:
                try:
                    new_team_premierships = int(input("How many premierships have they won? "))
                    break
                except ValueError:
                    print("Please enter a valid number.")
            premiers[user_team] = new_team_premierships
            print(f"{user_team} has won {new_team_premierships} premierships.")
        else:
            print(f"{user_team} has won {team_premierships} premierships.")

        get_more_premiers = input("Press Enter to continue or any other key to exit: ").strip()
        if get_more_premiers != "":
            print("Exiting the program.\n")
            break

    print(premiers)



Explanation
--------------------


1. **Initialize Dictionary**:

- The `premiers` dictionary is initialized with team abbreviations as keys and their respective premiership counts as values.

    .. code-block:: python

        premiers = {"ESS": 16, "COLL": 16, "CARL": 16, "MELB": 13, "RICH": 13, "HAW": 13, "GEE": 10}


1. **Start Infinite Loop**:

 - The `while True:` loop begins, allowing the program to repeatedly prompt the user for input until explicitly broken.

.. code-block:: python

    while True:


3. **Get User Input**:

 - The user is prompted to enter a team's short name, which is then converted to uppercase and stripped of any leading or trailing whitespace.

.. code-block:: python

    user_team = input("What team (short name)? ").upper().strip()


4. **Validate User Input**:

- The code checks if the input is valid (i.e., not empty and consists only of letters). If the input is invalid, it prints an error message and continues to the next iteration of the loop.

.. code-block:: python

    if not user_team.isalpha():
        print("Invalid input. Please enter a valid team short name consisting of letters only.")
        continue


5. **Check Team in Dictionary**:

- The code attempts to retrieve the number of premierships for the entered team from the `premiers` dictionary.

.. code-block:: python

    team_premierships = premiers.get(user_team)


6. **Handle Team Not Found**:

- If the team is not found in the dictionary (`team_premierships` is `None`), the code informs the user and prompts for the number of premierships the team has won. It then adds this new entry to the dictionary.

.. code-block:: python

    if team_premierships is None:
        print(f"{user_team} is not in the dictionary")
        while True:
            try:
                new_team_premierships = int(input("How many premierships have they won? "))
                break
            except ValueError:
                print("Please enter a valid number.")
        premiers[user_team] = new_team_premierships
        print(f"{user_team} has won {new_team_premierships} premierships.")


7. **Handle Team Found**:

- If the team is found in the dictionary, the code prints the number of premierships the team has won.

.. code-block:: python

    else:
        print(f"{user_team} has won {team_premierships} premierships.")


8. **Prompt to Continue or Exit**:

- The user is prompted to press Enter to continue or any other key to exit. If the user chooses to exit, the loop breaks.

.. code-block:: python

    get_more_premiers = input("Press Enter to continue or any other key to exit: ").strip()
    if get_more_premiers != "":
        print("Exiting the program.\n")
        break


9. **Print Final Dictionary**:

- After the loop ends, the final state of the `premiers` dictionary is printed.

.. code-block:: python

    print(premiers)
