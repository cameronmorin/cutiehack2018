from flask import Flask
from flask import render_template

bot = Flask(__name__)

@bot.route("/")
def index():
    return render_template("index.html", name ="Cam")

bot.run()