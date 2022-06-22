#store stuff the user can go/navigate to 
from flask import Blueprint, render_template

#This file is considered the blueprint to our application 
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")
    