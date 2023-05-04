import csv

from src.gui_proj.data.exceptions import UsernameAlreadyExistsException
from src.gui_proj.model.user_model import User

CSV_PATH = r'data\users.csv'


class UsersRepo:

    ins = None

    @staticmethod
    def get_instance():
        if UsersRepo.ins is None:
            UsersRepo.ins = UsersRepo()
        return UsersRepo.ins

    def __init__(self):
        self.f = open(CSV_PATH, 'a+', newline='', encoding='utf-8')
        self.csv = csv.reader(self.f)

    def __del__(self):
        self.f.close()

    def is_exists(self, username):
        self.f.seek(0)
        for row in self.csv:
            try:
                id_, user_name, passwd = self.parse_row(row)
                if user_name == username:
                    return True
            except:
                continue
        return False

    def add(self, user):
        if self.is_exists(user.username):
            raise UsernameAlreadyExistsException()
        last_user_id = self.extract_last_user_id()
        self.f.write(f"\n{last_user_id + 1},{user.username},{user.password}")
        self.f.flush()

    def extract_last_user_id(self):
        self.f.seek(0)
        last_row = self.f.readlines()[-1]
        id_val, username_val, pass_val = self.parse_row(last_row)
        return id_val

    def parse_row(self, line):
        return (
            int(line[0]),
            line[1],
            line[2]
        )

