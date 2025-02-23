from microbit import *
import random


def get_secret(min_num=1, max_num=9):
    # default to from 1 to 9
    return random.randint(min_num, max_num)


def select_number(start_num, min_num=1, max_num=9):
    counter = start_num
    display.show(counter, delay=200)
    while button_b.was_pressed() is False:
        if button_a.is_pressed():
            counter += 1
            if counter > max_num:
                counter = min_num
            display.show(counter, delay=200)
        sleep(200)
    return counter


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


game_guesses = 0
secret_num = get_secret()
guess = 5

while True:
    guess = select_number(guess, min_num=1, max_num=9)
    game_guesses += 1
    guessed = check_guess(secret_num, guess, game_guesses)
    if guessed:
        # new game
        secret_num = get_secret()
        game_guesses = 0
