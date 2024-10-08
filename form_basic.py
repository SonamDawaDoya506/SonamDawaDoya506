from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config["SECERET_KEY"] = "mysecretkey"

class InfoForm(FlaskForm):

    breed = StringField("What breed are you?")
    submit = SubmitField("submit")

@app.route("/", methods = ["GET","POST"])
def index():
    breed = False
    form = InfoForm()

    if form.validate_on_submit():

        breed = form.breed.data
        form.breed.data = " "
    return render_template("index1.html", breed = breed, form = form )

if __name__ == "__main__":
    app.run(debug = True)
