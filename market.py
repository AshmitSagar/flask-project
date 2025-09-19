from flask import Flask

app = Flask(__name__)


# root page
@app.route("/")
def hello_world():
    return "<h1>Hello World</h1>"


"""
# static about page
@app.route("/about")
def about_page():
    return "<h1>About Page</h1>"
"""


# Dynamic routes
@app.route("/about/<username>")
def about_page(username):
    return f"<h1>This is the about page of {username}</h1>"
