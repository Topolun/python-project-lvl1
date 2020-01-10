from brain_games.game_logik import game_number


def game_gcd():
    game_greeting = ('Find the greatest common divisor of given numbers.')
    first_number = game_number()
    second_number = game_number()
    question = str(first_number) + ', ' + str(second_number)
    while first_number != second_number:
        if first_number > second_number:
            first_number = first_number - second_number
        else:
            second_number = second_number - first_number
    return(str(first_number), question, game_greeting)
