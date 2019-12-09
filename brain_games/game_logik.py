from random import randint
from random import choice
import prompt
from brain_games.cli import greet


def game_number():
    random_number = randint(1, 100)
    return(random_number)


def game_even(number):
    even = 'no'
    random_number = number
    if random_number % 2 == 0:
        even = 'yes'
    print('Question: ', random_number)
    return(even)


def check_answer(answer, user):
    name = user
    correct_answer = answer
    user_answer = prompt.string('Your answer: ')
    if correct_answer != user_answer:
        print("'" + str(user_answer) + "'",
              "is wrong answer ;(. Correct answer was",
              "'" + str(correct_answer) + "'.",
              "\nLet's try again,", name + "!")
        return False
    print('Correct!')
    return True


def game():
    name = greet()
    for i in range(3):
        if check_answer(game_even(game_number()), name) is False:
            return()
        if i == 2:
            print('Congratulations,', name + '!')


def game1():
    name = greet()
    for i in range(3):
        if check_answer(game_calc(game_number(),
                        game_number()), name) is False:
            return()
        if i == 2:
            print('Congratulations,', name + '!')


def game_calc(number1, number2):
    operators = ['+', '-', '*']
    random_operator = choice(operators)
    mathemathik_expression = eval(str(number1) + random_operator
                                  + str(number2))
    print('Question: ', str(number1), random_operator, str(number2))
    return(str(mathemathik_expression))
