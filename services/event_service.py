"""
Este arquivo contém a classe EventService, responsável por toda a lógica de
negócio e persistência de dados para os eventos, manipulando o arquivo data/events.json.
Cumpre o papel da camada de "Service" na arquitetura MVC.
"""
import json
import os
from models.event import Event

class EventService:
    """
    Classe de serviço que gerencia a lógica de CRUD (Create, Read, Update, Delete)
    para a entidade Event, utilizando um arquivo JSON como banco de dados.
    """
    def __init__(self, filepath='data/events.json'):
        """
        Construtor da classe.

        Args:
            filepath (str): O caminho para o arquivo JSON de eventos.
        """
        self.filepath = filepath
        # Garante que o diretório e o arquivo de dados existam
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def _load_events(self):
        """Método privado para carregar a lista de eventos do arquivo JSON."""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Usa list comprehension para transformar cada dicionário em um objeto Event
        return [Event(**item) for item in data]

    def _save_events(self, events):
        """Método privado para salvar a lista de eventos no arquivo JSON."""
        with open(self.filepath, 'w', encoding='utf-8') as f:
            # Usa o método to_dict() do model Event para preparar os dados
            json.dump([e.to_dict() for e in events], f, indent=4)

    def get_all(self):
        """Retorna uma lista com todos os eventos."""
        return self._load_events()

    def get_by_id(self, event_id):
        """
        Busca um evento específico pelo seu ID único.

        Args:
            event_id (int | str): O ID do evento a ser procurado.

        Returns:
            Event | None: O objeto Event se encontrado, ou None caso contrário.
        """
        event_id = int(event_id)
        for event in self._load_events():
            if event.id == event_id:
                return event
        return None

def remover_evento(self, titulo: str):
        evento = self.buscar_evento_por_titulo(titulo)
        if evento:
            self.eventos.remove(evento)
            self._salvar_eventos()  
            print(f"Evento '{titulo}' removido com sucesso!")
            return True
        print(f"Evento '{titulo}' não encontrado.")
        return False

