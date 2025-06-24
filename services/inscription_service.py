import json
import os
from models.inscription import Inscription

class InscriptionService:
    def __init__(self, filepath='data/inscriptions.json'):
        self.filepath = filepath
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def _load_inscriptions(self):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [Inscription(**item) for item in data]

    def _save_inscriptions(self, inscriptions):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump([ins.to_dict() for ins in inscriptions], f, indent=4)

    def subscribe_user_to_event(self, user_id, event_id):
        """Inscreve um usuário em um evento."""
        inscriptions = self._load_inscriptions()


        new_id = max([i.id for i in inscriptions], default=0) + 1
        new_inscription = Inscription(id=new_id, user_id=user_id, event_id=event_id)

        inscriptions.append(new_inscription)
        self._save_inscriptions(inscriptions)
        return new_inscription

    def get_inscriptions_for_event(self, event_id):
        inscriptions = self._load_inscriptions()
        return [i for i in inscriptions if i.event_id == event_id]