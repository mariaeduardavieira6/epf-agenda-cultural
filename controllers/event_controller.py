from bottle import view, request, redirect, template
from services.event_service import EventService
from services.user_service import UserService
from services.inscription_service import InscriptionService
# --- ALTERAÇÃO: Importando o serviço de Categoria ---
from services.category_service import CategoryService

# --- Função de Validação ---
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
    user_service = UserService()
    # --- ALTERAÇÃO: Instanciando o serviço de Categoria ---
    category_service = CategoryService()
    inscription_service = InscriptionService(user_service=user_service, event_service=event_service)

    # --- INÍCIO DA ALTERAÇÃO PRINCIPAL ---
    # Agora, a lista de eventos lê o category_id da URL
    @app.route('/')
    @app.route('/events')
    @view('event_list')
    def list_events():
        search_query = request.query.get('query', '').strip()
        category_id = request.query.get('category_id', '').strip()

        category_name_filter = ""
        title = "Todos os Eventos"

        # Se um ID de categoria foi passado na URL
        if category_id:
            # Busca a categoria pelo ID para obter o nome
            category = category_service.get_by_id(category_id)
            if category:
                category_name_filter = category.name
                title = f"Eventos de: {category_name_filter}"

        # Usa o nome da categoria para filtrar os eventos
        events = event_service.search_events(query=search_query, category=category_name_filter)
        
        return dict(
            events=events,
            title=title,
            session=request.environ.get('beaker.session')
        )
    # --- FIM DA ALTERAÇÃO PRINCIPAL ---

    # Detalhes de um evento
    @app.route('/events/<event_id:int>')
    @view('event_detail')
    def event_detail(event_id):
        session = request.environ.get('beaker.session')
        event = event_service.get_by_id(event_id)
        subscribers = inscription_service.get_subscribers_by_event(event_id)
        user_id = session.get('user_id')
        is_subscribed = False

        if user_id:
            is_subscribed = inscription_service.is_user_subscribed(user_id, event_id)

        message = session.pop('message', None)

        return dict(
            event=event,
            subscribers=subscribers,
            is_subscribed=is_subscribed,
            message=message,
            session=session
        )

    # Inscrever usuário
    @app.route('/events/<event_id>/subscribe', method='POST')
    def subscribe_to_event(event_id):
        session = request.environ.get('beaker.session')
        user_id = session.get('user_id')
        if not user_id:
            return redirect('/login')

        result = inscription_service.subscribe_user_to_event(user_id, int(event_id))
        session['message'] = result['message']
        session.save()
        return redirect(f'/events/{event_id}')

    # Cancelar inscrição
    @app.route('/events/<event_id>/unsubscribe', method='POST')
    def unsubscribe_from_event(event_id):
        session = request.environ.get('beaker.session')
        user_id = session.get('user_id')
        if not user_id:
            return redirect('/login')

        result = inscription_service.cancel_subscription(user_id, int(event_id))
        session['message'] = result['message']
        session.save()
        return redirect(f'/events/{event_id}')

    # Mostrar formulário de novo evento
    @app.route('/events/new', method='GET')
    @view('event_form')
    def new_event_form():
        session = request.environ.get('beaker.session')
        if not session.get('user_name'):
            return redirect('/login')
        return dict(event=None, action='/events/new', error=None, session=session)

    # Criar novo evento
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
        category = (request.forms.get("category") or "Geral").strip() 

        error, capacity = validate_event_data(name, date, location, capacity_raw)

        if error:
            return template("event_form", event=None, action='/events/new', error=error, session=session)

        try:
            event_service.create(name, date, location, capacity, description, category)
        except Exception as e:
            print(f"Erro ao criar evento: {e}")
            return template("event_form", event=None, action='/events/new', error="Erro interno ao salvar o evento.", session=session)

        return redirect('/')

    # Mostrar formulário de edição
    @app.route('/events/edit/<event_id:int>', method='GET')
    @view('event_form')
    def edit_event_form(event_id):
        session = request.environ.get('beaker.session')
        if not session.get('is_admin'):
            return redirect('/')

        event = event_service.get_by_id(event_id)
        return dict(event=event, action=f'/events/edit/{event_id}', error=None, session=session)

    # Atualizar evento existente
    @app.route('/events/edit/<event_id:int>', method='POST')
    def update_event(event_id):
        session = request.environ.get('beaker.session')
        if not session.get('is_admin'):
            return redirect('/')

        data = {
            'name': request.forms.get("name"),
            'date': request.forms.get("date"),
            'location': request.forms.get("location"),
            'capacity': request.forms.get("capacity"),
            'description': request.forms.get("description"),
            'category': request.forms.get("category")
        }

        updated = event_service.update(event_id, data)
        if not updated:
            return template(
                "event_form",
                event=event_service.get_by_id(event_id),
                action=f'/events/edit/{event_id}',
                error="Erro ao atualizar evento.",
                session=session
            )

        return redirect(f'/events/{event_id}')

    # Deletar evento
    @app.route('/events/delete/<event_id:int>', method='POST')
    def delete_event(event_id):
        session = request.environ.get('beaker.session')
        if not session.get('is_admin'):
            return redirect('/')

        event_service.delete(event_id)
        return redirect('/')
