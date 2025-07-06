% rebase('layout.tpl', title='Agenda Cultural - Página Inicial', categories=categories, cities=cities)

<div class="hero-section text-center">
    <h1>Descubra a <span class="culture-text">Cultura</span> da sua Cidade</h1>
    <p>Encontre os melhores eventos culturais, conecte-se com artistas locais e faça parte de uma comunidade vibrante de amantes da cultura.</p>
    <a href="/events" class="btn btn-primary">Explorar Eventos</a>
    <a href="/about" class="btn btn-outline-light ms-3">Saiba Mais</a>
</div>
</section>

<section class="container stats-section mb-5">
    <div class="row" id="stats-container">
        <div class="col-12 text-center"><p>Carregando estatísticas...</p></div>
    </div>
</section>

<section class="container search-container">
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
            <label for="city" class="form-label">Cidade</label>
            <select name="city" id="city" class="form-select">
                <option value="">Todas</option>
                % for city in cities:
                    <option value="{{city}}">{{city}}</option>
                % end
            </select>
        </div>

        <div class="col-md-2">
            <button type="submit" class="btn btn-primary w-100">Buscar Eventos</button>
        </div>
    </form>
    <div class="quick-search">
        <span class="me-2">Busca rápida:</span>
        <a href="/events?time_filter=today" class="btn btn-outline-secondary btn-sm">Hoje</a>
        <a href="/events?time_filter=weekend" class="btn btn-outline-secondary btn-sm">Este fim de semana</a>
        <a href="/events?price_filter=free" class="btn btn-outline-secondary btn-sm">Gratuitos</a>
    </div>
</section>

<section class="container featured-events-section mb-5">
    <div class="text-center mb-4">
        <h2>Eventos em Destaque</h2>
        <p class="lead text-muted">Descubra os eventos mais populares e imperdíveis da temporada cultural</p>
    </div>
    <div class="row g-4" id="featured-events-container">
        <div class="col-12 text-center"><p>Carregando eventos em destaque...</p></div>
    </div>
</section>


<script>
    document.addEventListener('DOMContentLoaded', function() {
        // --- SCRIPT PARA BUSCAR E EXIBIR ESTATÍSTICAS ---
        fetch('/api/stats')
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                const statsContainer = document.getElementById('stats-container');
                statsContainer.innerHTML = `
                    <div class="col-md-3 col-6 mb-3"><div class="stat-item"><div class="stat-icon-box bg-events"><i class="fa-solid fa-calendar-days"></i></div><div class="stat-number">${data.events}+</div><div class="stat-label">Eventos</div></div></div>
                    <div class="col-md-3 col-6 mb-3"><div class="stat-item"><div class="stat-icon-box bg-cities"><i class="fa-solid fa-map-marker-alt"></i></div><div class="stat-number">${data.cities}</div><div class="stat-label">Cidades</div></div></div>
                    <div class="col-md-3 col-6 mb-3"><div class="stat-item"><div class="stat-icon-box bg-users"><i class="fa-solid fa-users"></i></div><div class="stat-number">${data.users}+</div><div class="stat-label">Usuários</div></div></div>
                    <div class="col-md-3 col-6 mb-3"><div class="stat-item"><div class="stat-icon-box bg-categories"><i class="fa-solid fa-tags"></i></div><div class="stat-number">${data.categories}+</div><div class="stat-label">Categorias</div></div></div>
                `;
            })
            .catch(error => {
                console.error('Erro ao buscar estatísticas:', error);
                const statsContainer = document.getElementById('stats-container');
                statsContainer.innerHTML = '<div class="col-12 text-center text-danger"><p>Erro ao carregar estatísticas.</p></div>';
            });
        
        // --- SCRIPT PARA BUSCAR E EXIBIR EVENTOS EM DESTAQUE ---
        fetch('/api/featured-events')
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                const featuredContainer = document.getElementById('featured-events-container');
                let featuredHTML = '';
                
                if (data.length === 0) {
                    featuredContainer.innerHTML = '<div class="col-12 text-center"><p>Nenhum evento em destaque no momento.</p></div>';
                    return;
                }

                data.forEach(event => {
                    const eventPrice = event.price > 0 ? `R$ ${event.price.toFixed(2).replace('.', ',')}` : 'Gratuito';
                    
                    const categoryIcon = event.category_icon ? event.category_icon : ''; 
                    
                    const imageUrl = event.image_url ? event.image_url : '/static/images/event-placeholder.jpg'; // Path local
                    
                    featuredHTML += `
                        <div class="col-md-6">
                            <a href="/events/${event.id}" class="featured-event-card">
                                <div class="card-img-container">
                                    <img src="${imageUrl}" class="card-img-top" alt="${event.name}">
                                    <span class="category-tag">${categoryIcon} ${event.category}</span>
                                </div>
                                <div class="card-body">
                                    <div class="event-info">
                                        <span><i class="fa-regular fa-calendar"></i> ${event.date}</span>
                                        <span><i class="fa-regular fa-clock"></i> ${event.time}</span>
                                        </div>
                                    <h5 class="card-title">${event.name}</h5>
                                    <p class="card-text">${event.description.substring(0, 100)}...</p>
                                    
                                    <p class="event-location"><i class="fa-solid fa-map-marker-alt"></i> ${event.city}</p>
                                    
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
                featuredContainer.innerHTML = '<div class="col-12 text-center text-danger"><p>Erro ao carregar eventos em destaque.</p></div>';
            });
    });
</script>