from random import randint


def recieve_data_for_round():
    progression = randint(1, 100)
    progression_output = ''
    step = randint(1, 10)
    unknown_number = randint(0, 9)
    correct_answer = 0
    for i in range(10):
        '''
        В случае 'step * i' не учитывается случай, когда скрытым числом
        является 0, либо все прогрессии начинаются с 0
        '''
        if i != 0:
            progression = progression + step
        if i == unknown_number:
            progression_output = progression_output + '.. '
            correct_answer = progression
        else:
            progression_output = progression_output + str(progression) + ' '
    return str(correct_answer), progression_output


GREETING = 'What number is missing in the progression?'
