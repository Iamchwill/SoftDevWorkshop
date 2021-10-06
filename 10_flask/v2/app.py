# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.run()

#Our prediction is that "about to print __name__... __main" will be printed in the same line in the terminal after you open the link. The link should take you to a webpage that says "No hablo queso"
#Post test: It prints it in 2 lines (not 1)
