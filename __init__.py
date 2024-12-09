from flask import Flask, render_template
from database import init_db

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")


if __name__ == "__main__":
    init_db(app)
    app.run(debug = True)