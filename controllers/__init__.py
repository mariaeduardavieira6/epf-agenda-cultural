from . import user_controller
from . import event_controller
from . import auth_controller  

def init_controllers(app):
    user_controller.setup(app)
    event_controller.setup(app)
    auth_controller.setup_auth_routes(app)  