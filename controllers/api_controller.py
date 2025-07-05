# controllers/api_controller.py

"""
Este controlador é responsável por expor rotas de API
para o frontend consumir dados como categorias e estatísticas.
"""

from bottle import response, view, request, template
import json

# Importa todos os serviços necessários
from services.event_service import EventService
from services.user_service import UserService
from services.category_service import CategoryService

# Instancia os serviços para que possamos usar seus métodos
event_service = EventService()
user_service = UserService()
category_service = CategoryService()

# Mapeamento de nomes de categoria para ícones emoji
category_icons_map = {
    "Música": "🎵",
    "Teatro": "🎭",
    "Exposição": "🖼️",
    "Curso": "📚",
    "Cinema": "🎬",
    "Dança": "💃",
    "Literatura": "✍️",
    "Arte": "🎨",
    "Gastronomia": "🍽️",
    "Esporte": "⚽"
}

def setup_api_routes(app):
    """Define as rotas de API e páginas no objeto da aplicação Bottle."""

    @app.get('/api/categories')
    def get_all_categories():
        """
        Endpoint para listar todas as categorias disponíveis.
        O frontend usará isso para popular os filtros e a seção de categorias.
        """
        categories = category_service.get_all()
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
            "cities": len(event_service.get_unique_locations()) 
        }
        
        response.content_type = 'application/json'
        return json.dumps(stats)
        
    # --- NOVA ROTA ADICIONADA AQUI ---
    @app.get('/api/featured-events')
    def get_featured_events():
        """
        Endpoint para buscar apenas os eventos marcados como destaque.
        """
        featured_events = event_service.get_featured_events()
        # Converte a lista de objetos Event para uma lista de dicionários
        events_dict = [event.to_dict() for event in featured_events]
        
        response.content_type = 'application/json'
        return json.dumps(events_dict)
    # --- FIM DA ALTERAÇÃO ---

    @app.get('/categories')
    @view('category_list')
    def page_categories():
        """
        Busca todas as categorias e as envia para o template 'category_list.tpl'
        para serem exibidas em uma página HTML.
        """
        all_categories = category_service.get_all()
        # Adiciona o ícone a cada objeto de categoria antes de passar para o template
        categories_with_icons = []
        for cat in all_categories:
            cat_dict = cat.to_dict() # Converte para dicionário se for um objeto
            cat_dict['icon'] = category_icons_map.get(cat_dict.get('name'), '❓') # '❓' como fallback
            categories_with_icons.append(cat_dict)

        return template('category_list', # Use template() diretamente
                        categories=categories_with_icons,
                        title="Todas as Categorias",
                        session=request.environ.get('beaker.session'))
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

    @app.get('/contact')
    @view('contact_page')
    def page_contact():
        """Renderiza a página de 'Contato'."""
        return dict(
            title="Contato",
            session=request.environ.get('beaker.session')
        )
