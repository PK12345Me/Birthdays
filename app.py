import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

CELEBRANTS={}
MONTH = ["January","February","March", "April", "May", "June","July","August","September","October","November", "December"]
DAY=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # TODO: Add the user's entry into the database
        name=request.form.get("name")
        if not name:
            return redirect("/")
        month=request.form.get("month")
        if not month:
            return redirect("/")
        day=request.form.get("day")
        if not day:
            return redirect("/")

        CELEBRANTS[name] = {'month': month, 'day': day}
        # Insert data into database
        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)

        return redirect("/")
    else:
        # TODO: Display the entries in the database on index.html
        return render_template("index.html", celebrants = CELEBRANTS, day = DAY, month = MONTH)
    # remember celebrant



