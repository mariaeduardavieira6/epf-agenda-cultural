from . import user_controller

def init_controllers(app):
    # Agora chamamos a função 'setup' de dentro do user_controller,
    # passando a instância da aplicação para ele.
    user_controller.setup(app)