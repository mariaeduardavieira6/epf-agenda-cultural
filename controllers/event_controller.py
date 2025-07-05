from bottle import view, request, redirect, template
from services.event_service import EventService
from services.user_service import UserService
from services.inscription_service import InscriptionService
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
    category_service = CategoryService()
    inscription_service = InscriptionService(user_service=user_service, event_service=event_service)

    # --- INÍCIO DA ALTERAÇÃO ---
    # Agora a função também entende o filtro de eventos gratuitos
    @app.route('/events')
    @view('event_list')
    def list_events():
        # Pega todos os parâmetros de filtro da URL
        search_query = request.query.get('query', '').strip()
        category_id = request.query.get('category_id', '').strip()
        location_filter = request.query.get('location', '').strip()
        time_filter = request.query.get('filter', '').strip()

        category_name_filter = ""
        title = "Todos os Eventos"

        # Define o título da página dinamicamente
        if category_id:
            category = category_service.get_by_id(category_id)
            if category:
                category_name_filter = category.name
                title = f"Eventos de: {category_name_filter}"
        elif location_filter:
            title = f"Eventos em: {location_filter}"
        elif time_filter == 'today':
            title = "Eventos de Hoje"
        elif time_filter == 'weekend':
            title = "Eventos do Fim de Semana"
        # --- NOVA CONDIÇÃO PARA O TÍTULO ---
        elif time_filter == 'free':
            title = "Eventos Gratuitos"

        # Usa o método de busca do serviço, que já entende todos os filtros
        events = event_service.search_events(
            query=search_query, 
            category=category_name_filter, 
            location=location_filter,
            time_filter=time_filter
        )
        
        # Busca todas as categorias e cidades para os dropdowns de filtro
        all_categories = category_service.get_all()
        all_locations = event_service.get_unique_locations()
        
        return dict(
            events=events,
            title=title,
            categories=all_categories,
            locations=all_locations,
            session=request.environ.get('beaker.session')
        )
    # --- FIM DA ALTERAÇÃO ---

    # Detalhes do evento, agora mostrando o preço
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

        remaining_slots = event.capacity - len(subscribers) if event else 0

        return dict(
            event=event,
            subscribers=subscribers,
            is_subscribed=is_subscribed,
            message=message,
            session=session,
            remaining_slots=remaining_slots
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

    # Mostrar formulário de novo evento com categorias e preço
    @app.route('/events/new', method='GET')
    @view('event_form')
    def new_event_form():
        session = request.environ.get('beaker.session')
        if not session.get('user_name'):
            return redirect('/login')
        
        all_categories = category_service.get_all()
        return dict(event=None, action='/events/new', error=None, session=session, categories=all_categories)

    # Criar novo evento com categorias, preço e validação
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
        price = (request.forms.get("price") or "0.0").strip()
        image_url = (request.forms.get("image_url") or "").strip()
        error, capacity = validate_event_data(name, date, location, capacity_raw)
        all_categories = category_service.get_all()

        if error:
            return template("event_form", event=None, action='/events/new', error=error, session=session, categories=all_categories)

        try:
            event_service.create(name, date, location, capacity, description, category, price)
        except Exception as e:
            print(f"Erro ao criar evento: {e}")
            return template("event_form", event=None, action='/events/new', error="Erro interno ao salvar o evento.", session=session, categories=all_categories)

        return redirect('/')

    # Mostrar formulário de edição com categorias e preço
    @app.route('/events/edit/<event_id:int>', method='GET')
    @view('event_form')
    def edit_event_form(event_id):
        session = request.environ.get('beaker.session')
        if not session.get('is_admin'):
            return redirect('/')

        event = event_service.get_by_id(event_id)
        all_categories = category_service.get_all()
        return dict(event=event, action=f'/events/edit/{event_id}', error=None, session=session, categories=all_categories)

    # Atualizar evento existente com categorias, preço e validação
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
            'category': request.forms.get("category"),
            'price': request.forms.get("price")
        }

        updated = event_service.update(event_id, data)
        all_categories = category_service.get_all()

        if not updated:
            return template(
                "event_form",
                event=event_service.get_by_id(event_id),
                action=f'/events/edit/{event_id}',
                error="Erro ao atualizar evento.",
                session=session,
                categories=all_categories
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
