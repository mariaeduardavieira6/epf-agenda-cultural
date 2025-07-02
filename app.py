# Arquivo: app.py
from beaker.middleware import SessionMiddleware
from bottle import Bottle, run
from config import Config

class App:
    def __init__(self):
        self.bottle = Bottle()
        self.config = Config()

        # Configuração da Sessão
        session_opts = {
            'session.type': 'file',
            'session.cookie_expires': 3600,
            'session.data_dir': './data/sessions',
            'session.auto': True
        }
        # "Envolve" nossa aplicação com o gerenciador de sessão
        self.bottle = SessionMiddleware(self.bottle, session_opts)

    def setup_routes(self):
        from controllers import init_controllers
        # Passa a aplicação de dentro da "caixa" da sessão para os controllers
        init_controllers(self.bottle.app)

    def run(self):
        self.setup_routes()
        # Roda o servidor com a aplicação "encapsulada" para a sessão funcionar
        run(
            self.bottle,
            host=self.config.HOST,
            port=self.config.PORT,
            debug=self.config.DEBUG,
            reloader=self.config.RELOADER
        )

def create_app():
    return App()

if __name__ == "__main__":
    app = App()
    app.run()
