from bottle import view, request, redirect, template
from services.event_service import EventService
# Importamos o UserService para futuras verificações de permissões
from services.user_service import UserService 

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

        name = request.forms.get("name").strip()
        date = request.forms.get("date")
        location = request.forms.get("location").strip()
        capacity_raw = request.forms.get("capacity")
        description = request.forms.get("description").strip()
        
        error, capacity = validate_event_data(name, date, location, capacity_raw)
        
        if error:
            return template( "event_form", event=None, action='/events/new', error=error, session=session )

        event_service.create(name, date, location, capacity, description)
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
        
        # TODO: Adicionar a lógica de atualização no EventService e chamá-la aqui
        print(f"Lógica de ATUALIZAR para o evento {event_id} virá aqui.")
        redirect(f'/events/{event_id}')

    # Rota para DELETAR um evento
    @app.route('/events/delete/<event_id:int>', method='POST')
    def delete_event(event_id):
        session = request.environ.get('beaker.session')
        if not session.get('is_admin'):
            return redirect('/')
        
        event_service.delete(event_id)
        redirect('/')