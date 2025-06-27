from models.event import Event
from services.event_service import EventService
from bottle import template, request, redirect

event_service = EventService()  

def validar_evento(title, description, date, location, capacity_raw):
    if not title or not description or not date or not location or not capacity_raw:
        return "Todos os campos são obrigatórios.", None

    try:
        capacity = int(capacity_raw)
        if capacity <= 0:
            return "A capacidade deve ser um número positivo.", None
    except ValueError:
        return "A capacidade deve ser um número válido.", None

    return None, capacity  

def setup(app):
    @app.route("/events")
    def list_events():
        events = event_service.listar_eventos()
        return template("event_list", events=events)

    @app.route("/events/<event_title>")
    def event_detail(event_title):
        event = event_service.buscar_evento_por_titulo(event_title)
        if not event:
            return "Evento não encontrado!"
        return template("event_detail", event=event)

    @app.route("/events/new")
    def new_event_form():
        return template("event_form", event=None, error=None)

    @app.route("/events/new", method="POST")
    def create_event():
        title = request.forms.get("title").strip()
        description = request.forms.get("description").strip()
        date = request.forms.get("date").strip()
        location = request.forms.get("location").strip()
        capacity_raw = request.forms.get("capacity").strip()

        erro, capacity = validar_evento(title, description, date, location, capacity_raw)
        if erro:
            return template("event_form", event=None, error=erro)

        event = Event(title, description, date, location, capacity)
        event_service.adicionar_evento(event)
        redirect("/events")

    @app.route("/events/<event_title>/edit")
    def edit_event_form(event_title):
        event = event_service.buscar_evento_por_titulo(event_title)
        if not event:
            return "Evento não encontrado!"
        return template("event_form", event=event, error=None)

    @app.route("/events/<event_title>/edit", method="POST")
    def update_event(event_title):
        event = event_service.buscar_evento_por_titulo(event_title)
        if not event:
            return "Evento não encontrado!"

        title = request.forms.get("title").strip()
        description = request.forms.get("description").strip()
        date = request.forms.get("date").strip()
        location = request.forms.get("location").strip()
        capacity_raw = request.forms.get("capacity").strip()

        erro, capacity = validar_evento(title, description, date, location, capacity_raw)
        if erro:
            return template("event_form", event=event, error=erro)

        event.title = title
        event.description = description
        event.date = date
        event.location = location
        event.capacity = capacity

        event_service.remover_evento(event_title)
        event_service.adicionar_evento(event)
        redirect("/events")

    @app.route("/events/<event_title>/delete")
    def delete_event(event_title):
        event_service.remover_evento(event_title)
        redirect("/events")

