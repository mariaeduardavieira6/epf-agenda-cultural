# services/user_service.py

"""
Módulo de Serviço para Gerenciamento de Usuários (services/user_service.py)

Este arquivo contém a classe UserService, que é responsável por toda a lógica de
negócio e persistência de dados para os usuários, manipulando o arquivo data/users.json.
Cumpre o papel da camada de "Service" na arquitetura MVC.
"""
import json
import os
from models.user import User

class UserService:
    """
    Classe de serviço que gerencia a lógica de CRUD (Create, Read, Update, Delete)
    para a entidade User, utilizando um arquivo JSON como banco de dados.
    """
    def __init__(self, filepath='data/users.json'):
        """
        Construtor da classe. Garante que a pasta e o arquivo de dados existam.
        """
        self.filepath = filepath
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def _load_users(self):
        """
        Método privado para carregar usuários do arquivo JSON de forma segura.

        Returns:
            list[User]: Uma lista de objetos User. Retorna uma lista vazia se
                        o arquivo estiver vazio, corrompido ou não for encontrado.
        """
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                users_data = json.load(f)
            if not isinstance(users_data, list):
                return []
        except (json.JSONDecodeError, FileNotFoundError):
            return []
        
        return [User(**data) for data in users_data]

    def _save_users(self, users):
        """Método privado para salvar a lista de usuários no arquivo JSON."""
        with open(self.filepath, 'w', encoding='utf-8') as f:
            users_data = [user.to_dict() for user in users]
            json.dump(users_data, f, indent=4)

    def get_by_email(self, email: str):
        """Busca um usuário pelo seu endereço de email."""
        for user in self._load_users():
            if user.email == email:
                return user
        return None

    def get_by_id(self, user_id):
        """Busca um usuário pelo seu ID único."""
        try:
            user_id = int(user_id)
        except (ValueError, TypeError):
            return None

        for user in self._load_users():
            if user.id == user_id:
                return user
        return None

    def get_all(self):
        """Retorna todos os usuários."""
        return self._load_users()

    def create_user(self, name, email, password, birthdate):
        """Cria um novo usuário e o salva no arquivo."""
        users = self.get_all()
        is_admin = len(users) == 0

        if self.get_by_email(email):
            return None 

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
        self._save_users(users)
        return new_user

    # --- NOVO MÉTODO ADICIONADO AQUI ---
    def get_total_count(self):
        """Retorna o número total de usuários cadastrados."""
        users = self._load_users()
        return len(users)