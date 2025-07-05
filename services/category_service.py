
"""
Este arquivo contém a classe CategoryService, responsável pela lógica
de negócio e persistência de dados para as categorias.
"""

import json
import os
from models.category import Category

class CategoryService:
    """
    Classe de serviço que gerencia a lógica de leitura para a entidade Category,
    utilizando um arquivo JSON como fonte de dados.
    """
    def __init__(self, filepath='data/categories.json'):
        """
        Construtor da classe.
        
        Args:
            filepath (str): O caminho para o arquivo JSON de categorias.
        """
        self.filepath = filepath
        # Garante que o diretório e o arquivo de dados existam
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def _load_categories(self):
        """Método privado para carregar a lista de categorias do arquivo JSON."""
        try:
            with open(self.filepath, 'r', encoding='utf-8-sig') as f: # <-- ALTERAÇÃO AQUI
                data = json.load(f)
                if not isinstance(data, list):
                    return []
                return [Category.from_dict(item) for item in data]
        except (json.JSONDecodeError, FileNotFoundError):
            return []
        
    def _save_categories(self, categories):
        with open(self.filepath, 'w', encoding='utf-8') as f: # <-- ALTERAÇÃO AQUI
            json.dump([c.to_dict() for c in categories], f, indent=4, ensure_ascii=False) # <-- ALTERAÇÃO AQUI

    def get_all(self):
        """Retorna uma lista com todas as categorias."""
        return self._load_categories()

    def get_by_id(self, category_id):
        """Busca uma categoria específica pelo seu ID único."""
        try:
            category_id = int(category_id)
        except (ValueError, TypeError):
            return None
            
        for category in self._load_categories():
            if category.id == category_id:
                return category
        return None