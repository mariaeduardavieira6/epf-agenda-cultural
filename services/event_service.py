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
        try:
            event_id = int(event_id)
        except ValueError:
            return None # Retorna None se o ID não for um número válido

        for event in self._load_events():
            if event.id == event_id:
                return event
        return None
    
    def create(self, name, date, location, capacity, description):
        """Cria um novo evento e o salva no arquivo JSON."""
        events = self._load_events()

        # Gera um novo ID baseado no maior ID existente
        new_id = max((event.id for event in events), default=0) + 1

        # Cria o novo objeto de evento
        new_event = Event(
            id=new_id,
            name=name,
            date=date,
            location=location,
            capacity=int(capacity),
            description=description
        )

        events.append(new_event)
        self._save_events(events)
        return new_event # Retorna o evento criado

    def update(self, event_id, name=None, date=None, location=None, capacity=None, description=None):
        """
        Atualiza um evento existente.

        Args:
            event_id (int | str): O ID do evento a ser atualizado.
            name (str, optional): Novo nome do evento.
            date (str, optional): Nova data do evento.
            location (str, optional): Nova localização do evento.
            capacity (int, optional): Nova capacidade do evento.
            description (str, optional): Nova descrição do evento.

        Returns:
            Event | None: O objeto Event atualizado se encontrado, ou None caso contrário.
        """
        events = self._load_events()
        try:
            event_id = int(event_id)
        except ValueError:
            return None

        for i, event in enumerate(events):
            if event.id == event_id:
                if name is not None:
                    events[i].name = name
                if date is not None:
                    events[i].date = date
                if location is not None:
                    events[i].location = location
                if capacity is not None:
                    events[i].capacity = int(capacity)
                if description is not None:
                    events[i].description = description
                
                self._save_events(events)
                return events[i] # Retorna o evento atualizado
        return None

    def delete(self, event_id):
        """
        Remove um evento pelo seu ID.

        Args:
            event_id (int | str): O ID do evento a ser removido.

        Returns:
            bool: True se o evento foi removido, False caso contrário.
        """
        events = self._load_events()
        try:
            event_id = int(event_id)
        except ValueError:
            return False

        original_len = len(events)
        events = [event for event in events if event.id != event_id]
        
        if len(events) < original_len:
            self._save_events(events)
            return True
        return False