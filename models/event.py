# models/event.py

"""
Este arquivo define a classe que representa a entidade de um evento na aplicação,
cumprindo o papel da camada "Model" na arquitetura MVC.
"""

class Event:
    """
    Representa a entidade de um evento cultural no sistema.
    Define os atributos e comportamentos essenciais de um evento.
    """
    # --- ALTERAÇÃO AQUI: Adicionado 'price' no construtor ---
    def __init__(self, id, name, date, location, capacity, description="", category="", price=0.0):
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
        """
        self.id = id
        self.name = name
        self.date = date
        self.location = location
        self.capacity = capacity
        self.description = description
        self.category = category
        # --- NOVO ATRIBUTO ---
        self.price = float(price)

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
            # --- NOVO CAMPO NO DICIONÁRIO ---
            "price": self.price
        }
