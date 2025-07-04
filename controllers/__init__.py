# controllers/__init__.py

from . import user_controller
from . import event_controller
from . import auth_controller
from . import api_controller  # <-- 1. IMPORTAR O NOVO CONTROLADOR

def init_controllers(app):
    user_controller.setup(app)
    event_controller.setup(app)
    auth_controller.setup_auth_routes(app)
    api_controller.setup_api_routes(app)  # <-- 2. INICIALIZAR AS NOVAS ROTAS