from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi


class LoginScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(
            r'login.ui',
            self
        )

        self.setFixedWidth(1200)
        self.setFixedHeight(800)
