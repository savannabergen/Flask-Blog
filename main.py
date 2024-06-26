from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__)

# Create a Route Decorator
@app.route('/')

def index():
    first_name = "John"
    stuff = "This is <b>Bold</b>"
    favourite_pizza = ["pepperoni", "cheese", "42"]
    return render_template("index.html", first_name=first_name, stuff=stuff, 
                           favourite_pizza=favourite_pizza)

@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)

# Create Custom Error Page

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500