% rebase('layout.tpl', title='Eventos', categories=categories, cities=cities)

<style>
    /* Estilo para os botões de busca rápida */
    .quick-search {
        margin-top: 20px;
        text-align: center;
    }
    .quick-search .btn {
        margin: 0 5px;
    }

    /* Novos estilos para os cards de eventos */
    .event-card {
        background-color: var(--white);
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        height: 100%;
        display: flex;
        flex-direction: column;
        overflow: hidden;
        position: relative;
    }

    .event-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
    }

    .event-card-img {
        width: 100%;
        height: 180px;
        object-fit: cover;
        border-top-left-radius: 12px;
        border-top-right-radius: 12px;
    }

    .event-card-body {
        padding: 1.5rem;
        flex-grow: 1;
        display: flex;
        flex-direction: column;
    }

    .event-card-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: var(--cosmos-blue);
        margin-bottom: 0.75rem;
    }

    .event-card-meta {
        font-size: 0.95rem;
        color: var(--blue-marble);
        margin-bottom: 0.5rem;
    }

    .event-card-description {
        font-size: 1rem;
        color: var(--cosmos-blue);
        line-height: 1.5;
        margin-bottom: 1rem;
        flex-grow: 1;
    }

    .event-card-footer {
        padding: 1rem 1.5rem;
        border-top: 1px solid rgba(0, 48, 73, 0.05);
        background-color: var(--light-beige);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .event-card-actions {
        display: flex;
        align-items: center; /* Alinha o link "Ver detalhes" e os botões */
        gap: 0.75rem;      /* Adiciona um espaço consistente entre os itens */
    }

    .event-card-price {
        font-weight: 700;
        color: var(--crimson-blaze);
        font-size: 1.1rem;
    }

    .event-card-link {
        color: var(--crimson-blaze);
        font-weight: 600;
        text-decoration: none;
        transition: color 0.3s ease;
    }

    .event-card-link:hover {
        color: var(--gochujang-red);
    }

    .admin-actions .btn {
        margin-right: 0.5rem;
    }
</style>

<h1 class="display-4 fw-bold mb-4 text-center text-cosmos-blue">{{ title or 'Eventos Cadastrados' }}</h1>

<div class="search-bar card mb-4 shadow-sm">
    <div class="card-body">
        <form action="/events" method="GET" class="row g-3 align-items-end">
            <div class="col-md-4">
                <label for="query" class="form-label">O que você procura?</label>
                <input type="text" name="query" id="query" class="form-control" placeholder="Nome do evento...">
            </div>
            <div class="col-md-3">
                <label for="category_id" class="form-label">Categoria</label>
                <select name="category_id" id="category_id" class="form-select">
                    <option value="">Todas</option>
                    % for cat in categories:
                        <option value="{{cat.id}}">{{cat.name}}</option>
                    % end
                </select>
            </div>
            
            <div class="col-md-3">
                <label for="city" class="form-label">Cidade</label>
                <select name="city" id="city" class="form-select">
                    <option value="">Todas</option>
                    % for city in cities:
                        <option value="{{city}}">{{city}}</option>
                    % end
                </select>
            </div>
            
            <div class="col-md-2">
                <button type="submit" class="btn btn-primary w-100">Buscar</button>
            </div>
        </form>

        <div class="quick-search">
            <span class="me-2">Busca rápida:</span>
            <a href="/events?filter=today" class="btn btn-outline-secondary btn-sm">Hoje</a>
            <a href="/events?filter=weekend" class="btn btn-outline-secondary btn-sm">Este fim de semana</a>
            <a href="/events?filter=free" class="btn btn-outline-secondary btn-sm">Gratuitos</a>
        </div>
    </div>
</div>


% if not events:
    <p class="text-center text-muted mt-5">Nenhum evento encontrado.</p>
% else:
    <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
    % for event in events:
        <div class="col">
            <div class="event-card shadow">
                
                % if event.image_url:
                    <img src="{{event.image_url}}" class="event-card-img" alt="Imagem de {{event.name}}">
                % else:
                    <img src="/static/images/default-event.jpg" class="event-card-img" alt="Evento sem imagem">
                % end

                <div class="event-card-body">
                    <h3 class="event-card-title">{{event.name}}</h3>
                    <p class="event-card-meta">
                        🗓️ {{event.date}} <br>
                        📍 {{event.city}} <br>
                        Categoría: {{event.category}}
                    </p>
                    <p class="event-card-description">
                        {{event.description[:100] + '...' if len(event.description) > 100 else event.description}}
                    </p>
                </div>

                <div class="event-card-footer">
                    <span class="event-card-price">
                        % if event.price > 0:
                            R$ {{ '%.2f' % event.price }}
                        % else:
                            Gratuito
                        % end
                    </span>
                    
                    <div class="event-card-actions"> 
                        <a href="/events/{{event.id}}" class="event-card-link">Ver detalhes</a>

                        % if session and session.get('is_admin'):
                            <a href="/events/edit/{{event.id}}" class="btn btn-sm btn-warning">Editar</a>
                            <form action="/events/delete/{{event.id}}" method="POST" style="display: inline;" onsubmit="return confirm('Tem certeza que deseja excluir este evento?');">
                                <button type="submit" class="btn btn-sm btn-danger">Excluir</button>
                            </form>
                        % end
                    </div>
                </div>
            </div>
        </div>
    % end
    </div>
% end

% if session and session.get('is_admin'):
    <div class="text-center mt-5 mb-4">
        <a href="/events/new" class="btn btn-primary btn-lg">Criar Novo Evento</a>
    </div>
% end