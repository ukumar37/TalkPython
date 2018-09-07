# import actors
import random
import time

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
        #SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        #SmallAnimal('Bat', 3),
        #Dragon('Dragon', 50),
        Wizard('Evil Wizard', 250)
    ]

    # print(creatures)  # we can do this because we created the __repr__ method in class Creatures

    hero = Wizard('Gandolf', 75)  # Instantiate our hero

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and foggy forest ...'
              .format(active_creature.name, active_creature.level))
        print('')

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around?')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('The wizard runs and hides taking time to recover ...')
                time.sleep(5)
                print('The wizard returns revitalized!')
        elif cmd == 'r':
            print('The wizard has become unsure of his power and flees!')
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees:'.format(hero.name))
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        else:
            print('ok, exiting game ... bye')
            break


        if not creatures:
            print('You defeated all the creatures, well done!!')
            break

        print("")


if __name__ == '__main__':  # only run the main method if it is being called from the program (i.e. not as a package)
    main()
