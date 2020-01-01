from random import randint
import prompt


def greet():
    name = prompt.string('May I have your name? ')
    print('Hello, ', name + '!')
    return(name)


def game_number(argument1=1, argument2=100):
    random_number = randint(argument1, argument2)
    return(random_number)


def check_answer(answer, user):
    name = user
    correct_answer = answer
    user_answer = prompt.string('Your answer: ')
    if correct_answer != user_answer:
        print("'" + str(user_answer) + "'",
              "is wrong answer ;(. Correct answer was",
              "'" + str(correct_answer) + "'.",
              "\nLet's try again,", name + "!")
        return False
    print('Correct!')
    return True
