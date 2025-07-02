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
    
    def get_all(self):
        return self._load_users()
    
    def create_user(self, name, email, password, birthdate):
        users = self.get_all()
        is_admin = False
        if len(users) == 0:
            is_admin = True  # primeiro usuário será admin

        # gera novo ID (exemplo)
        new_id = max((u.id for u in users), default=0) + 1

        new_user = User(
            id=new_id,
            name=name,
            email=email,
            password=password,
            birthdate=birthdate,
            is_admin=is_admin
        )
        
        users.append(new_user)
        self._save_users(users)  # método que salva no JSON

        return new_user