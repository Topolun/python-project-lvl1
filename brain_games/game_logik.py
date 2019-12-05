from random import randint
import prompt
from brain_games.cli import greet


def game_number():
    random_number = randint(1, 100)
    even = 'no'
    if random_number % 2 == 0:
        even = 'yes'
    print('Question: ', random_number)
    return(even)


def check_answer(answer, user):
    name = user
    correct_answer = answer
    user_answer = prompt.string('Your answer: ')
    if correct_answer != user_answer:
        print("'" + user_answer + "'",
              "is wrong answer ;(. Correct answer was",
              "'" + correct_answer + "'.", "\nLet's try again,", name + "!")
        return False
    print('Correct!')
    return True


def game():
    name = greet()
    for i in range(3):
        if check_answer(game_number(), name) is False:
            return()
        if i == 2:
            print('Congratulations,', name + '!')
