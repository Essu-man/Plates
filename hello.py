from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/Dashboard")
def login():
    return render_template("Dashboard")

if __name__ == "__main__":
    app.run(debug=True)
