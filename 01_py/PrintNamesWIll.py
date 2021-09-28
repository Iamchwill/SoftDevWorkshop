## William Chen
## SoftDev
## K<00> -- Print Class Names With Trio And No Teacher! (Limited Directions,
## so we made our own decisions)
## <2021>-<09>-<21>

## lists of names
pd1 = ['Emma', 'Shriya', 'William', 'Aaron', 'Shyne']
pd2 = ['studentA', 'studentB', 'studentC', 'studentD']

import random

def printName():
    period = input('Pick a period (Input 1 or 2): ')
    if period == '1':
        print(pd1[random.randint(0,len(pd1) - 1)])
    elif period == '2':
        print(pd2[random.randint(0,len(pd2) - 1)])
    else:
        print('NOT AN OPTION')
        printName()
