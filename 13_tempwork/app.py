#AWEsome: Ella Krechmer, Aaron Contreras, William Chen
#SoftDev
#K13 -- Template for Success
#10-08-21

# Import Flask so app will work
from flask import Flask, render_template
app = Flask(__name__)

# Import the things needed for occupation-chooser to work
import random
import csv

# Occupation-chooser code here
# Dictionary is now for all to see!
dictionary ={}
with open('data/occupations.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #Excludes the last row since it isn't an occupation"
        if (row['Job Class']!= 'Total' and row['Job Class']!= 'Job Class'):
            dictionary[row['Job Class']] = float(row['Percentage'])

#Uses random.choices to pick the random job
def select_Job():
    job = random.choices(list(dictionary.keys()),list(dictionary.values()), k = 1)
    return "Here's the random one: " + job[0]

#What shall be shown
@app.route("/occupyflaskst")
def HEY_WORLD():
    return render_template('tablified.html', title = "occupations", collection = dictionary, job = select_Job())

#RUN
app.debug=True
app.run()
