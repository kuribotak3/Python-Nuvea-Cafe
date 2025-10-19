from .routes import menu

def register_routes(app):
    app.register_blueprint(menu)