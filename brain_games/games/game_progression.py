from brain_games.game_logik import game_number


def game_progression():
    game_greeting = ('What number is missing in the progression?')
    progression = game_number()
    progression_output = ''
    step = game_number(1, 10)
    unknown_number = game_number(0, 9)
    correct_answer = 0
    for i in range(10):
        if i != 0:
            progression = progression + step
        if i == unknown_number:
            progression_output = progression_output + '.. '
            correct_answer = progression
        else:
            progression_output = progression_output + str(progression) + ' '
    return(str(correct_answer), progression_output, game_greeting)
