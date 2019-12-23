from brain_games.game_logik import check_answer, game_number, greet


def game_even_run():
    name = greet()
    for i in range(3):
        if check_answer(game_even(game_number()), name) is False:
            return()
        if i == 2:
            print('Congratulations,', name + '!')


def game_even(number):
    even = 'no'
    random_number = number
    if random_number % 2 == 0:
        even = 'yes'
    print('Question: ', random_number)
    return(even)
