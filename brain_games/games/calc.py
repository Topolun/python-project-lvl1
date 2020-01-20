from random import choice
from random import randint
from operator import add, sub, mul


def recieve_data_for_round():
    operators = [('+', add), ('-', sub), ('*', mul)]
    random_operator = choice(operators)
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    mathemathik_expression = random_operator[1](number1, number2)
    question = "{} {} {}".format(number1, random_operator[0], number2)
    return str(mathemathik_expression), question


GREETING = 'What is the result of the expression?'
