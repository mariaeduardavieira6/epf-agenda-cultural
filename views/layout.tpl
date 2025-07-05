<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agenda Cultural - {{title or 'Bem-vindo'}}</title>
    <!-- CSS do Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- ALTERAÇÃO: Adicionando a biblioteca de ícones Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <!-- Seu CSS personalizado -->
    <link rel="stylesheet" href="/static/css/style.css" />
</head>
<body>
    <header>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container-fluid">
                <a class="navbar-brand" href="/">Agenda Cultural</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <!-- Links de Navegação Principal -->
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link" href="/events">Eventos</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/categories">Categorias</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/about">Sobre</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="/contact">Contato</a>
                        </li>
                    </ul>

                    <!-- Links de Usuário e Admin à Direita -->
                    <ul class="navbar-nav ms-auto">
                        % if session and session.get('user_name'):
                            % if session.get('is_admin'):
                                <li class="nav-item">
                                    <a href="/events/new" class="btn btn-primary">Cadastrar Evento</a>
                                </li>
                            % end
                            <li class="nav-item">
                                <span class="nav-link">Olá, {{session.get('user_name')}}!</span>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="/logout">Logout</a>
                            </li>
                        % else:
                            <li class="nav-item">
                                <a class="nav-link" href="/login">Login</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="/register">Cadastre-se</a>
                            </li>
                        % end
                    </ul>
                </div>
            </div>
        </nav>
    </header>

    <main class="container mt-4">
        {{!base}}
    </main>

    <footer class="footer mt-auto py-3 bg-light">
        <div class="container text-center">
            <span class="text-muted">&copy; 2025, Meu Projeto. Todos os direitos reservados.</span>
        </div>
    </footer>

    <!-- JavaScript do Bootstrap -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
