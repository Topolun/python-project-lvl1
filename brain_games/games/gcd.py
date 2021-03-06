from random import randint


def greatest_common_devisor(first_number, second_number):
    while first_number != second_number:
        if first_number > second_number:
            first_number = first_number - second_number
        else:
            second_number = second_number - first_number
    return first_number


def recieve_data_for_round():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    question = "{} {}".format(first_number, second_number)
    return str(greatest_common_devisor(first_number, second_number)), question


GREETING = 'Find the greatest common divisor of given numbers.'
