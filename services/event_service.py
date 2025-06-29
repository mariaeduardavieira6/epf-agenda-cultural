import json
import os
from models.event import Event

class EventService:
    def __init__(self, arquivo="events.json"):
        self.arquivo = arquivo
        self.eventos = self._carregar_eventos()

    def _carregar_eventos(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    return [Event.from_dict(e) for e in data]
                except json.JSONDecodeError:
                    return []
        return []

    def _salvar_eventos(self):
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump([e.to_dict() for e in self.eventos], f, indent=4, ensure_ascii=False)

    def adicionar_evento(self, evento: Event):
        self.eventos.append(evento)
        self._salvar_eventos()  
        print(f"Evento '{evento.title}' adicionado com sucesso!")

    def listar_eventos(self):
        return self.eventos

    def buscar_evento_por_titulo(self, titulo: str):
        for evento in self.eventos:
            if evento.title == titulo:
                return evento
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
    