from contextlib import contextmanager
import pymysql
import os

from dotenv import load_dotenv
from pymysql import Connection

load_dotenv()


class DatabaseManager:
    def __init__(self):
        # init variable to store database
        self.session: Connection | None = None

    # set connection database
    def init_connection(self):
        # check session, skip if already set
        if self.session:
            print("[INFO] Connection already initialized.")
            return

        # connect database
        try:
            self.session = pymysql.connect(
                host=os.getenv("DB_HOSTNAME"),
                port=int(os.getenv("DB_PORT", 3306)),
                user=os.getenv("DB_USERNAME"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME"),
                cursorclass=pymysql.cursors.DictCursor
            )
            print("[INIT] Database connection established.")
        except pymysql.MySQLError as e:
            print(f"[ERROR] Failed to connect: {e}")
            self.session = None

    # get database from variable init session
    def get_session(self) -> Connection:
        if not self.session:
            raise ConnectionError(
                "Database not initialized. Call init_connection() first."
            )
        return self.session

    # close database connection
    def close_connection(self):
        if self.session:
            self.session.close()
            self.session = None
            print("[SHUTDOWN] Database connection closed.")
        else:
            print("[INFO] No active connection to close.")


db_manager = DatabaseManager()