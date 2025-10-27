from flask import Flask
from app.routes import register_routes
from dotenv import load_dotenv
from app.config.database import db_manager

import os
import atexit


def create_app():
    load_dotenv()

    app = Flask(__name__)

    # langsung init koneksi di sini
    db_manager.init_connection()

    @atexit.register
    def shutdown():
        db_manager.close_connection()

    # register blueprint (semua rute dimasukkan)
    register_routes(app)

    return app
