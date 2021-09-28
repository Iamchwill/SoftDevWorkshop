## William Chen
## SoftDev
## K<05> -- Alagamate Code With New Trios!
## <2021>-<09>-<28>

# SUMMARY OF TRIO DISCUSSION
# We all have to make the list into a dictionary
# How do we get the list from the dictonary?
# We can use .get()
# Why isn't .get() working?
# Oh it's the pd1 in len()
# We need to set up member's submodule now.
# The bell rang. Email to continue comunication

# DISCOVERIES
# .get(key) gets the value from the dictionary
# Changing code requires rigorous bug checks
# Rayat used the wrong link for the submodule
# git link is not used for submodules in the workshop repo

# QUESTIONS
# Is there a specific reason for using a dictionary?
# Is it better than two lists?
# Why is the git link not used for submodules?
# Does it cause problems?
#

# COMMENTS
# 

## lists of names
Names = {
    'pd1': ['Emma', 'Shriya', 'William', 'Aaron', 'Shyne'],
    'pd2': ['studentA', 'studentB', 'studentC', 'studentD']
}

import random

# Making printName 
def printName():
    # User picks which class
    period = input('Pick a period (Input 1 or 2) Or select 3 for a name from either: ')
    if period == '1':
        print(Names.get('pd1')[random.randint(0,len(Names.get('pd1')) - 1)])
    elif period == '2':
        print(Names.get('pd2')[random.randint(0,len(Names.get('pd2')) - 1)])
    elif period == '3':
        total = Names.get('pd1') + Names.get('pd2')
        print(total[random.randint(0, len(total) - 1)])
    #If not an option than tell user and restarts until they pick an option
    else:
        print('NOT AN OPTION')
        printName()
