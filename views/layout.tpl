<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agenda Cultural - {{title or 'Bem-vindo'}}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="/static/css/style.css" />
</head>
<body class="d-flex flex-column min-vh-100">
    <header>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark"> <div class="container-fluid">
                <a class="navbar-brand" href="/">Agenda Cultural</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item"><a class="nav-link" href="/events">Eventos</a></li>
                        <li class="nav-item"><a class="nav-link" href="/categories">Categorias</a></li>
                        <li class="nav-item"><a class="nav-link" href="/about">Sobre</a></li>
                        <li class="nav-item"><a class="nav-link" href="/contact">Contato</a></li>
                    </ul>
                    <ul class="navbar-nav ms-auto">
                        % if session and session.get('user_name'):
                            % if session.get('is_admin'):
                                <li class="nav-item me-2">
                                    <a href="/events/new" class="btn btn-primary">Cadastrar Evento</a>
                                </li>
                            % end
                            <li class="nav-item"><span class="nav-link nav-greeting">Olá, {{session.get('user_name')}}!</span></li>
                            <li class="nav-item"><a class="nav-link" href="/logout">Logout</a></li>
                        % else:
                            <li class="nav-item"><a class="nav-link" href="/login">Login</a></li>
                            <li class="nav-item"><a class="nav-link" href="/register">Cadastre-se</a></li>
                        % end
                    </ul>
                </div>
            </div>
        </nav>
    </header>

    <main class="container mt-4 flex-grow-1">
        {{!base}}
    </main>

    <footer class="site-footer">
        <div class="container">
            <div class="row">
                <div class="col-md-4 mb-4">
                    <h5><i class="fa-solid fa-calendar-days"></i> Agenda Cultural</h5>
                    <p>Conectando pessoas aos melhores eventos culturais da sua cidade. Descubra, participe e faça parte da cena cultural local.</p>
                    <div class="social-icons">
                        <a href="#"><i class="fab fa-instagram"></i></a>
                        <a href="#"><i class="fab fa-facebook-f"></i></a>
                        <a href="#"><i class="fab fa-twitter"></i></a>
                    </div>
                </div>
                <div class="col-md-2 col-6 mb-4">
                    <h5>Links Rápidos</h5>
                    <ul class="list-unstyled footer-links">
                        <li><a href="/events">Eventos</a></li>
                        <li><a href="/categories">Categorias</a></li>
                    </ul>
                </div>
                <div class="col-md-3 col-6 mb-4">
                    <h5>Categorias</h5>
                    <ul class="list-unstyled footer-links" id="footer-categories-list">
                        <li>Carregando...</li>
                    </ul>
                </div>
                <div class="col-md-3 mb-4">
                    <h5>Contato</h5>
                    <ul class="list-unstyled footer-links">
                        <li><i class="fas fa-map-marker-alt me-2"></i> Brasília - DF</li>
                        <li><i class="fas fa-phone me-2"></i> (61) 9999-9999</li>
                        <li><i class="fas fa-envelope me-2"></i> contato@agendacultural.com</li>
                    </ul>
                </div>
            </div>
            <hr style="border-color: #495057;">
            <div class="text-center">
                <p class="mb-0">&copy; 2025, Meu Projeto. Todos os direitos reservados.</p>
            </div>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            fetch('/api/categories')
                .then(response => response.json())
                .then(data => {
                    const categoriesList = document.getElementById('footer-categories-list');
                    const limitedData = data.slice(0, 5); // Limita a 5 categorias no rodapé
                    let categoriesHTML = '';
                    if (limitedData.length === 0) {
                        categoriesHTML = '<li>Nenhuma categoria.</li>';
                    } else {
                        limitedData.forEach(category => {
                            categoriesHTML += `<li><a href="/events?category_id=${category.id}">${category.name}</a></li>`;
                        });
                    }
                    categoriesList.innerHTML = categoriesHTML;
                })
                .catch(error => {
                    console.error('Erro ao buscar categorias para o rodapé:', error);
                    const categoriesList = document.getElementById('footer-categories-list');
                    categoriesList.innerHTML = '<li>Erro ao carregar.</li>';
                });
        });
    </script>
</body>
</html>