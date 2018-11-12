from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def userHome():
    user = request.form["username"]
    password = request.form["password"]
    print("User logged in with: " + user + ", " + password)
    return "Good luck with your webserver!"

app.run()