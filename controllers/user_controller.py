# controllers/user_controller.py
from bottle import template, request, redirect
from services.user_service import UserService

def setup(app):
    user_service = UserService()

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
    # Nota: A lógica desta rota precisa ser implementada no InscriptionService
    @app.route('/adm/users/<user_id:int>/remove_registration/<event_id:int>', method='POST')
    def remove_registration(user_id, event_id):
        session = request.environ.get('beaker.session')
        if not session.get('is_admin'):
            return redirect('/')
        # A lógica de remoção da inscrição deve ser chamada aqui
        redirect('/adm/users')
