# Arquivo: models/user.py
class User:
    def __init__(self, id, name, email, password, birthdate, is_admin=False):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.birthdate = birthdate
        self.is_admin = is_admin

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "birthdate": self.birthdate,
            "is_admin": self.is_admin
        }

class AdminUser(User):
    def __init__(self, id, name, email, password, birthdate):
        super().__init__(id, name, email, password, birthdate, is_admin=True)