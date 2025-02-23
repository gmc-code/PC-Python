from microbit import *
import random


def get_secret(min_num=1, max_num=9):
    # default to from 1 to 9
    return random.randint(min_num, max_num)


def select_number(num, min_num=1, max_num=9):
    # limit to 1 to 9; repeat until both buttons pressed together
    while True:
        display.show(num)
        if button_a.is_pressed() and button_b.is_pressed():
            return num
        elif button_a.is_pressed() and not (button_b.is_pressed()):
            if num > min_num:
                num -= 1
        elif button_b.is_pressed() and not (button_a.is_pressed()):
            if num < max_num:
                num += 1
        sleep(200)


def check_guess(secret_num, guess, game_guesses):
    if guess == secret_num:
        display.show(Image.YES)
        sleep(400)
        display.scroll(str(game_guesses) + " GUESSES", delay=80)
        sleep(400)
        return True
    elif guess > secret_num:
        display.show(Image.ARROW_S)
        sleep(400)
        display.show(str(guess))
    else:
        display.show(Image.ARROW_N)
        sleep(400)
        display.show(str(guess))
    return False

total_games = 0
total_guesses = 0
game_guesses = 0
secret_num = get_secret()
guess = 5

while True:
    guess = select_number(guess, min_num=1, max_num=9)
    game_guesses += 1
    total_guesses += 1
    guessed = check_guess(secret_num, guess, game_guesses)
    if guessed:
        # new game
        secret_num = get_secret()
        game_guesses = 0
        total_games += 1
        display.scroll(str(round(total_guesses / total_games, 1)) + " FOR " + str(total_games) + " GAMES", delay=80)
        sleep(600)
        display.show(guess)

