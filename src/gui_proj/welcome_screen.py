from PyQt5.QtWidgets import QMainWindow, QStackedWidget
from PyQt5.uic import loadUi

from src.gui_proj.login_screen import LoginScreen
from src.gui_proj.signup_screen import SignUpScreen


class WelcomeScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi(
            r'main.ui',
            self
        )

        self.setFixedWidth(1200)
        self.setFixedHeight(800)

        self.loginButton.clicked.connect(self.login_button_on_clicked)
        self.signInButton.clicked.connect(self.sign_in_button_on_clicked)

        self.widgets = QStackedWidget()
        self.widgets.addWidget(self)

    def show(self) -> None:
        self.widgets.show()

    def login_button_on_clicked(self):
        print("clicked log in button")
        login_screen = LoginScreen()
        self.widgets.addWidget(login_screen)
        self.widgets.setCurrentWidget(login_screen)

    def sign_in_button_on_clicked(self):
        print("clicked on sign in button")
        signup_screen = SignUpScreen()
        self.widgets.addWidget(signup_screen)
        self.widgets.setCurrentWidget(signup_screen)
