from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    my_list = [1,2,3,4,5,6,6]
    puppies = ["Huki","Bulki","Zaki"]
    user_logged_in = True
    user_logged_in1 = False
    return render_template("basic2.html",my_list = my_list,
                          puppies = puppies, user_logged_in = user_logged_in,
                          user_logged_in1 = user_logged_in1)

if __name__ == "__main__":
    app.run(debug=True)
