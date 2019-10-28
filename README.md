# BlogHub by PostWaterAmerica

## Roster:

- Brandon Chen (Templates manager)

- Kenneth Chin (Database manager)

- Biraj Chowdhury (Python creator)

- Albert Wan (Project manager)

## Requirements To Run the Project

- You will need python3 and flask in your virtual envrionment
- After installing python3, you can install flask by running the command `pip3 install flask`

## Run the Project
- First, you will need to clone the repository. You can do this by going into terminal and typing `git clone git@github.com:bertw2002/PostWaterAmerica.git`
- Then, cd into the cloned repository and execute `python3 app.py` Now you're set!


## Navigating the webpage
- You will need to create an account in order to post blogs.
- Once you create an account, you can creat your own blogs and view other people's blogs.

## Modules and Libraries
```
-from flask import Flask
-from flask import render_template
-from flask import request
-from flask import session
-from flask import redirect
-from flask import url_for
```

-Flask
http://flask.palletsprojects.com/en/1.1.x/
We used this to create a website hosted by a local server and is the main component of the project. It uses different routes to navigate around.

-Render_template
http://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
This is necessary to display the written HTML file which is how the website page will look like. Each route in the python file uses render_template to pass any necessary variables for use and display in the HTML file.

-Request
http://flask.palletsprojects.com/en/1.1.x/quickstart/#accessing-request-data
Request is used to transfer data from the HTML file back to python. Once a user fills out a form, request is necessary in order to interact with the input in the python file. It is used for creating an account and entry.

-Session
https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions
This stores information about the current user from one request to another. The main use of this in our project is to identify the current logged in user. This way, we can enable the user to create a blog under their name and be able to edit their previously created blog.

-Redirect
https://flask.palletsprojects.com/en/1.1.x/quickstart/#redirects-and-errors
This is used in a route to redirect the user to another endpoint. We used this as a way to edit the user's blog. After the user submits the form, a route updates the table with the new information and then redirects to the general blog page.

-Url_for
https://flask.palletsprojects.com/en/1.1.x/quickstart/#url-building
Url_for builds a url with the name of the function as the first argument and any variables after. We used this in our HTML file to construct a url directing to a proper route and function. It transfers data from the HTML to the python file without using request.form and any input by the user.
