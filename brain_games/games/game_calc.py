from random import choice
from brain_games.game_logik import game_number


def game_calc():
    game_greeting = ('What is the result of the expression?')
    operators = ['+', '-', '*']
    random_operator = choice(operators)
    number1 = game_number()
    number2 = game_number()
    mathemathik_expression = eval(str(number1) + random_operator
                                  + str(number2))
    question = str(number1) + ' ' + random_operator + ' ' + str(number2)
    return(str(mathemathik_expression), question, game_greeting)
