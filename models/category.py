"""
Este arquivo define a classe que representa a entidade de uma Categoria na aplicação.
"""

class Category:
    """
    Representa a entidade de uma categoria de evento no sistema.
    """
    def __init__(self, id, name, icon=""):
        """
        Construtor da classe Category.

        Args:
            id (int): O identificador único da categoria.
            name (str): O nome da categoria (ex: "Música", "Teatro").
            icon (str, optional): O nome de um ícone associado à categoria (ex: "music-note").
        """
        self.id = id
        self.name = name
        self.icon = icon

    def to_dict(self):
        """
        Converte o objeto Category para um dicionário Python.
        """
        return {
            "id": self.id,
            "name": self.name,
            "icon": self.icon
        }
    
    @staticmethod # <-- ESSA LINHA É CRÍTICA!
    def from_dict(data):
        """
        Cria um objeto Category a partir de um dicionário.
        Útil para carregar dados do JSON.
        """
        return Category(
            id=data.get('id'),
            name=data.get('name'),
            icon=data.get('icon', '') # Garante que 'icon' seja um valor padrão se não existir
        )