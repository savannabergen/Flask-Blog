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
