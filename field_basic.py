from flask import Flask, render_template,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import (StringField,BooleanField,DateTimeField,
                    RadioField,SelectField,TextField,
                    TextAreaField,SubmitField)

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config["SECRET_KEY"] = "mykey"

class InfoForm(FlaskForm):
    breed = StringField("What breed are you?",validators = [DataRequired()])
    neutered = BooleanField("Have you been neutered?")
    mood = RadioField("Please choose mood: ",
                        choices = [("mood_one","Happy"),("mood_two","Excited")])
    food_choice = SelectField(u"Pick your favourite food: ",
                                choices = [("chi","Chicken"),("bf","Beef"),
                                            ("fish","Fish")])
    feedback = TextAreaField()
    submit = SubmitField("Submit")


@app.route("/", methods = ["GET","POST"])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session["breed"] = form.breed.data
        session["neutered"] = form.neutered.data
        session["mood"] = form.mood.data
        session["food"] = form.food_choice.data
        session["feedback"] = form.feedback.data

        return redirect(url_for("thank_you"))
    return render_template("field_index.html",form = form)

    @app.route("/thank_you")
    def thank_you():
        return render_template("thank_you.html")

if __name__ == "__mian__":
    app.run(debug = True)
