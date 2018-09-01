def main():
    print_header()

    game_loop()


def print_header():
    print('---------------------------')
    print('       WIZARD BATTLE')
    print('---------------------------')


def game_loop():

    while True:

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around?')
        if cmd == 'a':
            print('attack')
        elif cmd == 'r':
            print('runaway')
        elif cmd == 'l':
            print('look around')
        else:
            print('ok, exiting game ... bye')
            break


if __name__ == '__main__':  # only run the main method if it is being called from the program (i.e. not as a package)
    main()
