from bottle import route, view, request, redirect, static_file
from services.user_service import UserService

def setup(app):
    user_service = UserService()

    # Rotas de Cadastro
    @app.route('/register', method='GET')
    @view('user_form')
    def show_register_form():
        return dict(user=None, action='/register', session=request.environ.get('beaker.session'))

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
    @view('login')
    def show_login_form():
        error_message = "Email ou senha inválidos." if request.query.get('error') else None
        return dict(error=error_message, session=request.environ.get('beaker.session'))

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

    # Rota para Arquivos Estáticos (CSS, etc.)
    @app.route('/static/<filepath:path>')
    def server_static(filepath):
        return static_file(filepath, root='./static')