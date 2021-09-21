## lists of names
pd1 = ['Emma', 'Shriya', 'William', 'Aaron', 'Shyne']
pd2 = ['studentA', 'studentB', 'studentC', 'studentD']

import random

def printName():
    period = int(input('Pick a period (Input 1 or 2): '))
    if period == 1:
        print(pd1[random.randint(0,len(pd1) - 1)])
    if period == 2:
        print(pd2[random.randint(0,len(pd2) - 1)])
