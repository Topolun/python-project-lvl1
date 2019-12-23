from random import choice
from brain_games.game_logik import check_answer, game_number, greet


def game_calc_run():
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
