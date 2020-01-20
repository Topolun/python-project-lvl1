from random import randint


def recieve_data_for_round():
    first_number = randint(1, 100)
    progression_output = ''
    step = randint(1, 10)
    unknown_number = randint(0, 9)
    correct_answer = 0
    for i in range(10):
        if i == unknown_number:
            progression_output = progression_output + '.. '
            correct_answer = first_number + step * i
        else:
            progression_output += str(first_number + step * i) + ' '
    return str(correct_answer), progression_output


GREETING = 'What number is missing in the progression?'
