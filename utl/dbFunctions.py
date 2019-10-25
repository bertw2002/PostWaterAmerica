# PWA- chenB, chinK, chowdhuryB, wanA
# SoftDev1 pd9
# This file contains all the functions for the databases

from sqlite3 import connect, Row

#creates the tables users and topics
def create():
    # Setup the database
    DB_FILE = "blogs.db"
    db = connect(DB_FILE)
    db.row_factory = Row
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS users(username TEXT, displayName TEXT,password TEXT)"
    b = "CREATE TABLE IF NOT EXISTS topics(blogNumber INT, blogTopic TEXT, entry TEXT, creator TEXT)"
    c.execute(q)
    c.execute(b)
    db.commit()
    db.close()

def addUser(username,displayName,password):
    DB_FILE = "blogs.db"
    db = connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO users VALUES (?, ?, ?)", (str(username), str(displayName), str(password)))
    db.commit()
    db.close()

def addBlog(blogNumber, blogTopic, entry, creator):
    DB_FILE = "blogs.db"
    db = connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO users VALUES (?, ?, ?,?)", (str(blogNumber), str(blogTopic), str(entry), str(creator)))
    db.commit()
    db.close()

def verifyUser(username, password):
    DB_FILE = "blogs.db"
    db = connect(DB_FILE)
    c = db.cursor()

    if checkUsername(username):
        cur = c.execute("SELECT password FROM users WHERE username = ?", (str(username),))
        userPassword = cur.fetchall()
        for row in userPassword:
            if password in row:
                return True
            else:
                return False
    else:
         return False

    db.commit()
    db.close()

def checkUsername(username):
    DB_FILE = "blogs.db"
    db = connect(DB_FILE)
    c = db.cursor()
    cur = c.execute("SELECT username FROM users")
    usernames = cur.fetchall()
    for row in usernames:
        if username in row:
            return True
    db.commit()
    db.close()
create()
# check()
# addUser("test","asdfd","password")
# print(verifyUser("test","password"))
# print(verifyUser("test","asdf"))
# print(verifyUser("asdf","asdf"))
