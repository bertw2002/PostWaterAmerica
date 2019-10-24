# Team Krispy Kreme - Kenneth Chin and Kazi Jamal
# SoftDev1 pd9
# K15 -- Do I Know You?
# 2019-10-04

from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
import os
import sqlite3

app = Flask(__name__)
#
# DB_FILE="blog.db"
# db = sqlite3.connect(DB_FILE)
# dbcursor = db.cursor()
#
# #Create table
# dbcursor.execute("DROP TABLE IF EXISTS login")
# loginCreateTable = "CREATE TABLE login (username TEXT, password TEXT, displayName TEXT);"
# dbcursor.execute(loginCreateTable)
# dbcursor.execute("INSERT INTO login VALUES (?, ?, ?);", ["admin123", "password123", "admin"]) #test login
#
# dbcursor.execute("DROP TABLE IF EXISTS blog")
# blogCreateTable = "CREATE TABLE blog (displayName TEXT, blog TEXT);"
# dbcursor.execute(blogCreateTable)

# creates secret key for session
app.secret_key = os.urandom(32)

# hardcodes a single username/password combination
testuser = "krispykreme"
testpass = "12345678"

# redirects to login page if no user logged in
# redirects to welcome page if user logged in
@app.route("/")
def root():
    if "username" in session:
        return redirect(url_for('welcome'))
    return render_template('homepage.html')

# has logout button to log out
@app.route("/welcome")
def welcome():
    if "username" not in session:
        return redirect(url_for('root'))
    return render_template("welcome.html")

# has logout button to log out
@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

# login page with form which sends request to /auth route
@app.route("/login")
def login():
    return render_template("login.html")

# handles login request
@app.route("/auth", methods=["POST"])
def auth():
    if request.form['username'] == testuser:
        # if correct username/password combination, add username to session and redirect to welcome route
        if request.form['password'] == testpass:
            session['username'] = request.form['username']
            return redirect(url_for('welcome'))
        # if invalid password return error
        else:
            print("invalid password")
            return error("Invalid Password")
    # if invalid username return error
    else:
        print("invalid username")
        return error("Invalid Username")


# returns a page with provided error message
def error(message):
    return render_template("error.html", error=message)

# removes session data for username
@app.route("/logout")
def logout():
    session.pop('username')
    return redirect(url_for('root'))

# removes session data for username
@app.route("/createAccount")
def createAccount():
    return render_template("createAccount.html")


if __name__ == "__main__":
    app.debug = True
    app.run()
