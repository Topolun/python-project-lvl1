from random import choice
from random import randint
from operator import add, sub, mul


def recieve_data_for_round():
    operator_symbol, operator_function = choice(OPERATORS)
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    mathemathik_expression = operator_function(number1, number2)
    question = "{} {} {}".format(number1, operator_symbol, number2)
    return str(mathemathik_expression), question


OPERATORS = [('+', add), ('-', sub), ('*', mul)]
GREETING = 'What is the result of the expression?'
