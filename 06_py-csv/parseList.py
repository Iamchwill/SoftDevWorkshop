# Cashew (Shriya Anand, Emma Buller, William Chen)
# SoftDev
# K<06> -- <Stl/O: Divine your Destiny! (Parsing through files)
# <2021>-<09>-<29>

# We planned in class using Shryia's code as a base
# and then moved to split the file into each key and value and then add it a dictionary.
# Afterwards the probablity would be the percentage of the previous value + it's own.
# I found random.choice() and talked about it.

# V2
# We realized we used the wrong text. Copy and pasted from Raw this time.
# We used csv.Reader this time since the regular reader seperates commas even in quotes

#imports
import random
import csv

import random
def selectJob():
    dictionary ={}
    with open('occ_per.csv', newline='') as csvfile:
         reader = csv.DictReader(csvfile)
         for row in reader:
             if (row['Job Class']!= 'Total' and row['Job Class']!= 'Job Class'):
                 dictionary[row['Job Class']] = float(row['Percentage'])
    job = random.choices(list(dictionary.keys()),list(dictionary.values()), k = 1)
    return job[0]
