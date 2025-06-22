from bottle import route, template, request, redirect
from models.event import Event
from services.event_service import EventService

@route ("/events")
def list_events():
    events = EventService.get_all()
    return template("event_list", events = events)

@route ("/events/<events_id>")
def event_detail(event_id):
    event = EventService.get_by_id(event_id)
    if not event:
        return "Evento não encontrado!"
    return template("event_detail", event = event)

@route ("/events/new")
def new_event_form():
    return template("event_form", event = None)

@route ("/events/new", method = "POST")
def create_event():
    title = request.forms.get("title")
    description = request.forms.get("description")
    date = request.forms.get("date")
    location = request.forms.get("location")
    capacity = request.forms.get("capacity")

    event = Event(title, description, date, location, int(capacity))
    EventService.create(event)
    redirect("/events")

@route ("/events/<event_id>/edit")
def edit_event_form(event_id):
    event = EventService.get_by_id(event_id)
    if not event:
        return "Evento não encontrado!"
    return template("event_form", event = event)

@route ("/events/<event_id>/edit", method = "POST")
def uptade_event(event_id):
    if not Event:
        return "Evento não encontrado!"
    
    Event.title = request.forms.get("title")
    Event.description = request.forms.get("description")
    Event.date = request.forms.get("date")
    Event.location = request.forms.get("location")
    Event.capacity = request.forms.get("capacity")

    EventService.uptade(Event)
    redirect("/events")

@route ("/events/<event_id>/delete")
def delete_event(event_id):
    EventService.delete(event_id)
    redirect("/events")
