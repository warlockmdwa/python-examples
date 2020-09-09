#Super Villain name generator

import random

def nameGen():
    firstNames = ['Doctor', 'Funny', 'Atomic', 'Sneaky','Chaotic',
                  'Mind','Psionic','Maniacal','Giant','Mad','Cyber','Racist']

    surNames = ['Cannibal', 'Destroyer', 'Man','Heretic',
                'Diablo','Lawless','Pyromancer','Slime','Cat','Nosferatu','Witch']

    return 'Your Super Villain name is : {} {}!'.format(random.choice(firstNames), random.choice(surNames))

for i in range(3):
    print(nameGen())
