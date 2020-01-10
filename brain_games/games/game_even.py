from brain_games.game_logik import game_number


def game_even():
    game_greeting = ('Say "Yes" if number even otherwise answer "no".')
    even = 'no'
    random_number = game_number()
    if random_number % 2 == 0:
        even = 'yes'
    return(even, random_number, game_greeting)
