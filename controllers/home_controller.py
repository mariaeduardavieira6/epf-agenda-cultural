# controllers/home_controller.py

"""
Este controlador é responsável por renderizar a página inicial (homepage) do site.
"""

from bottle import view, request
# ALTERAÇÃO: Importando os serviços necessários
from services.category_service import CategoryService
from services.event_service import EventService

def setup_home_routes(app):
    """Define a rota para a página inicial."""
    
    # Instanciando os serviços
    category_service = CategoryService()
    event_service = EventService() # <-- Novo serviço instanciado

    @app.route('/')
    @view('home')
    def homepage():
        """Renderiza a página inicial e envia a lista de categorias e cidades."""
        
        # Busca todas as categorias para o dropdown de busca
        all_categories = category_service.get_all()
        # Busca todas as cidades únicas para o dropdown de busca
        all_locations = event_service.get_unique_locations() # <-- Nova linha
        
        return dict(
            title="Bem-vindo",
            categories=all_categories,
            locations=all_locations, # <-- Enviando a lista de cidades
            session=request.environ.get('beaker.session')
        )
