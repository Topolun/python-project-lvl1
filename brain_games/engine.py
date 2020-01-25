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
        correct_answer, question = game.recieve_data_for_round()
        print('Question: ', question)
        user_answer = prompt.string('Your answer: ')
        if correct_answer != user_answer:
            print("'" + str(user_answer) + "'",
                  "is wrong answer ;(. Correct answer was",
                  "'" + str(correct_answer) + "'.",
                  "\nLet's try again,", name + "!")
            return
        print('Correct!')
    print('Congratulations,', name + '!')
