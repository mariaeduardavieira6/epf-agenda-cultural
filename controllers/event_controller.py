from bottle import route, template, request, redirect
from models.event import Event
from services.event_service import EventService

def validar_evento(title, description, date, location, capacity_raw):
    if not title or not description or not date or not location or not capacity_raw:
        return "Todos os campos são obrigatórios.", None

    try:
        capacity = int(capacity_raw)
        if capacity <= 0:
            return "A capacidade deve ser um número positivo.", None
    except ValueError:
        return "A capacidade deve ser um número válido.", None

    return None, int(capacity_raw)  


@route("/events")
def list_events():
    events = EventService.get_all()
    return template("event_list", events=events)

@route("/events/<event_id>")
def event_detail(event_id):
    event = EventService.get_by_id(event_id)
    if not event:
        return "Evento não encontrado!"
    return template("event_detail", event=event)

@route("/events/new")
def new_event_form():
    return template("event_form", event=None, error=None)

@route("/events/new", method="POST")
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
    EventService.create(event)
    redirect("/events")

@route("/events/<event_id>/edit")
def edit_event_form(event_id):
    event = EventService.get_by_id(event_id)
    if not event:
        return "Evento não encontrado!"
    return template("event_form", event=event, error=None)

@route("/events/<event_id>/edit", method="POST")
def update_event(event_id):
    event = EventService.get_by_id(event_id)
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

    EventService.update(event)
    redirect("/events")

@route("/events/<event_id>/delete")
def delete_event(event_id):
    EventService.delete(event_id)
    redirect("/events")
