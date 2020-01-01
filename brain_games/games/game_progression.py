from brain_games.game_logik import check_answer, game_number, greet


def game_progression():
    progression = game_number()
    step = game_number(1, 10)
    unknown_number = game_number(0, 9)
    correct_answer = 0
    for i in range(10):
        if i != 0:
            progression = progression + step
        if i == unknown_number:
            print('..', end=' ')
            correct_answer = progression
        else:
            print(progression, end=' ')
    return(str(correct_answer))


def game_progression_run():
    name = greet()
    for i in range(3):
        if check_answer(game_progression(), name) is False:
            return()
        if i == 2:
            print('Congratulations,', name + '!')
