from . import user_controller

def init_controllers(app):
    user_controller.setup(app)