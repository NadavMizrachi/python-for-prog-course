from src.gui_proj.data.users_repo import UsersRepo
from src.gui_proj.data.users_repo_db import UsersRepoDB


class SignUp:
    @staticmethod
    def is_valid(username, passwd, passwd_conf):
        if username == '' or passwd == '' or passwd_conf == '':
            return (
                False,
                "One of the fields is empty"
            )

        if passwd != passwd_conf:
            return (
                False,
                "Passwords does not match"
            )

        if UsersRepoDB.get_instance().is_exists(username):
            return (
                False,
                "Username is already exists"
            )
        return True, ""


