# controllers/user_controller.py
from bottle import route, template, request, redirect, static_file 
from services.user_service import UserService


# Dados das Categorias (para a página inicial)
category_data_for_template = [
    {'key': 'musica', 'label': 'Música', 'icon': '🎵'},
    {'key': 'teatro', 'label': 'Teatro', 'icon': '🎭'},
    {'key': 'exposicao', 'label': 'Exposição', 'icon': '🖼️'},
    {'key': 'curso', 'label': 'Curso', 'icon': '📚'},
    {'key': 'cinema', 'label': 'Cinema', 'icon': '🎬'},
    {'key': 'danca', 'label': 'Dança', 'icon': '💃'},
    {'key': 'literatura', 'label': 'Literatura', 'icon': '✍️'},
    {'key': 'arte', 'label': 'Arte', 'icon': '🎨'}
]

def setup(app):
    user_service = UserService()

    # --- NOVA ROTA: Página Inicial (/) ---
    @app.route('/')
    def home_page():
        current_session = request.environ.get('beaker.session')
        user_name = current_session.get('user_name', None) if current_session else None
        
        return template('home', 
                        categories=category_data_for_template, 
                        title="Início", 
                        user_name=user_name)

    # Rotas de Cadastro
    @app.route('/register', method='GET')
    def show_register_form():
        return template('user_form', user=None, action='/register', session=request.environ.get('beaker.session'))

    @app.route('/register', method='POST')
    def process_register_form():
        name = request.forms.get('name')
        email = request.forms.get('email')
        password = request.forms.get('password')
        birthdate = request.forms.get('birthdate')
        user_service.create_user(name, email, password, birthdate)
        redirect('/login')
    
    # Rotas de Login
    @app.route('/login', method='GET')
    def show_login_form():
        error_message = "Email ou senha inválidos." if request.query.get('error') else None
        return template('login', error=error_message, session=request.environ.get('beaker.session'))

    @app.route('/login', method='POST')
    def process_login():
        email = request.forms.get('email')
        password = request.forms.get('password')
        user = user_service.get_by_email(email)
        if user and user.password == password:
            session = request.environ.get('beaker.session')
            session['user_id'] = user.id
            session['user_name'] = user.name
            session['is_admin'] = user.is_admin
            session.save()
            redirect('/')
        else:
            redirect('/login?error=1')
            
    # Rota de Logout
    @app.route('/logout')
    def logout_user():
        session = request.environ.get('beaker.session')
        session.delete()
        redirect('/login')
    
    # Rota para Página de Administração - lista de usuários
    @app.route('/adm/users')
    def admin_users():
        session = request.environ.get('beaker.session')
        if not session.get('is_admin'):
            return redirect('/')
        users = user_service.get_all() 
        return template('admin_users', users=users, session=session)

    # Rota para remover inscrições de usuário no evento (admin)
    @app.route('/adm/users/<user_id:int>/remove_registration/<event_id:int>', method='POST')
    def remove_registration(user_id, event_id):
        session = request.environ.get('beaker.session')
        if not session.get('is_admin'):
            return redirect('/')
        redirect('/adm/users')