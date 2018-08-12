def main():
    print_header()
    run_event_loop()


def print_header():
    print('-------------------------')
    print('      Journal App')
    print('-------------------------')
    print()


def run_event_loop():

    print('What do you want to do with your journal?')

    cmd = None

    while cmd != 'X':

        cmd = input('[L]ist entries, [A]dd an entry, E[X]it: ')

        if cmd.lower().strip() == 'l':
            print('L')
        elif cmd.lower().strip() == 'a':
            print('A')
        elif cmd.lower().strip() != 'x':
            print("Sorry. We don't understand '{}'.".format(cmd))

    print('Done. Goodbye!')

main()

