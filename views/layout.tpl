<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agenda Cultural - {{title or 'Bem-vindo'}}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9Oer-2Mng7peFpQh-E5Hq2z1i2hL1oVn/eQ8Jz3L1p5S2z" crossorigin="anonymous">
    <link rel="stylesheet" href="/static/css/style.css" />
</head>
<body>
    <header>
        <nav class="navbar navbar-expand-lg" style="background-color: var(--cosmos-blue);">
            <div class="container-fluid">
                <a class="navbar-brand text-white" href="/">Agenda Cultural</a>

                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ms-auto">
% if session and session.get('user_name'):
                        <li class="nav-item">
                            <span class="nav-link text-white">Olá, {{session.get('user_name')}}!</span>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link text-white" href="/logout">Logout</a>
                        </li>
% else:
                        <li class="nav-item">
                            <a class="nav-link text-white" href="/login">Login</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link text-white" href="/register">Cadastre-se</a>
                        </li>
% end
                    </ul>
                </div>
            </div>
        </nav>
    </header>
    <main class="container">
        {{!base}}
    </main>
    <footer class="main-footer">
        <p>&copy; 2025, Meu Projeto. Todos os direitos reservados.</p>
    </footer>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-SL3tL4LqM+rMh9l8lH9l1P2oK2pL4lV2j5D2C5Q7C5V8C9V0P1J5T7N7L7L7L7L" crossorigin="anonymous"></script>
    </body>
</html>