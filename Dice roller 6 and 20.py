import random

while True:
    roller1 = input('Press 1 to roll dices on 6\n'
                    'Press 2 to roll dices on 20\n'
                    'Choose it: ')

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,20)

    choice1 = '1'
    choice2 = '2'

    if (roller1 == choice1):
        print('Your result is : {}'.format(dice1))
        print('\n')

    elif (roller1 == choice2):
        print('Your result is: {}'.format(dice2))
        print('\n')



