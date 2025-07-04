# controllers/api_controller.py

"""
Este controlador é responsável por expor rotas de API
para o frontend consumir dados como categorias e estatísticas.
"""

from bottle import response, view, request
import json

# Importa todos os serviços necessários
from services.event_service import EventService
from services.user_service import UserService
from services.category_service import CategoryService

# Instancia os serviços para que possamos usar seus métodos
event_service = EventService()
user_service = UserService()
category_service = CategoryService()

def setup_api_routes(app):
    """Define as rotas de API e páginas no objeto da aplicação Bottle."""

    @app.get('/api/categories')
    def get_all_categories():
        """
        Endpoint para listar todas as categorias disponíveis.
        O frontend usará isso para popular os filtros e a seção de categorias.
        """
        categories = category_service.get_all()
        # Converte a lista de objetos Category para uma lista de dicionários
        categories_dict = [cat.to_dict() for cat in categories]
        
        response.content_type = 'application/json'
        return json.dumps(categories_dict)

    @app.get('/api/stats')
    def get_site_stats():
        """
        Endpoint para buscar as estatísticas principais do site,
        como número de eventos, usuários e categorias.
        """
        stats = {
            "events": event_service.get_total_count(),
            "users": user_service.get_total_count(),
            "categories": category_service.get_all().__len__(),
            "cities": 12 # Valor fixo por enquanto
        }
        
        response.content_type = 'application/json'
        return json.dumps(stats)

    @app.get('/categories')
    @view('category_list')
    def page_categories():
        """
        Busca todas as categorias e as envia para o template 'category_list.tpl'
        para serem exibidas em uma página HTML.
        """
        all_categories = category_service.get_all()
        return dict(
            categories=all_categories,
            title="Todas as Categorias", # Título da página
            session=request.environ.get('beaker.session')
        )

    @app.get('/about')
    @view('about_page')
    def page_about():
        """Renderiza a página 'Sobre Nós'."""
        return dict(
            title="Sobre Nós",
            session=request.environ.get('beaker.session')
        )

    # --- ROTA FINAL ADICIONADA AQUI ---
    @app.get('/contact')
    @view('contact_page') # Usará um novo template chamado contact_page.tpl
    def page_contact():
        """Renderiza a página de 'Contato'."""
        return dict(
            title="Contato",
            session=request.environ.get('beaker.session')
        )
