# Arquivo: services/event_service.py

import json
import os
from models.event import Event  # Assumindo que a Dupla 2 já criou este model

class EventService:
    def __init__(self, filepath='data/events.json'):
        self.filepath = filepath
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def _load_events(self):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # O model Event precisa ter um construtor que aceite estes argumentos
        return [Event(**item) for item in data]

    def _save_events(self, events):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump([e.to_dict() for e in events], f, indent=4)

    def get_all(self):
        return self._load_events()

    def get_by_id(self, event_id):
        event_id = int(event_id)
        for event in self._load_events():
            if event.id == event_id:
                return event
        return None

    def create(self, name, date, location, capacity, description):
        events = self._load_events()
        new_id = max([e.id for e in events], default=0) + 1
        
        new_event = Event(
            id=new_id, 
            name=name, 
            date=date, 
            location=location, 
            capacity=capacity, 
            description=description
        )
        
        events.append(new_event)
        self._save_events(events)
        return new_event

    def delete(self, event_id):
        events = self._load_events()

        updated_events = [e for e in events if e.id != int(event_id)]
        
        self._save_events(updated_events)

