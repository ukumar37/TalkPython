# import actors
import random

from actors import Wizard, Creature

def main():
    print_header()

    game_loop()


def print_header():
    print('---------------------------')
    print('       WIZARD BATTLE')
    print('---------------------------')


def game_loop():

    creatures = [  # Instantiate our creatures
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000)
    ]

    # print(creatures)

    hero = Wizard('Gandolf', 75)  # Instantiate our hero

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and foggy forest ...'
              .format(active_creature.name, active_creature.level))
        print('')

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around?')
        if cmd == 'a':
            hero.attack(active_creature)
            # print('attack')
        elif cmd == 'r':
            print('runaway')
        elif cmd == 'l':
            print('look around')
        else:
            print('ok, exiting game ... bye')
            break


if __name__ == '__main__':  # only run the main method if it is being called from the program (i.e. not as a package)
    main()
