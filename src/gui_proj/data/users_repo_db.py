import csv
import sqlite3

from src.gui_proj.data.exceptions import UsernameAlreadyExistsException
from src.gui_proj.model.user_model import User

DB_URL = r'data\proj_db.db'


class UsersRepoDB:

    ins = None

    @staticmethod
    def get_instance():
        if UsersRepoDB.ins is None:
            UsersRepoDB.ins = UsersRepoDB()
        return UsersRepoDB.ins

    def __init__(self):
        self.conn = sqlite3.connect(DB_URL)

    def __del__(self):
        self.conn.close()

    def is_exists(self, username):
        query = "SELECT * FROM users WHERE username = '" + username + "' "
        res = self.conn.cursor().execute(query)
        is_exist = res.fetchone() is not None
        return is_exist

    def add(self, user):
        if self.is_exists(user.username):
            raise UsernameAlreadyExistsException()
        query = f"""
            INSERT INTO users(username, password)
            VALUES('{user.username}', '{user.password}')
        """
        self.conn.cursor().executescript(query)
        self.conn.commit()

