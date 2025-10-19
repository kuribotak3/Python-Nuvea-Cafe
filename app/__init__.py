from flask import Flask
from app.routes import register_routes
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()

    app = Flask(__name__)

    # Ambil dari environment
    # app.config['DATABASE_HOSTNAME'] = os.getenv('DATABASE_HOSTNAME')

    # register blueprint (semua rute dimasukkan)
    register_routes(app)

    return app
