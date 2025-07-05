# controllers/__init__.py

from . import user_controller
from . import event_controller
from . import auth_controller
from . import api_controller
from . import home_controller  # <-- 1. IMPORTA O NOVO CONTROLADOR

def init_controllers(app):
    # A rota da homepage deve ser registrada primeiro
    home_controller.setup_home_routes(app) # <-- 2. INICIALIZA A HOMEPAGE
    
    user_controller.setup(app)
    event_controller.setup(app)
    auth_controller.setup_auth_routes(app)
    api_controller.setup_api_routes(app)
