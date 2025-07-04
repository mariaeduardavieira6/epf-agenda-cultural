<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agenda Cultural - {{title or 'Bem-vindo'}}</title>
    <link rel="stylesheet" href="/static/css/style.css" />
</head>
<body>
    <header class="main-header">
        <nav class="main-nav">
            <a href="/" class="nav-brand">Agenda Cultural</a>

            <div class="nav-menu">
                <a href="/events" class="nav-link">Eventos</a>
                <a href="/categories" class="nav-link">Categorias</a>
                <a href="/about" class="nav-link">Sobre</a>
                <a href="/contact" class="nav-link">Contato</a>
            </div>
            
            <div class="nav-links">
                % if session and session.get('user_name'):
                    <!-- Este bloco verifica se o usuário é admin -->
                    % if session.get('is_admin'):
                        <a href="/events/new" class="nav-link button-primary">Cadastrar Evento</a>
                    % end
                
                    <span class="nav-greeting">Olá, {{session.get('user_name')}}!</span>
                    <a href="/logout" class="nav-link">Logout</a>
                % else:
                    <a href="/login" class="nav-link">Login</a>
                    <a href="/register" class="nav-link">Cadastre-se</a>
                % end
            </div>
        </nav>
    </header>
    <main class="container">
        {{!base}}
    </main>
    <footer class="main-footer">
        <p>&copy; 2025, Meu Projeto. Todos os direitos reservados.</p>
    </footer>
</body>
</html>