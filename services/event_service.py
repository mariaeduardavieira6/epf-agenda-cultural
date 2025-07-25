import json
import os
from models.event import Event
from datetime import date, timedelta

class EventService:
    """
    Classe de serviço que gere a lógica de CRUD (Create, Read, Update, Delete)
    para a entidade Event, utilizando um ficheiro JSON como banco de dados.
    """
    def __init__(self, filepath='data/events.json'):
        """
        Construtor da classe. Garante que o ficheiro de dados exista.
        """
        self.filepath = filepath
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def _load_events(self):
        """Método privado para carregar a lista de eventos do ficheiro JSON."""
        with open(self.filepath, 'r', encoding='utf-8-sig') as f:
            try:
                data = json.load(f)
                if not isinstance(data, list):
                    return []
                # O model Event já espera 'city', então o carregamento funcionará
                return [Event(**item) for item in data]
            except json.JSONDecodeError:
                return []

    def _save_events(self, events):
        """Método privado para salvar a lista de eventos no ficheiro JSON."""
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump([e.to_dict() for e in events], f, indent=4, ensure_ascii=False)

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

    # ===== ALTERAÇÃO 1: 'search_events' agora busca por 'city' =====
    def search_events(self, query="", category="", city="", time_filter=""): # MUDOU 'location' PARA 'city'
        """
        Busca e filtra eventos por nome, categoria, cidade e/ou período de tempo.
        """
        events = self.get_all()

        if query:
            events = [e for e in events if query.lower() in e.name.lower()]

        if category:
            events = [e for e in events if e.category and e.category.lower() == category.lower()]

        if city: # MUDOU A LÓGICA DE 'location' PARA 'city'
            events = [e for e in events if e.city and e.city.lower() == city.lower()]

        if time_filter:
            today = date.today()

            if time_filter == 'today':
                events = [e for e in events if date.fromisoformat(e.date) == today]

            elif time_filter == 'weekend':
                weekday = today.weekday()
                if weekday <= 4:
                    friday = today + timedelta(days=(4 - weekday))
                else:
                    friday = today - timedelta(days=(weekday - 4))
                weekend_dates = [friday, friday + timedelta(days=1), friday + timedelta(days=2)]
                events = [e for e in events if date.fromisoformat(e.date) in weekend_dates]

            elif time_filter == 'free':
                events = [e for e in events if e.price == 0.0]

        return events
    # --- FIM DA ALTERAÇÃO 1 ---

    def get_featured_events(self):
        """Retorna uma lista apenas com os eventos marcados como destaque."""
        all_events = self._load_events()
        featured_events = [event for event in all_events if event.is_featured]
        return featured_events

    # ===== ALTERAÇÃO 2: 'create' agora aceita o parâmetro 'city' =====
    def create(self, name, date, location, city, capacity, description, category, price=0.0, time="00:00", image_url="", rating=0.0, is_featured=False):
        """
        Cria um novo evento com todos os detalhes e o salva no ficheiro.
        """
        events = self._load_events()
        new_id = max((event.id for event in events), default=0) + 1

        new_event = Event(
            id=new_id, name=name, date=date, location=location, city=city, # 'city' ADICIONADO AQUI
            capacity=int(capacity), description=description, category=category,
            price=float(price), time=time, image_url=image_url,
            rating=float(rating), is_featured=bool(is_featured)
        )
        events.append(new_event)
        self._save_events(events)
        return new_event
    # --- FIM DA ALTERAÇÃO 2 ---

    # ===== ALTERAÇÃO 3: 'update' agora atualiza o campo 'city' =====
    def update(self, event_id, data):
        """Atualiza um evento existente com os novos dados."""
        events = self._load_events()
        event_found = False
        for i, event in enumerate(events):
            if event.id == int(event_id):
                event.name = data.get('name', event.name)
                event.date = data.get('date', event.date)
                event.location = data.get('location', event.location)
                event.city = data.get('city', event.city) # LINHA NOVA ADICIONADA
                event.capacity = int(data.get('capacity', event.capacity))
                event.description = data.get('description', event.description)
                event.category = data.get('category', event.category)
                event.price = float(data.get('price', event.price))
                event.time = data.get('time', event.time)
                event.image_url = data.get('image_url', event.image_url)
                event.rating = float(data.get('rating', event.rating))
                event.is_featured = bool(data.get('is_featured', event.is_featured))
                event_found = True
                break

        if event_found:
            self._save_events(events)
        return event_found
    # --- FIM DA ALTERAÇÃO 3 ---

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
        return len(self._load_events())

    def get_total_categories(self):
        """Retorna o número total de categorias de eventos distintas."""
        return len({event.category for event in self._load_events() if event.category})

    # ===== ALTERAÇÃO 4: NOVO MÉTODO PARA PEGAR CIDADES ÚNICAS =====
    def get_unique_cities(self):
        """Retorna uma lista de cidades únicas e ordenadas."""
        events = self._load_events()
        cities = set()
        for event_data in events:
            if event_data.city:
                cities.add(event_data.city)
        return sorted(list(cities))
    # --- FIM DA ALTERAÇÃO 4 ---

    def get_unique_locations(self):
        """Retorna uma lista de locais (endereços) únicos e ordenados."""
        events = self._load_events()
        locations = set()
        for event_data in events:
            if event_data.location:
                locations.add(event_data.location)
        return sorted(list(locations))