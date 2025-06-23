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