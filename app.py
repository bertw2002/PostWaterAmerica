# PWA- chenB, chinK, chowdhuryB, wanA
# SoftDev1 pd9


from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
import os
import sqlite3

#imports functions from dbfunctions.py
from utl.dbFunctions import create, addUser, checkUsername, checkUser, getBlogNumber,showEntries, yourBlogs, noRepeatBlogs, addBlog, createOtherBlogList, get, update, getDisplayname,checkDisplayname,getUsername


app = Flask(__name__)
create()

# creates secret key for session
app.secret_key = os.urandom(32)

currentUser = ""

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
    username = session.get('username')
    blogs = yourBlogs(username)
    print(blogs)
    return render_template("welcome.html",yourBlogs = blogs)

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
    if checkUsername(request.form['username']):
        # if correct username/password combination, add username to session and redirect to welcome route
        if checkUser(request.form['username'], request.form['password']):
            session['username'] = request.form['username']
            currentUser = request.form['username']
            return redirect(url_for('welcome'))
        # if invalid password return error
        else:
            print("invalid password")
            return error("Invalid Password")
    # if invalid username return error
    else:
        print("INVALID username")
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

# To view other people's blogs
@app.route("/otherBlog")
def otherBlog():
    #create dictionary to transfer data to html
    #create dictionary to transfer data to html
    blogDict = {}
    for row in createOtherBlogList(currentUser):
        blogDict[row[0]] = row[1]
    return render_template("otherBlog.html", allBlogs = blogDict)

#View Blogs that match your search
@app.route("/blogsYouSearched")
def searchedBlogs():
    yourSearch= request.args['yourSearch']
    return


@app.route("/checkCreate")
def checkCreate():
    if checkDisplayname(request.args['displayName']):
            return render_template("createAccount.html", userError = "***That display name is already in use, try a different one")
    if checkUsername(request.args['username']):
            return render_template("createAccount.html", userError = "***That username is already in use, try a different one")
#confirms password, allowing user to not make mistakes while putting in password
    if (request.args['password'] == request.args['confirmPassword']):
        addUser(request.args['username'],request.args['displayName'],request.args['password'])

        session['username'] = request.args['username']
        currentUser = request.args['username']
        #goes back to login.html
        return render_template("login.html")
    else:
        #if passwords don't match, go back to createaccount.html
        return render_template("createAccount.html", userError = "***Passwords don't match")

# To create a topic
@app.route("/createTopic")
def createTopic():
    print(session)
    return render_template("createTopic.html")

#View one of your blogs
@app.route("/yourBlog",methods=["POST","GET"])
def yourBlog():
    print(request.form)
    print(session)
    #stores username and password using session function
    username = session.get('username')
    blogName = request.form.get('blogName')
    if noRepeatBlogs(username,blogName):
        #forms entry. People can add entries too.
        if 'newEntry' in request.form.keys():
            entry = request.form['newEntry']
            addBlog(blogName,entry,username)
    else :
        return redirect(url_for('createTopic'))
    blogNum = getBlogNumber(username,blogName)
    entries = showEntries(blogNum)
    return render_template("yourBlog.html",topic = blogName,topicEntries = entries)

@app.route("/<blogID>/<blogTopic>")
def displayEntry(blogID, blogTopic):
    #displays entry with ability to edit their own blogs, not others. They can add entries to their own blogs.
    info = get(blogID,blogTopic)
    print(info)
    c = getDisplayname(info[3])
    t = info[1]
    e = info[2]
    i = info[0]
    if session['username'] == info[3]:
        access = True
    else:
        access = False
    #goes to otheruserblog.html to allow these changes.
    return render_template("otherUserBlog.html", creator = str(c), topic = str(t), entry = str(e), yes = access, id = i)

@app.route("/editBlog/<blogID>/<blogTopic>")
#edit function that allows user to edit.
def edit(blogID, blogTopic):
    info = get(blogID, blogTopic)
    print(info[2])
    return render_template("editBlog.html", topic = info[1], ID = blogID, oldEntry = str(info[2]))

@app.route("/editBlog2/<blogID>/<blogTopic>",methods=["POST","GET"])
#edit2 comes into play when user actually submits edit entry form, redirecting to blog page.
def edit2(blogID, blogTopic):
    entry = request.form['newEntry']
    update(blogID,blogTopic,entry)
    return redirect("/otherBlog")

if __name__ == "__main__":
    app.debug = True
    app.run()
