from flask import Flask, render_template
from forms import TeamForm

app = Flask(__name__)

app.secret_key = "keep this secret"

@app.route("/")
def home():
    team_form = TeamForm()

    return render_template("home.html", team_form = team_form)

@app.route("/add-team", methods=["POST"])
def add_team():
    team_form = TeamForm()

if __name__ == "__main__":
    app.run(debug = True)