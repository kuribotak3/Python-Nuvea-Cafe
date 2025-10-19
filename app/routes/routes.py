from flask import Blueprint, render_template

menu = Blueprint('menu', __name__)

# @menu.route('/')
# def menu_home():
#     return render_template('index.html')

@menu.route('/about-us')
def menu_about():
    return render_template('about.html')
