from app import create_app
from flask import render_template
from flask_bootstrap import Bootstrap5

app = create_app()
bootstrap = Bootstrap5(app)   

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)