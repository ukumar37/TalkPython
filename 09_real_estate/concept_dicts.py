

# Below are multiple ways to create dictionaries
import collections

lookup = {}
lookup = dict()
lookup = {'age': 42, 'loc': 'Italy'}
lookup = dict(age=42, loc='Italy')


class Wizard:
    def __init__(self, name, level):
        self.level = level
        self.name = name


gandolf = Wizard("Gandolf", 42)
print(gandolf.__dict__)
print(gandolf.level)
print(gandolf.name)


# How to reference an index item?
print(lookup)
print(lookup['loc'])


# How to add a new key-value pair to an existing dictionary?
lookup['cat'] = 'Fun code demos'

if 'cat' in lookup:
    print(lookup['cat'])


# Suppose there came from a data source like a database, web service, etc.
# and we want to randomly access them

User = collections.namedtuple('User', 'id, name, email')
users = [
    User(1, 'User1', 'user1@talkpython.fm'),
    User(2, 'User2', 'user2@talkpython.fm'),
    User(3, 'User3', 'user3@talkpython.fm'),
    User(4, 'User4', 'user14@talkpython.fm')
]

lookup = dict()
for u in users:
    lookup[u.id] = u

print(lookup[3])