from PyQt5 import QtWidgets

from src.gui_proj.data.users_repo import UsersRepo
from src.gui_proj.model.user_model import User

ur = UsersRepo()
print(ur.is_exists("nadav16"))

new_user = "livnat"
ur.add(User(new_user, "pass"))

print("is pass? = " + str(ur.is_exists(new_user)))