# models/event.py

"""
Este ficheiro define a classe que representa a entidade de um evento na aplicação,
cumprindo o papel da camada "Model" na arquitetura MVC.
"""

class Event:
    """
    Representa a entidade de um evento cultural no sistema.
    Define os atributos e comportamentos essenciais de um evento.
    """
    # --- ALTERAÇÃO AQUI: Adicionados novos campos para a funcionalidade de destaque ---
    def __init__(self, id, name, date, location, capacity, description="", category="", price=0.0, 
                 time="00:00", image_url="", rating=0.0, is_featured=False):
        """
        Construtor da classe Event.

        Args:
            id (int): O identificador único do evento.
            name (str): O nome do evento.
            date (str): A data do evento.
            location (str): O local onde o evento ocorrerá.
            capacity (int): A capacidade máxima de participantes.
            description (str, optional): Uma descrição mais detalhada do evento.
            category (str, optional): A categoria do evento (ex: "Música", "Teatro").
            price (float, optional): O preço do ingresso. Padrão é 0.0 (gratuito).
            time (str, optional): A hora do evento.
            image_url (str, optional): O URL da imagem de capa do evento.
            rating (float, optional): A classificação do evento (0.0 a 5.0).
            is_featured (bool, optional): Se o evento é um destaque na homepage.
        """
        self.id = id
        self.name = name
        self.date = date
        self.location = location
        self.capacity = capacity
        self.description = description
        self.category = category
        self.price = float(price)
        # --- NOVOS ATRIBUTOS ---
        self.time = time
        self.image_url = image_url
        self.rating = float(rating)
        self.is_featured = bool(is_featured)

    def to_dict(self):
        """
        Converte o objeto Event para um dicionário Python.
        Este método é crucial para salvar os dados no formato JSON.
        """
        return {
            "id": self.id,
            "name": self.name,
            "date": self.date,
            "location": self.location,
            "capacity": self.capacity,
            "description": self.description,
            "category": self.category,
            "price": self.price,
            # --- NOVOS CAMPOS NO DICIONÁRIO ---
            "time": self.time,
            "image_url": self.image_url,
            "rating": self.rating,
            "is_featured": self.is_featured
        }
