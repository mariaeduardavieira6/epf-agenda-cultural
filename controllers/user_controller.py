
from bottle import route, view, request, redirect
from services.user_service import UserService

def setup(app):
    user_service = UserService()

    @app.route('/register', method='GET')
    @view('user_form')
    def show_register_form():
        return dict(
            user=None,
            action='/register'
        )

    @app.route('/register', method='POST')
    def process_register_form():
        name = request.forms.get('name')
        email = request.forms.get('email')
        password = request.forms.get('password')
        birthdate = request.forms.get('birthdate')

        user_service.create_user(name, email, password, birthdate)
        
        print(f"Usuário '{name}' cadastrado com sucesso. Redirecionando para /login.")
        redirect('/login')

    
    @app.route('/login', method='GET')
    @view('login')
    def show_login_form():
        return {}

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

            print(f"Sessão criada para o usuário: {user.name}")
            redirect('/') 
        else:
            print("Falha no login: email ou senha incorretos.")
            redirect('/login')

    @app.route('/logout')
    def logout_user():
        session = request.environ.get('beaker.session')
        session.delete() 
        redirect('/login')