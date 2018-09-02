
class Wizard:
    def __init__(self, name, level):  # initialize the class
        self.name = name  # once instantiated, give the object a name
        self.level = level  # once instantiated, give the object a level


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):  # output the value of an instance of an object by using a print statement
        return "Creature {} of level {}".format(
            self.name, self.level
        )