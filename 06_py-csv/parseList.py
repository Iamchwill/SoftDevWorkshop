# Cashew (Shriya Anand, Emma Buller, William Chen)
# SoftDev
# K<06> -- <Stl/O: Divine your Destiny! (Parsing through files)
# <2021>-<09>-<29>

# We planned in class using Shryia's code as a base
# and then moved to split the file into each key and value and then add it a dictionary.
# Afterwards the probablity would be the percentage of the previous value + it's own.
# I found random.choice() and talked about it.

import random

def selectDestiny():
    #read the file and split at new line
    file = open("occ_per.csv","r")
    data = file.read()
    dataList = data.split("\n")
    
    #put files into list
    destinies = {}
    #First line is title, last 2 are Total and empty
    for x in range(1,len(dataList) - 2):
        item = dataList[x].split("\t")
        destinies[item[0]] = float(item[1])

    jobs = list(destinies.keys())
    percentages = list(destinies.values())
    #choices() chooses k of the jobs randomly based on weighted list.
    job = random.choices(jobs, percentages, k = 1);
    return job[0]
