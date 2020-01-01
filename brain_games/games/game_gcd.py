from brain_games.game_logik import check_answer, game_number, greet


def game_gcd(number1, number2):
    first_number = number1
    second_number = number2
    print('Question: ', first_number, second_number)
    while first_number != second_number:
        if first_number > second_number:
            first_number = first_number - second_number
        else:
            second_number = second_number - first_number
    return(str(first_number))


def game_gcd_run():
    name = greet()
    for i in range(3):
        if check_answer(game_gcd(game_number(), game_number()), name) is False:
            return()
        if i == 2:
            print('Congratulations,', name + '!')
