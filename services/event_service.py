from models.event import Event

class EventService:
    def __init__(self):
        self.eventos = []

    def adicionar_evento(self, evento: Event):
        self.eventos.append(evento)
        print(f"Evento '{evento.title}' adicionado com sucesso!")

    def listar_eventos(self):
        return self.eventos
    
    
    def buscar_evento_por_titulo(self, titulo: str):
        for evento in self.eventos:
            if evento.titulo == titulo:
                return evento
        return None

    def remover_evento(self, titulo: str):
        evento = self.buscar_evento_por_titulo(titulo)
        if evento:
            self.eventos.remove(evento)
            print(f"Evento '{titulo}' removido com sucesso!")
            return True
        print(f"Evento '{titulo}' não encontrado.")
        return False
