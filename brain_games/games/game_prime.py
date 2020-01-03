from brain_games.game_logik import check_answer, game_number, greet


def game_prime_run():
    name = greet()
    for i in range(3):
        if check_answer(game_prime(), name) is False:
            return()
        if i == 2:
            print('Congratulations,', name + '!')


def game_prime():
    prime = 'no'
    check_number = game_number()
    devider = 2
    print('Question: ', check_number)
    while devider ** 2 <= check_number and check_number % devider != 0:
        devider = +1
    if devider ** 2 > check_number:
        prime = 'yes'
    return(prime)
