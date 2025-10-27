from flask import Blueprint, render_template

menu = Blueprint('menu', __name__)

@menu.route('/about-us')
def about():
    return render_template('about/index.html')

@menu.route('/catalog-menu')
def catalog():
    return render_template('catalog/index.html')

@menu.route("/login")
def login():
    return render_template("login/index.html")

@menu.route("/register")
def register():
    return render_template("register/index.html")