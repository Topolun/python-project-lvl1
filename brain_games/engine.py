import prompt


def greet():
    name = prompt.string('May I have your name? ')
    print('Hello, ', name + '!')
    return name


def run(game):
    print('Welcome to the Brain Games!')
    print(game.GREETING)
    name = greet()
    for rounds in range(3):
        game_round_data = game.recieve_data_for_round()
        print('Question: ', game_round_data[1])
        user_answer = prompt.string('Your answer: ')
        if game_round_data[0] != user_answer:
            print("'" + str(user_answer) + "'",
                  "is wrong answer ;(. Correct answer was",
                  "'" + str(game_round_data[0]) + "'.",
                  "\nLet's try again,", name + "!")
            return
        print('Correct!')
    print('Congratulations,', name + '!')
