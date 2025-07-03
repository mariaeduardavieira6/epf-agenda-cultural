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
        """
        Inicializa o serviço de inscrição, recebendo instâncias dos outros serviços.
        """
        self.filepath = os.path.join('data', 'inscriptions.json')
        self.user_service = user_service
        self.event_service = event_service
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Garante que o arquivo de inscrições exista."""
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def _read_inscriptions(self):
        """Lê os dados do arquivo inscriptions.json."""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _write_inscriptions(self, inscriptions):
        """Escreve os dados no arquivo inscriptions.json."""
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(inscriptions, f, indent=4)

    def subscribe_user_to_event(self, user_id: int, event_id: int):
        """
        Inscreve um usuário em um evento, validando as regras de negócio.
        """
        # Regra 1: O evento deve existir. Usa o EventService.
        event = self.event_service.get_by_id(event_id)
        if not event:
            return {'success': False, 'message': 'Evento não encontrado.'}

        # Regra 2: O usuário já está inscrito?
        if self.is_user_subscribed(user_id, event_id):
            return {'success': False, 'message': 'Você já está inscrito neste evento.'}

        # Regra 3: O evento tem capacidade disponível? 
        subscribers_count = len(self.get_subscriber_ids_by_event(event_id))
        if subscribers_count >= event.capacity:
            return {'success': False, 'message': 'Este evento já atingiu a capacidade máxima.'}

        # Se todas as regras passaram, inscreve o usuário.
        all_inscriptions = self._read_inscriptions()
        # A inscrição é um dicionário simples, não precisamos de um model complexo aqui.
        all_inscriptions.append({'user_id': user_id, 'event_id': event_id})
        self._write_inscriptions(all_inscriptions)
        
        return {'success': True, 'message': 'Inscrição realizada com sucesso!'}

    def cancel_subscription(self, user_id: int, event_id: int):
        """
        Cancela a inscrição de um usuário em um evento. 
        """
        all_inscriptions = self._read_inscriptions()
        initial_count = len(all_inscriptions)
        
        # Filtra a lista, removendo a inscrição correspondente.
        inscriptions_to_keep = [
            insc for insc in all_inscriptions
            if not (insc['user_id'] == user_id and insc['event_id'] == event_id)
        ]

        if len(inscriptions_to_keep) < initial_count:
            self._write_inscriptions(inscriptions_to_keep)
            return {'success': True, 'message': 'Inscrição cancelada com sucesso.'}
        
        return {'success': False, 'message': 'Inscrição não encontrada.'}

    def get_subscribers_by_event(self, event_id: int):
        """
        Lista os detalhes dos usuários inscritos em um evento. [cite: 34, 40]
        """
        subscriber_ids = self.get_subscriber_ids_by_event(event_id)
        
        # Usa o user_service para buscar os dados de cada usuário pelo ID.
        subscribers_details = [self.user_service.get_by_id(uid) for uid in subscriber_ids]
        
        # Retorna a lista de objetos User, removendo possíveis Nones.
        return [user for user in subscribers_details if user]

    def get_subscriber_ids_by_event(self, event_id: int):
        """Retorna uma lista apenas com os IDs dos usuários inscritos."""
        all_inscriptions = self._read_inscriptions()
        return [
            inscription['user_id']
            for inscription in all_inscriptions
            if inscription['event_id'] == event_id
        ]

    def is_user_subscribed(self, user_id: int, event_id: int):
        """Verifica de forma rápida se um usuário já está inscrito."""
        all_inscriptions = self._read_inscriptions()
        for inscription in all_inscriptions:
            if inscription['user_id'] == user_id and inscription['event_id'] == event_id:
                return True
        return False