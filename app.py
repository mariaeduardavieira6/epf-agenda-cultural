from beaker.middleware import SessionMiddleware
from bottle import Bottle, run
from config import Config

class App:
    def __init__(self):
        self.bottle = Bottle()
        self.config = Config()

        
        session_opts = {
            'session.type': 'file',             
            'session.cookie_expires': 3600,     
            'session.data_dir': './data/sessions', 
            'session.auto': True
        }

        self.bottle = SessionMiddleware(self.bottle, session_opts)


    def setup_routes(self):
        from controllers import init_controllers

        init_controllers(self.bottle.app)


    
    def run(self):
        self.setup_routes()
        run(
            self.bottle, 
            host=self.config.HOST,
            port=self.config.PORT,
            debug=self.config.DEBUG,
            reloader=self.config.RELOADER
        )


def create_app():
    return App()