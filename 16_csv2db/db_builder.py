"""
Waahoos: Alejandro Alonso, Ivan Mijacika, William Chen
SoftDev
K16 -- All About Database -- Sqlite3
2021-10-25
"""

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#=========================================================

def input_database(table, file):
    with open(file, 'r') as csvfile:
        data = csv.DictReader(csvfile)
        command = "CREATE TABLE " + table + " ("
        for column in data.fieldnames:
            command += column
            if data.fieldnames[len(data.fieldnames) - 1] != column:
                command += ", "
        command += ")"
        #print(command)
        c.execute(command)
        for row in data:
            values = ""
            for column in data.fieldnames:
                if data.fieldnames[0] == column:
                    values += '"'
                values += row[column]
                if data.fieldnames[0] == column:
                    values += '"'
                if data.fieldnames[len(data.fieldnames) - 1] != column:
                    values += ", "
            #print(values)
            c.execute('INSERT INTO ' + table + ' VALUES (' + values + ')')

input_database("courses", "courses.csv")
input_database("students", "students.csv")


#command = ""          # test SQL stmt in sqlite3 shell, save as string
#c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
