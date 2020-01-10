from brain_games.game_logik import game_number


def game_prime():
    game_greeting = ('Answer "yes" if given number is prime. '
                     'Otherwise answer "no".')
    prime = 'no'
    check_number = game_number()
    devider = 2
    while devider ** 2 <= check_number and check_number % devider != 0:
        devider = +1
    if devider ** 2 > check_number:
        prime = 'yes'
    return(prime, check_number, game_greeting)
