from random import randint


def recieve_data_for_round():
    random_number = randint(1, 100)
    if random_number % 2 == 0:
        even = 'yes'
    else:
        even = 'no'
    return even, random_number


GREETING = 'Say "Yes" if number even otherwise answer "no".'
