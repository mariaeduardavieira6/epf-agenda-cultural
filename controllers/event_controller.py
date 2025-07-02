from bottle import view, request, redirect, template
from services.event_service import EventService
# Importamos o UserService para futuras verificações de permissões
from services.user_service import UserService 
from services.registration_service import RegistrationService

# --- Função de Validação 
def validate_event_data(name, date, location, capacity_raw):
    """Valida os dados do formulário de evento."""
    if not all([name, date, location, capacity_raw]):
        return "Todos os campos são obrigatórios.", None
    try:
        capacity = int(capacity_raw)
        if capacity <= 0:
            return "A capacidade deve ser um número positivo.", None
    except ValueError:
        return "A capacidade deve ser um número válido.", None
    return None, capacity

# --- Configuração das Rotas ---
def setup(app):
    event_service = EventService()
    user_service = UserService() # Instância para futuras verificações
    registration_service = RegistrationService()

    # Rota da página inicial: Lista de Eventos
    @app.route('/')
    @view('event_list')
    def list_events():
        events = event_service.get_all()
        return dict(
            events=events,
            session=request.environ.get('beaker.session')
        )

    # Rota para ver detalhes de um evento específico
    @app.route('/events/<event_id:int>')
    @view('event_detail')
    def event_detail(event_id):
        event = event_service.get_by_id(event_id)
        return dict(
            event=event,
            session=request.environ.get('beaker.session')
        )

    # Rota para mostrar o formulário de criação
    @app.route('/events/new', method='GET')
    @view('event_form')
    def new_event_form():
        session = request.environ.get('beaker.session')
        # Proteção: Apenas usuários logados podem criar eventos
        if not session.get('user_name'):
            return redirect('/login')
        
        return dict(
            event=None,
            action='/events/new',
            error=None,
            session=session
        )

    # Rota para processar a criação de um novo evento
    @app.route('/events/new', method='POST')
    def create_event():
        session = request.environ.get('beaker.session')
        if not session.get('user_name'):
            return redirect('/login')
        
        
        name = (request.forms.get("name") or "").strip()
        date = (request.forms.get("date") or "").strip()
        location = (request.forms.get("location") or "").strip()
        capacity_raw = (request.forms.get("capacity") or "").strip()
        description = (request.forms.get("description") or "").strip()


        print(f"Dados recebidos: {name}, {date}, {location}, {capacity_raw}, {description}")

        error, capacity = validate_event_data(name, date, location, capacity_raw)

        if error:
            return template("event_form", event=None, action='/events/new', error=error, session=session)

        try:
            event_service.create(name, date, location, capacity, description)
        except Exception as e:
            print(f"Erro ao criar evento: {e}")
            return template("event_form", event=None, action='/events/new', error="Erro interno ao salvar o evento.", session=session)

        redirect('/')
        
    # --- ROTAS NOVAS PARA EDITAR E DELETAR ---

    # Rota para mostrar o formulário de EDIÇÃO
    @app.route('/events/edit/<event_id:int>', method='GET')
    @view('event_form')
    def edit_event_form(event_id):
        session = request.environ.get('beaker.session')
        # Proteção: Apenas usuários administradores podem editar
        if not session.get('is_admin'):
            return redirect('/')

        event = event_service.get_by_id(event_id)
        return dict(
            event=event,
            action=f'/events/edit/{event_id}', # Ação aponta para a rota de update
            error=None,
            session=session
        )

    # Rota para processar a ATUALIZAÇÃO de um evento
    @app.route('/events/edit/<event_id:int>', method='POST')
    def update_event(event_id):
        session = request.environ.get('beaker.session')
        if not session.get('is_admin'):
            return redirect('/')

        name = request.forms.get("name")
        date = request.forms.get("date")
        location = request.forms.get("location")
        capacity = request.forms.get("capacity")
        description = request.forms.get("description")

        updated = event_service.update(event_id, name, date, location, capacity, description)
        if not updated:
            return template(
            "event_form", 
            event=event_service.get_by_id(event_id), 
            action=f'/events/edit/{event_id}', 
            error="Erro ao atualizar evento.", 
            session=session
        )

        redirect(f'/events/{event_id}')


    # Rota para DELETAR um evento
    @app.route('/events/delete/<event_id:int>', method='POST')
    def delete_event(event_id):
        session = request.environ.get('beaker.session')
        if not session.get('is_admin'):
            return redirect('/')
        
        event_service.delete(event_id)
        redirect('/')

    #Rota para inscrição em um determinado evento
    @app.route('/events/<event_id:int>/register', method='GET')
    @view('event_register_form')
    def show_register_event_form(event_id):
        session = request.environ.get('beaker.session')
        if not session.get('user_id'):
            return redirect('/login')

        event = event_service.get_by_id(event_id)
        if not event:
            return redirect('/')
        
        return dict(event=event, session=session, error = None)

    @app.route('/events/<event_id:int>/register', method='POST')
    def process_register_event(event_id):
        session = request.environ.get('beaker.session')
        if not session.get('user_id'):
            return redirect('/login')

        user_id = session['user_id']
        success = registration_service.register_user_to_event(user_id, event_id)

        if not success:
            # Já inscrito ou erro
            return template('event_register_form', event=event_service.get_by_id(event_id),
                            error='Você já está inscrito neste evento.', session=session)


    @app.route('/events/<event_id:int>')
    @view('event_detail')
    def event_detail(event_id):
        event = event_service.get_by_id(event_id)
        session = request.environ.get('beaker.session')
        return dict(
            event=event,
            session=session,
            registration_service=registration_service
        )