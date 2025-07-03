from bottle import view, request, redirect, template
from services.user_service import UserService

def setup_auth_routes(app):
    """Configura as rotas de autenticação (login, logout, registro)."""
    
    user_service = UserService()

    @app.route('/register', method='GET')
    @view('register')
    def register_form():
        """Exibe o formulário de registro."""
        return dict(error=None, session=request.environ.get('beaker.session'))

    @app.route('/register', method='POST')
    def register_user():
        """Processa o envio do formulário de registro."""
        name = request.forms.get('name')
        email = request.forms.get('email')
        password = request.forms.get('password')
        birthdate = request.forms.get('birthdate')

        # Validação simples
        if not all([name, email, password, birthdate]):
            return template('register', error="Todos os campos são obrigatórios.", session=request.environ.get('beaker.session'))

        existing_user = user_service.get_by_email(email)
        if existing_user:
            return template('register', error="Este e-mail já está em uso.", session=request.environ.get('beaker.session'))
            
        # Cria o usuário (aqui você deveria fazer o hash da senha em um projeto real)
        user_service.create_user(name, email, password, birthdate)

        return redirect('/login')

    @app.route('/login', method='GET')
    @view('login')
    def login_form():
        """Exibe o formulário de login."""
        return dict(error=None, session=request.environ.get('beaker.session'))

    @app.route('/login', method='POST')
    def login_user():
        """Processa o envio do formulário de login."""
        email = request.forms.get('email')
        password = request.forms.get('password')
        
        user = user_service.get_by_email(email)

        # Validação do usuário e da senha
        if user and user.password == password: # Em um projeto real, compare o hash da senha
            session = request.environ.get('beaker.session')
            
            # --- PONTO CRÍTICO ---
            # Armazena as informações do usuário na sessão
            session['user_id'] = user.id
            session['user_name'] = user.name
            
            # Verifica se o usuário é um AdminUser para definir a permissão
            # Esta verificação assume que o seu modelo User tem um atributo 'is_admin' ou similar.
            # O plano de ação menciona uma classe AdminUser(User)[cite: 22].
            session['is_admin'] = getattr(user, 'is_admin', False) 
            
            session.save()
            return redirect('/')
        else:
            return template('login', error="E-mail ou senha inválidos.", session=request.environ.get('beaker.session'))

    @app.route('/logout')
    def logout_user():
        """Limpa a sessão do usuário e faz o logout."""
        session = request.environ.get('beaker.session')
        session.delete()
        return redirect('/')