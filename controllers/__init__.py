from . import user_controller
from . import event_controller

def init_controllers(app):
    user_controller.setup(app)
    event_controller.setup(app)