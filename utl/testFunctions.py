from csv import DictReader
from re import search
from dbFunctions import addUser

# Creates a table if it does not exist
def create(tbl_name, headers, db):
  tbl_headers = " (" + ",".join("{0} BLOB".format(header) for header in headers) + ")"
  db.execute("CREATE TABLE IF NOT EXISTS " + tbl_name + tbl_headers)

# Add all entries from csv into a table
def insertAll(file, tbl_name, db):
  f = DictReader(open(file))
  create(tbl_name, f.fieldnames, db)
  for row in f:
    insert(row.values(), tbl_name, db)

# Insert one row into a table
def insert(values, tbl_name, db):
  field = " VALUES("
  for value in values:
    if bool(search("^[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)$", value)):
      field += value + ","
    else: field += '"{0}"'.format(value) + ","
  db.execute("INSERT INTO " + tbl_name + field[:-1] + ")")

# print the value of a table
def printTable(tbl_name, cur):
  cur.execute("SELECT * FROM " + tbl_name)
  for row in cur.fetchall():
    print(dict(row))

addUser('JDoe' , 'JaneDoe', '1234')
#
# def grades(name):
