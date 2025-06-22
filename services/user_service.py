# Arquivo: services/user_service.py
import json
import os
from models.user import User

class UserService:
    def __init__(self, filepath='data/users.json'):
        self.filepath = filepath
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def _load_users(self):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            users_data = json.load(f)
        return [User(**data) for data in users_data]

    def _save_users(self, users):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump([user.to_dict() for user in users], f, indent=4)

    def get_by_email(self, email: str):
        for user in self._load_users():
            if user.email == email:
                return user
        return None

    def create_user(self, name, email, password, birthdate):
        users = self._load_users()
        if self.get_by_email(email):
            return None

        new_id = max([user.id for user in users], default=0) + 1
        new_user = User(id=new_id, name=name, email=email, password=password, birthdate=birthdate)

        users.append(new_user)
        self._save_users(users)
        return new_user