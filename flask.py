from flask import Flask, render_template, flask, session, redirect, url_for
from flask_wtf import FlaskForm

app.config[" SECRET_KEY"] = "kmykey"

class SimplForm(FlaskForm):
    submit = SubmitField("Click Me")

@app.route("/",methods = ["GET","POST"])
def index():
    form = SimpleForm()

    if form.validator_on_submit():
        flask("You just clicked the button!")

        return redirect(url_for("index"))
    return render_template("flask.html", form = form)
