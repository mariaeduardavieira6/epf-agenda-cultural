% rebase('layout.tpl', title='Página Inicial', categories=categories, locations=locations)

<style>
    /* Estilos para a homepage */
    .hero-section {
        background: #fdf8f5; /* Fundo levemente alaranjado/rosado */
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
        color: #e67e22; /* Laranja mais forte */
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
            <!-- ALTERAÇÃO AQUI: Trocando 'Cidade' por 'Local' -->
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
</div>


<script>
    document.addEventListener('DOMContentLoaded', function() {
        
        // Busca e exibe as estatísticas com ícones
        fetch('/api/stats')
            .then(response => response.json())
            .then(data => {
                const statsContainer = document.getElementById('stats-container');
                statsContainer.innerHTML = `
                    <div class="col-md-3 col-6 mb-3">
                        <div class="stat-item">
                            <div class="stat-icon-box bg-events"><i class="fa-solid fa-calendar-days"></i></div>
                            <div class="stat-number">${data.events}+</div>
                            <div class="stat-label">Eventos</div>
                        </div>
                    </div>
                    <div class="col-md-3 col-6 mb-3">
                        <div class="stat-item">
                            <div class="stat-icon-box bg-cities"><i class="fa-solid fa-map-marker-alt"></i></div>
                            <div class="stat-number">${data.cities}</div>
                            <div class="stat-label">Cidades</div>
                        </div>
                    </div>
                    <div class="col-md-3 col-6 mb-3">
                        <div class="stat-item">
                            <div class="stat-icon-box bg-users"><i class="fa-solid fa-users"></i></div>
                            <div class="stat-number">${(data.users / 1000).toFixed(1)}K+</div>
                            <div class="stat-label">Usuários</div>
                        </div>
                    </div>
                    <div class="col-md-3 col-6 mb-3">
                        <div class="stat-item">
                            <div class="stat-icon-box bg-categories"><i class="fa-solid fa-star"></i></div>
                            <div class="stat-number">${data.categories}+</div>
                            <div class="stat-label">Categorias</div>
                        </div>
                    </div>
                `;
            });
    });
</script>
>>>>>>> 85bc4e06a4b63ccf3e8b27bb9643b3694c476ec3
