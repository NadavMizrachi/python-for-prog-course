from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from src.gui_proj.data.users_repo_db import UsersRepoDB
from src.gui_proj.logic.sign_up import SignUp
from src.gui_proj.model.user_model import User

# TODO make "signUp2 page, to fill firstName, lastName, BirthDate, photo


class SignUpScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(
            r'signup.ui',
            self
        )

        self.setFixedWidth(1200)
        self.setFixedHeight(800)

        self.signUpButton.clicked.connect(self.sign_up)

    def sign_up(self):
        username_txt = self.username.text()
        passwd_txt = self.password.text()
        passwd_conf_txt = self.passwordConfirmation.text()

        validation_res = SignUp.is_valid(username_txt, passwd_txt, passwd_conf_txt)
        is_valid = validation_res[0]
        description = validation_res[1]
        if is_valid:
            UsersRepoDB.get_instance().add(
                User(username_txt, passwd_txt)
            )

        else:
            self.errorLabel.setText(description)



