import json
import os

from services.event_service import EventService
from services.user_service import UserService

class InscriptionService:
    """
    Serviço que gerencia a lógica de inscrições, conectando usuários e eventos.
    Manipula o arquivo inscriptions.json.
    """
    def __init__(self, user_service: UserService, event_service: EventService):
        self.filepath = os.path.join('data', 'inscriptions.json')
        self.user_service = user_service
        self.event_service = event_service
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Garante que o arquivo de inscrições exista."""
        if not os.path.exists(self.filepath):
            try:
                with open(self.filepath, 'w', encoding='utf-8') as f:
                    json.dump([], f)
            except Exception as e:
                print(f"[Erro] Não foi possível criar o arquivo de inscrições: {e}")

    def _read_inscriptions(self):
        """Lê os dados do arquivo inscriptions.json."""
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        except Exception as e:
            print(f"[Erro] Falha ao ler inscrições: {e}")
            return []

    def _write_inscriptions(self, inscriptions):
        """Escreve os dados no arquivo inscriptions.json."""
        try:
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(inscriptions, f, indent=4)
        except Exception as e:
            print(f"[Erro] Falha ao salvar inscrições: {e}")

    def subscribe_user_to_event(self, user_id: int, event_id: int):
        event = self.event_service.get_by_id(event_id)
        if not event:
            return {'success': False, 'message': 'Evento não encontrado.'}

        if self.is_user_subscribed(user_id, event_id):
            return {'success': False, 'message': 'Você já está inscrito neste evento.'}

        subscribers_count = len(self.get_subscriber_ids_by_event(event_id))
        if subscribers_count >= event.capacity:
            return {'success': False, 'message': 'Este evento já atingiu a capacidade máxima.'}

        all_inscriptions = self._read_inscriptions()
        all_inscriptions.append({'user_id': user_id, 'event_id': event_id})

        self._write_inscriptions(all_inscriptions)
        return {'success': True, 'message': 'Inscrição realizada com sucesso!'}

    def cancel_subscription(self, user_id: int, event_id: int):
        all_inscriptions = self._read_inscriptions()
        initial_count = len(all_inscriptions)

        inscriptions_to_keep = [
            insc for insc in all_inscriptions
            if not (insc['user_id'] == user_id and insc['event_id'] == event_id)
        ]

        if len(inscriptions_to_keep) < initial_count:
            self._write_inscriptions(inscriptions_to_keep)
            return {'success': True, 'message': 'Inscrição cancelada com sucesso.'}
        
        return {'success': False, 'message': 'Inscrição não encontrada.'}

    def get_subscribers_by_event(self, event_id: int):
        subscriber_ids = self.get_subscriber_ids_by_event(event_id)
        subscribers_details = [self.user_service.get_by_id(uid) for uid in subscriber_ids]
        return [user for user in subscribers_details if user]

    def get_subscriber_ids_by_event(self, event_id: int):
        all_inscriptions = self._read_inscriptions()
        return [
            inscription['user_id']
            for inscription in all_inscriptions
            if inscription['event_id'] == event_id
        ]

    def is_user_subscribed(self, user_id: int, event_id: int):
        all_inscriptions = self._read_inscriptions()
        for inscription in all_inscriptions:
            if inscription['user_id'] == user_id and inscription['event_id'] == event_id:
                return True
        return False
