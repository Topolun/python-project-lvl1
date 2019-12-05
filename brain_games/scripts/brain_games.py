from brain_games.cli import greet


def main():
    print('''Welcome to the Brain Games!
        \rSay "Yes" if number even otherwise answer "no".''')
    name = greet()
    print(name)


if __name__ == '__main__':
    main()
