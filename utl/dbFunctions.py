# PWA- chenB, chinK, chowdhuryB, wanA
# SoftDev1 pd9
# This file contains all the functions for the databases

from sqlite3 import connect, Row

#global varible to hold next blog Number for the next new topic created

#creates the tables users and topics
def create():
    # Setup the database
    DB_FILE = "blogs.db"
    db = connect(DB_FILE)
    db.row_factory = Row
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS users(username TEXT, displayName TEXT,password TEXT)"
    b = "CREATE TABLE IF NOT EXISTS blogs(blogNumber INT, blogName TEXT, entry TEXT, creator TEXT)"
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

def addBlog(blogTopic, entry, creator):
    DB_FILE = "blogs.db"
    db = connect(DB_FILE)
    c = db.cursor()
    cur = c.execute("SELECT MAX(blogNumber) FROM blogs")
    allBlogNumbers = cur.fetchall()
    blogNumber = 0;
    for blognum in allBlogNumbers:
        if (len(allBlogNumbers) != 0):
            blogNumber = blognum[0] + 1
    c.execute("INSERT INTO blogs VALUES (?, ?, ?,?)", (int(blogNumber), str(blogTopic), str(entry), str(creator)))
    db.commit()
    db.close()

def checkUser(username, password):
    DB_FILE = "blogs.db"
    db = connect(DB_FILE)
    c = db.cursor()

    if checkUsername(username):
        cur = c.execute("SELECT password FROM users WHERE username = ?", (str(username),))
        userPassword = cur.fetchall()
        db.commit()
        db.close()
        for row in userPassword:
            if password in row:
                return True
            else:
                return False
    else:
         return False



def noRepeatBlogs(username,blogName):
    DB_FILE = "blogs.db"
    db = connect(DB_FILE)
    c = db.cursor()
    cur = c.execute("SELECT blogName FROM blogs WHERE creator = ?",(str(username),))
    yourBlogs = cur.fetchall()
    db.commit()
    db.close()  
    for blog in yourBlogs:
        if blogName == blog:
            return False
    return True

def checkUsername(username):
    DB_FILE = "blogs.db"
    db = connect(DB_FILE)
    c = db.cursor()
    cur = c.execute("SELECT username FROM users")
    usernames = cur.fetchall()
    db.commit()
    db.close()
    for row in usernames:
        if username in row:
            return True
    return False


def showEntries(blognumber):
    DB_FILE = "blogs.db"
    db = connect(DB_FILE)
    c = db.cursor()
    cur = c.execute("SELECT entry FROM blogs WHERE blogNumber = ?",(int(blognumber),))
    allEntries = cur.fetchall()
    db.commit()
    db.close()
    entries = []
<<<<<<< HEAD
=======
    allEntries = cur.fetchall()

>>>>>>> 08dcbc6a8652be97cf952e439b7779346274413f
    for entry in allEntries:
        entries.append(entry)
    return entries

def getBlogNumber(username,blogtitle):
    DB_FILE = "blogs.db"
    db = connect(DB_FILE)
    c = db.cursor()
    cur = c.execute("SELECT blogNumber FROM blogs WHERE blogName = ? AND creator = ?",(str(blogtitle),str(username)))
    num = cur.fetchall()
    db.commit()
    db.close()
    print(num)
    return num[0][0]

def yourBlogs(username):
    DB_FILE = "blogs.db"
    db = connect(DB_FILE)
    c = db.cursor()
    cur = c.execute("SELECT blogName FROM blogs WHERE creator = ?",(str(username),))
    yourBlogs =[]
    yourBlogS = cur.fetchall()
    db.commit()
    db.close()
    print(yourBlogS)
    for blog in yourBlogS:
        print(blog[0])
        yourBlogs.append(blog[0])
    return yourBlogs

def createOtherBlogList(user):
    DB_FILE = "blogs.db"
    db = connect(DB_FILE)
    c = db.cursor()
    cur = c.execute("SELECT blogNumber,blogName FROM blogs WHERE creator != ?;", [str(user)])
    allBlogsButUser = cur.fetchall()
    return allBlogsButUser

def get(ID, topic):
    DB_FILE = "blogs.db"
    db = connect(DB_FILE)
    c = db.cursor()
    cur = c.execute("SELECT * FROM blogs WHERE blogNumber == ? and blogName == ?;", [str(ID), str(topic)])
    info = cur.fetchone()
    return info

create()
# check()
# addUser("test","asdfd","password")
# print(verifyUser("test","password"))
# print(verifyUser("test","asdf"))
# print(verifyUser("asdf","asdf"))
