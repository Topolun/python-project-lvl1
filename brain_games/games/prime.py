from random import randint


def is_prime(number):
    divider = 2
    prime = 'no'
    nummber_sqrt = number**0.5
    while divider <= nummber_sqrt and number % divider != 0:
        divider += 1
    if divider > nummber_sqrt:
        prime = 'yes'
    return prime


def recieve_data_for_round():
    number_to_check = randint(1, 100)
    prime = is_prime(number_to_check)
    return prime, number_to_check


GREETING = '''Answer "yes" if given number is prime.
             \rOtherwise answer "no".'''
