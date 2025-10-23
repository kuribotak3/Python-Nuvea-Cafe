from flask import Blueprint, render_template

menu = Blueprint('menu', __name__)

@menu.route('/about-us')
def about():
    return render_template('about/index.html')
