# Jun Tao Lei & Kenneth Chin
# SoftDev1 pd9
# K#17 - No Trouble
# 2019-10-07

from sqlite3 import connect, Row
# from csvrw import insertAll, printTable

# Setup the database
DB_FILE = "blogs.db"

db = connect(DB_FILE)
db.row_factory = Row
c = db.cursor()

def create():
    # Setup the database
    DB_FILE = "blogs.db"
    db = connect(DB_FILE)
    db.row_factory = Row
    c = db.cursor()
    q = "CREATE TABLE IF NOT EXISTS users(username TEXT, displayName TEXT,password INT)"
    b = "CREATE TABLE IF NOT EXISTS topics(blogNumber INT, blogTopic TEXT, creator TEXT)"
    c.execute(q)
    c.execute(b)
    db.commit()
    db.close()

def addUser(username, displayName, password):
    DB_FILE = "blogs.db"
    db = connect(DB_FILE)
    db.row_factory = Row
    c = db.cursor()
    q = "INSERT INTO users(username, displayName,password) VALUES(" +  username + "," + displayName + "," + password + ")"
    c.execute(q)
    db.commit()
    db.close()

  # tbl_headers = " (" + ",".join("{0} BLOB".format(header) for header in headers) + ")"
  # db.execute("CREATE TABLE IF NOT EXISTS " + tbl_name + tbl_headers)

# # Add the csv and create a table to store the csv if it does not exist
# insertAll("data/courses.csv", "courses", db)
# insertAll("data/students.csv", "students", db)
#
# # Print the database
# print("courses table")
# printTable("courses", c)
# print("\nstudents table")
# printTable("students", c)
# q = """SELECT name, students.id, mark
# FROM students, courses
# WHERE students.id = courses.id;"""

# q = "CREATE TABLE IF NOT EXISTS users(password INT,username TEXT, displayName TEXT)"
# b =   "CREATE TABLE IF NOT EXISTS topics(blogTopic TEXT, creator TEXT, blogNumber INT)"
# c.execute(q)
# c.execute(b)
# Save and exit the database
db.commit()
db.close()
