# Arquivo: app.py
import os
from beaker.middleware import SessionMiddleware
from bottle import Bottle, run, template, static_file, request, TEMPLATE_PATH

template_path = os.path.join(os.path.dirname(__file__), 'views')
TEMPLATE_PATH.insert(0, template_path)

class App:
    def __init__(self):
        self.bottle_app = Bottle()
        
        # Configurações básicas (host, porta, debug, reloader)
        self.HOST = 'localhost'
        self.PORT = 8080
        self.DEBUG = True
        self.RELOADER = True

        # Configuração da sessão
        session_opts = {
            'session.type': 'file',
            'session.cookie_expires': 3600,
            'session.data_dir': './data/sessions',
            'session.auto': True
        }
        self.app = SessionMiddleware(self.bottle_app, session_opts)

    def setup_routes(self):
        # Inicializa todos os seus controladores definidos em 'controllers/__init__.py'
        from controllers import init_controllers
        init_controllers(self.bottle_app)

        # Rota ÚNICA para servir arquivos estáticos (CSS, JS, imagens)
        @self.bottle_app.route('/static/<filepath:path>')
        def serve_static(filepath):
            return static_file(filepath, root='./static')

    def run(self):
        self.setup_routes()
        run(
            self.app,
            host=self.HOST,
            port=self.PORT,
            debug=self.DEBUG,
            reloader=self.RELOADER
        )

if __name__ == "__main__":
    app_instance = App()
    app_instance.run()