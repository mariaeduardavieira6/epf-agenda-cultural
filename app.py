from beaker.middleware import SessionMiddleware
from bottle import Bottle, run
from config import Config

class App:
    def __init__(self):
        self.bottle_app = Bottle()
        self.config = Config()

        
        session_opts = {
            'session.type': 'file',             
            'session.cookie_expires': 3600,     
            'session.data_dir': './data/sessions', 
            'session.auto': True
        }

        self.bottle = SessionMiddleware(self.bottle_app, session_opts)


    def setup_routes(self):
        from controllers import init_controllers

        init_controllers(self.bottle_app)


    
    def run(self):
        self.setup_routes()
        run(
            self.bottle_app, 
            host=self.config.HOST,
            port=self.config.PORT,
            debug=self.config.DEBUG,
            reloader=self.config.RELOADER
        )


def create_app():
    return App()

if __name__ == "__main__":
    app = create_app()
    app.run()
