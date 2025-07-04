"""Este arquivo contém a classe EventService, responsável por toda a lógica de
negócio e persistência de dados para os eventos, manipulando o arquivo data/events.json.
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
        Construtor da classe. Garante que o arquivo de dados exista.
        """
        self.filepath = filepath
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def _load_events(self):
        """Método privado para carregar a lista de eventos do arquivo JSON."""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                if not isinstance(data, list):
                    return []
                return [Event(**item) for item in data]
            except json.JSONDecodeError:
                return [] 

    def _save_events(self, events):
        """Método privado para salvar a lista de eventos no arquivo JSON."""
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump([e.to_dict() for e in events], f, indent=4)

    def get_all(self):
        """Retorna uma lista com todos os eventos."""
        return self._load_events()

    def get_by_id(self, event_id):
        """Busca um evento específico pelo seu ID único."""
        try:
            event_id = int(event_id)
        except (ValueError, TypeError):
            return None
        for event in self._load_events():
            if event.id == event_id:
                return event
        return None
    
    def search_events(self, query="", category=""):
        """
        Busca e filtra eventos por nome e/ou categoria.
        """
        events = self.get_all()
        
        if query:
            events = [
                event for event in events 
                if query.lower() in event.name.lower()
            ]
        
        # --- INÍCIO DA ALTERAÇÃO ---
        if category:
            events = [
                event for event in events
                # Adicionamos 'if event.category' para garantir que a categoria não é None
                if event.category and event.category.lower() == category.lower()
            ]
        # --- FIM DA ALTERAÇÃO ---
            
        return events

    def create(self, name, date, location, capacity, description, category):
        """
        Cria um novo evento, agora incluindo a categoria, e o salva no arquivo.
        """
        events = self._load_events()
        new_id = max((event.id for event in events), default=0) + 1
        
        new_event = Event(
            id=new_id,
            name=name,
            date=date,
            location=location,
            capacity=int(capacity),
            description=description,
            category=category
        )

        events.append(new_event)
        self._save_events(events)
        return new_event

    def update(self, event_id, data):
        """Atualiza um evento existente com os novos dados."""
        events = self._load_events()
        event_found = False
        for i, event in enumerate(events):
            if event.id == int(event_id):
                event.name = data.get('name', event.name)
                event.date = data.get('date', event.date)
                event.location = data.get('location', event.location)
                event.capacity = int(data.get('capacity', event.capacity))
                event.description = data.get('description', event.description)
                event.category = data.get('category', event.category)
                event_found = True
                break
        
        if event_found:
            self._save_events(events)
        return event_found

    def delete(self, event_id):
        """Remove um evento pelo seu ID."""
        events = self._load_events()
        original_len = len(events)
        events = [event for event in events if event.id != int(event_id)]
        
        if len(events) < original_len:
            self._save_events(events)
            return True
        return False
        
    def get_total_count(self):
        """Retorna o número total de eventos cadastrados."""
        events = self._load_events()
        return len(events)

    def get_total_categories(self):
        """Retorna o número total de categorias de eventos distintas."""
        events = self._load_events()
        # Cria um conjunto (set) para contar apenas categorias únicas
        unique_categories = {event.category for event in events if event.category}
        return len(unique_categories)
