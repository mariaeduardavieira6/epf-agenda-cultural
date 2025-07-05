% rebase('layout.tpl', title='Página Inicial', categories=categories, locations=locations)

<style>
    /* Estilos para a homepage */
    .hero-section {
        background: #fdf8f5;
        padding: 60px 0;
        text-align: center;
        border-radius: 15px;
        margin-bottom: 40px;
    }
    .hero-section h1 {
        font-size: 3.5rem;
        font-weight: bold;
    }
    .hero-section .culture-text {
        color: #e67e22;
    }
    .stats-section .stat-item {
        text-align: center;
    }
    .stat-icon-box {
        width: 70px;
        height: 70px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 15px;
        font-size: 2rem;
        color: white;
    }
    .bg-events { background-color: #f8d7da; color: #721c24; }
    .bg-cities { background-color: #d4edda; color: #155724; }
    .bg-users { background-color: #cce5ff; color: #004085; }
    .bg-categories { background-color: #fce3e4; color: #e83e8c; }
    .stats-section .stat-number {
        font-size: 2.5rem;
        font-weight: bold;
    }
    .stats-section .stat-label {
        font-size: 1.1rem;
        color: #6c757d;
    }
    .search-container {
        background: white;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin-top: 50px;
        margin-bottom: 60px;
    }
    .quick-search {
        margin-top: 20px;
        text-align: center;
    }
    .quick-search .btn {
        margin: 0 5px;
    }

    /* Estilos para os cartões de destaque */
    .featured-event-card {
        border: 1px solid #e9ecef;
        border-radius: 15px;
        overflow: hidden;
        text-decoration: none;
        color: inherit;
        display: block;
        transition: box-shadow 0.3s ease;
    }
    .featured-event-card:hover {
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    .featured-event-card .card-img-container {
        position: relative;
    }
    .featured-event-card .category-tag {
        position: absolute;
        top: 15px;
        left: 15px;
        background-color: rgba(0, 0, 0, 0.5);
        color: white;
        padding: 5px 10px;
        border-radius: 20px;
        font-size: 0.8rem;
    }
    .featured-event-card .card-body {
        padding: 20px;
    }
    .featured-event-card .event-info {
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: #6c757d;
        font-size: 0.9rem;
        margin-bottom: 15px;
    }
    .featured-event-card .event-rating {
        color: #ffc107;
    }
    .featured-event-card .card-title {
        font-weight: bold;
        font-size: 1.25rem;
    }
    .featured-event-card .card-text {
        color: #6c757d;
    }
    .featured-event-card .event-location {
        color: #6c757d;
        font-size: 0.9rem;
        margin-top: 15px;
    }
    .featured-event-card .event-price {
        font-size: 1.5rem;
        font-weight: bold;
        color: var(--primary-color);
        margin-top: 20px;
    }
</style>

<!-- Seção Principal (Hero) -->
<div class="hero-section">
    <div class="container">
        <h1>Descubra a <span class="culture-text">Cultura</span> da sua Cidade</h1>
        <p class="lead">
            Encontre os melhores eventos culturais, conecte-se com artistas locais e faça parte de uma comunidade vibrante de amantes da cultura.
        </p>
    </div>
</div>

<!-- Seção de Estatísticas com Ícones -->
<div class="container stats-section mb-5">
    <div class="row" id="stats-container">
        <div class="col-md-3"><p>Carregando estatísticas...</p></div>
    </div>
</div>

<!-- INÍCIO DA ALTERAÇÃO: A ordem das secções foi trocada -->

<!-- Seção de Busca -->
<div class="container search-container">
    <h2 class="text-center mb-4">Encontre seu próximo evento cultural</h2>
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
            <label for="location" class="form-label">Local</label>
            <select name="location" id="location" class="form-select">
                <option value="">Todos</option>
                % for loc in locations:
                    <option value="{{loc}}">{{loc}}</option>
                % end
            </select>
        </div>
        <div class="col-md-2">
            <button type="submit" class="btn btn-primary w-100" style="background-color: #e67e22; border-color: #e67e22;">Buscar Eventos</button>
        </div>
    </form>
    <div class="quick-search">
        <span class="me-2">Busca rápida:</span>
        <a href="/events?filter=today" class="btn btn-outline-secondary btn-sm">Hoje</a>
        <a href="/events?filter=weekend" class="btn btn-outline-secondary btn-sm">Este fim de semana</a>
        <a href="/events?filter=free" class="btn btn-outline-secondary btn-sm">Gratuitos</a>
    </div>
</div>

<!-- Secção de Eventos em Destaque -->
<div class="container mb-5">
    <div class="text-center mb-4">
        <h2>Eventos em Destaque</h2>
        <p class="lead text-muted">Descubra os eventos mais populares e imperdíveis da temporada cultural</p>
    </div>
    <div class="row g-4" id="featured-events-container">
        <!-- Os cartões de evento em destaque serão inseridos aqui pelo JavaScript -->
        <div class="col-12"><p>Carregando eventos em destaque...</p></div>
    </div>
</div>

<!-- FIM DA ALTERAÇÃO -->


<script>
    document.addEventListener('DOMContentLoaded', function() {
        
        // Busca e exibe as estatísticas com ícones
        fetch('/api/stats')
            .then(response => response.json())
            .then(data => {
                const statsContainer = document.getElementById('stats-container');
                statsContainer.innerHTML = `
                    <div class="col-md-3 col-6 mb-3"><div class="stat-item"><div class="stat-icon-box bg-events"><i class="fa-solid fa-calendar-days"></i></div><div class="stat-number">${data.events}+</div><div class="stat-label">Eventos</div></div></div>
                    <div class="col-md-3 col-6 mb-3"><div class="stat-item"><div class="stat-icon-box bg-cities"><i class="fa-solid fa-map-marker-alt"></i></div><div class="stat-number">${data.cities}</div><div class="stat-label">Cidades</div></div></div>
                    <div class="col-md-3 col-6 mb-3"><div class="stat-item"><div class="stat-icon-box bg-users"><i class="fa-solid fa-users"></i></div><div class="stat-number">${(data.users / 1000).toFixed(1)}K+</div><div class="stat-label">Usuários</div></div></div>
                    <div class="col-md-3 col-6 mb-3"><div class="stat-item"><div class="stat-icon-box bg-categories"><i class="fa-solid fa-star"></i></div><div class="stat-number">${data.categories}+</div><div class="stat-label">Categorias</div></div></div>
                `;
            });
        
        // --- SCRIPT PARA BUSCAR E EXIBIR EVENTOS EM DESTAQUE ---
        fetch('/api/featured-events')
            .then(response => response.json())
            .then(data => {
                const featuredContainer = document.getElementById('featured-events-container');
                let featuredHTML = '';
                
                if (data.length === 0) {
                    featuredContainer.innerHTML = '<p class="text-center">Nenhum evento em destaque no momento.</p>';
                    return;
                }

                data.forEach(event => {
                    const eventPrice = event.price > 0 ? `R$ ${event.price.toFixed(2)}` : 'Gratuito';
                    
                    featuredHTML += `
                        <div class="col-md-6">
                            <a href="/events/${event.id}" class="featured-event-card">
                                <div class="card-img-container">
                                    <img src="${event.image_url}" class="card-img-top" alt="${event.name}" style="height: 250px; object-fit: cover;">
                                    <span class="category-tag">${event.category}</span>
                                </div>
                                <div class="card-body">
                                    <div class="event-info">
                                        <span><i class="fa-regular fa-calendar"></i> ${event.date}</span>
                                        <span><i class="fa-regular fa-clock"></i> ${event.time}</span>
                                        <span class="event-rating"><i class="fa-solid fa-star"></i> ${event.rating}</span>
                                    </div>
                                    <h5 class="card-title">${event.name}</h5>
                                    <p class="card-text">${event.description.substring(0, 100)}...</p>
                                    <p class="event-location"><i class="fa-solid fa-map-marker-alt"></i> ${event.location}</p>
                                    <div class="event-price">${eventPrice}</div>
                                </div>
                            </a>
                        </div>
                    `;
                });
                featuredContainer.innerHTML = featuredHTML;
            })
            .catch(error => {
                console.error('Erro ao buscar eventos em destaque:', error);
                const featuredContainer = document.getElementById('featured-events-container');
                featuredContainer.innerHTML = '<p class="text-center text-danger">Erro ao carregar eventos em destaque.</p>';
            });
    });
</script>
