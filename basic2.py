from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    name = "Sonam"   #just creating variable(containers)
    letters = list(name) #for sclicing
    pup_dict = {"pup_name": "Pussy"}  #creating dictionary

    # sending the variables to html 
    return render_template("basic1.html", name = name, letters = letters,
                            pup_dict = pup_dict)

if __name__ == "__main__":
    app.run(debug=True)
