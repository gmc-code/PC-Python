from microbit import *
import random


def get_secret(min_num=1, max_num=9):

    return random.randint(min_num, max_num)


def select_number1():
    counter = middle_index
    display.show(chars[counter])
    while button_b.was_pressed() is False:
        if button_a.is_pressed():
            counter += 1
            if counter == max_char_index:
                counter = 0
            display.show(chars[counter])
        sleep(200)
    return counter


def select_number(num, min_num=1, max_num=9):
    num = select_number1() * 10 + select_number1()
    if num > 9:
        display.scroll(num, delay=80)
    else:
        display.show(num)
    return num


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
guess = 50

while True:
    guess = select_number(guess, min_num=1, max_num=99)
    game_guesses += 1
    total_guesses += 1
    guessed = check_guess(secret_num, guess, game_guesses)
    if guessed:
        # new game
        secret_num = get_secret()
        game_guesses = 0
        total_games += 1
        display.scroll(
            str(round(total_guesses / total_games, 1))
            + " FOR "
            + str(total_games)
            + " GAMES",
            delay=80,
        )
        sleep(600)
        display.show(guess)
