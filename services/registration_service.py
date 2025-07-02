import json
import os

class RegistrationService:
    def __init__(self, filepath='data/registrations.json'):
        self.filepath = filepath
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def _load_registrations(self):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _save_registrations(self, regs):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(regs, f, indent=4)

    def register_user_to_event(self, user_id, event_id):
        regs = self._load_registrations()
        # Verifica se já está inscrito
        if any(r for r in regs if r['user_id'] == user_id and r['event_id'] == event_id):
            return False  # Já inscrito

        regs.append({'user_id': user_id, 'event_id': event_id})
        self._save_registrations(regs)
        return True

    def get_user_events(self, user_id):
        regs = self._load_registrations()
        return [r['event_id'] for r in regs if r['user_id'] == user_id]

    def get_event_users(self, event_id):
        regs = self._load_registrations()
        return [r['user_id'] for r in regs if r['event_id'] == event_id]

    def is_user_registered(self, user_id, event_id):
        regs = self._load_registrations()
        return any(r for r in regs if r['user_id'] == user_id and r['event_id'] == event_id)
