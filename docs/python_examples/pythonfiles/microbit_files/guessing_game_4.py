from microbit import *
import random


def get_secret(min_num=1, max_num=9):
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


def check_guess(secret_num, guess):
    if guess == secret_num:
        display.show(Image.YES)
        sleep(400)
        return True
    elif guess > secret_num:
        display.show(Image.ARROW_S)
        sleep(400)
        display.show(guess)
        return False
    else:
        display.show(Image.ARROW_N)
        sleep(400)
        display.show(guess)
        return False


def get_best_score(best_score, game_guesses):
    if best_score is None:
        return game_guesses
    else:
        return min(best_score, game_guesses)


total_games = 1
best_score = None
secret_num = get_secret()
guess = 5
game_guesses = 0
guessed = False
display.scroll("1-9?")
while True:
    guess = select_number(guess, min_num=1, max_num=9)
    game_guesses += 1
    guessed = check_guess(secret_num, guess)
    if guessed:
        display.scroll(str(game_guesses) + " GUESSES", delay=80)
        best_score = get_best_score(best_score, game_guesses)
        display.scroll("BEST: " + str(best_score) + " GAMES: " + str(total_games), delay=80)
        # new game
        total_games += 1
        secret_num = get_secret()
        guess = 5
        game_guesses = 0
        guessed = False
