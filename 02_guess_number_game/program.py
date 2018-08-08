import random

print('---------------------------')
print('  Guess that Number Game')
print('---------------------------')
print()

the_number = random.randint(0, 100)

guess = -1

name = input('Player what is your name?: ')


while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)
    if guess < the_number:
        print('Sorry {}, your guess of {} is too low'.format(name, guess))
    elif guess > the_number:
        print('Sorry {}, your guess of {} is too high'.format(name, guess))
    else:
        print('Excellent work {}. You won ${}!'.format(name, guess))

print('done')