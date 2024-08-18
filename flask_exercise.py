from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/') #127.0.0.1:5000
def index():
    return "<h1>Welcome to /Puppy_name/name world<h!>"

@app.route('/puppy_name/<name>') #127.0.0.1:5000/puppy_latin
def puppylatin(name):
    pname = " "
    if name[-1] == "y":
        pname = name[:-1] + "iful"
    else:
        pname = name + "y"
    return "<h1>Hi your Puppy latin name is: {}".format(pname)

if __name__ == '__main__':
    app.run()
