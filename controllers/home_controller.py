# controllers/home_controller.py

"""
Este controlador é responsável por renderizar a página inicial (homepage) do site.
"""

from bottle import view, request
# ALTERAÇÃO: Importando os serviços necessários
from services.category_service import CategoryService
from services.event_service import EventService
from services.user_service import UserService
from services.inscription_service import InscriptionService

 # Instanciando os serviços
category_service = CategoryService()
event_service = EventService() # <-- Novo serviço instanciado


def setup_home_routes(app):
    """Define a rota para a página inicial."""

    @app.route('/')
    @view('home') # Renderiza views\home.tpl
    def homepage():
        """Renderiza a página inicial e envia a lista de categorias e cidades."""
        session = request.environ.get('beaker.session')

        # ===== INÍCIO DA ALTERAÇÃO =====
        
        # Busca todas as categorias para o dropdown de busca
        all_categories = category_service.get_all()
        # Busca todas as cidades únicas para o dropdown de busca
        all_cities = event_service.get_unique_cities() # MUDOU DE get_unique_locations

        return dict(
            title="Bem-vindo",
            categories=all_categories,
            cities=all_cities, # MUDOU DE locations para cities
            session=request.environ.get('beaker.session')
        )
        # ===== FIM DA ALTERAÇÃO =====