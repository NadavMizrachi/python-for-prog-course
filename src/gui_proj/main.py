from PyQt5.QtWidgets import QApplication, QStackedWidget
import welcome_screen

app = QApplication([])
ws = welcome_screen.WelcomeScreen()
ws.show()
app.exec_()


