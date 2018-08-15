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
    journal_data = []  # list()

    while cmd != 'x':

        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x':
            print("Sorry. We don't understand '{}'.".format(cmd))

    print('Done. Goodbye!')


def list_entries(data):
    print("Your journal entries are:")
    entries = reversed(data) # reverse the list order
    for idx, entry in enumerate(entries): # enumerated command adds indexes to the list, resulting in something calles "tuples"
        print('* ({}) {}'.format(idx + 1, entry))


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    data.append(text)


main()
