import random


class Wizard:
    def __init__(self, name, level):  # initialize the class
        self.name = name  # once instantiated, give the object a name
        self.level = level  # once instantiated, give the object a level


    def attack(self, creature):
        print("The wizard {} attacks {}".format(self.name, creature.name))

        my_roll = random.randint(1, 12) * self.level
        creature_roll = random.randint(1, 12) * creature.level

        print("You roll {} ...".format(my_roll))
        print("{} rolls {} ...".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("The wizard has handily triumphed over {}".format(creature.name))
            return True
        else:
            print("The wizard has been DEFEATED!!!!")
            return False



class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):  # output the value of an instance of an object by using a print statement
        return "Creature {} of level {}".format(
            self.name, self.level
        )