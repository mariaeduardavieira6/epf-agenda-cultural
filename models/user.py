class User:
    def __init__(self, id, name, email, password, birthdate, is_admin=False):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.birthdate = birthdate
        self.is_admin = is_admin

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email

    def get_password(self):
        
        return self.password

    def get_birthdate(self):
        return self.birthdate
   
    def to_dict(self):
        """Converte o objeto para um dicionário para poder salvar no JSON."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "birthdate": self.birthdate,
            "is_admin": self.is_admin
        }

class AdminUser(User):
    """ Esta classe não precisa de alterações. """
    def __init__(self, id, name, email, password, birthdate):
        super().__init__(id, name, email, password, birthdate, is_admin=True)

