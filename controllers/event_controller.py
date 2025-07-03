from bottle import view, request, redirect, template
from services.event_service import EventService
from services.user_service import UserService
from services.inscription_service import InscriptionService

# --- Função de Validação  ---
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
    # NOVO: Instanciar o InscriptionService, passando os outros serviços para ele
    inscription_service = InscriptionService(user_service=user_service, event_service=event_service)

    # Rota da página inicial: Lista de Eventos (sem alterações)
    @app.route('/')
    @view('event_list')
    def list_events():
        events = event_service.get_all()
        return dict(
            events=events,
            session=request.environ.get('beaker.session')
        )

    # MODIFICADO: Rota para ver detalhes de um evento específico
    # Agora ela também busca os inscritos e verifica se o usuário atual está inscrito.
    @app.route('/events/<event_id:int>')
    @view('event_detail')
    def event_detail(event_id):
        session = request.environ.get('beaker.session')
        event = event_service.get_by_id(event_id)
        
        # NOVO: Lógica de Inscrição
        subscribers = inscription_service.get_subscribers_by_event(event_id)
        user_id = session.get('user_id') # Importante: seu login precisa salvar o user_id na sessão!
        is_subscribed = False
        if user_id:
            is_subscribed = inscription_service.is_user_subscribed(user_id, event_id)

        # NOVO: Lógica para exibir mensagens de sucesso/erro (ex: "Inscrição realizada!")
        message = session.pop('message', None) # Pega a mensagem da sessão e a remove

        return dict(
            event=event,
            subscribers=subscribers,
            is_subscribed=is_subscribed,
            message=message, # Envia a mensagem para o template
            session=session
        )

    # NOVO: Rota para INSCREVER um usuário em um evento
    @app.route('/events/<event_id>/subscribe', method='POST')
    def subscribe_to_event(event_id):
        session = request.environ.get('beaker.session')
        user_id = session.get('user_id')

        # Proteção: Apenas usuários logados podem se inscrever
        if not user_id:
            return redirect('/login')
        
        # Tenta inscrever o usuário usando o serviço
        result = inscription_service.subscribe_user_to_event(user_id, int(event_id))

        # Guarda a mensagem (sucesso ou erro) na sessão para exibi-la na página
        session['message'] = result['message']
        session.save() # Salva a sessão após a modificação

        # Redireciona de volta para a página de detalhes do evento
        return redirect(f'/events/{event_id}')

    # NOVO: Rota para CANCELAR a inscrição de um usuário
    @app.route('/events/<event_id>/unsubscribe', method='POST')
    def unsubscribe_from_event(event_id):
        session = request.environ.get('beaker.session')
        user_id = session.get('user_id')

        # Proteção: Apenas usuários logados podem cancelar
        if not user_id:
            return redirect('/login')

        # Tenta cancelar a inscrição
        result = inscription_service.cancel_subscription(user_id, int(event_id))

        # Guarda a mensagem na sessão
        session['message'] = result['message']
        session.save()

        # Redireciona de volta para a página de detalhes do evento
        return redirect(f'/events/{event_id}')

    # Rota para mostrar o formulário de criação (sem alterações)
    @app.route('/events/new', method='GET')
    @view('event_form')
    def new_event_form():
        session = request.environ.get('beaker.session')
        if not session.get('user_name'):
            return redirect('/login')
        
        return dict(
            event=None,
            action='/events/new',
            error=None,
            session=session
        )

    # Rota para processar a criação de um novo evento (sem alterações)
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

        error, capacity = validate_event_data(name, date, location, capacity_raw)

        if error:
            return template("event_form", event=None, action='/events/new', error=error, session=session)

        try:
            event_service.create(name, date, location, capacity, description)
        except Exception as e:
            print(f"Erro ao criar evento: {e}")
            return template("event_form", event=None, action='/events/new', error="Erro interno ao salvar o evento.", session=session)

        redirect('/')
        
    # Rota para mostrar o formulário de EDIÇÃO (sem alterações)
    @app.route('/events/edit/<event_id:int>', method='GET')
    @view('event_form')
    def edit_event_form(event_id):
        session = request.environ.get('beaker.session')
        if not session.get('is_admin'):
            return redirect('/')

        event = event_service.get_by_id(event_id)
        return dict(
            event=event,
            action=f'/events/edit/{event_id}',
            error=None,
            session=session
        )

    # Rota para processar a ATUALIZAÇÃO de um evento (sem alterações)
    @app.route('/events/edit/<event_id:int>', method='POST')
    def update_event(event_id):
        session = request.environ.get('beaker.session')
        if not session.get('is_admin'):
            return redirect('/')
        
        # TODO: Adicionar a lógica de atualização no EventService e chamá-la aqui
        print(f"Lógica de ATUALIZAR para o evento {event_id} virá aqui.")
        redirect(f'/events/{event_id}')

    # Rota para DELETAR um evento (sem alterações)
    @app.route('/events/delete/<event_id:int>', method='POST')
    def delete_event(event_id):
        session = request.environ.get('beaker.session')
        if not session.get('is_admin'):
            return redirect('/')
        
        event_service.delete(event_id)
        redirect('/')