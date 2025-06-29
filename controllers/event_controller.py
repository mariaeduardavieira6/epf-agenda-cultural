# Arquivo: controllers/event_controller.py
from bottle import view, request, redirect
from services.event_service import EventService

def setup(app):
    event_service = EventService()

    # Rota da página inicial: Lista de Eventos
    @app.route('/')
    @view('event_list')
    def list_events():
        return dict(
            events=event_service.get_all(),
            session=request.environ.get('beaker.session')
        )
    
    # TODO: As outras rotas de evento da Dupla 2 virão aqui.