<!DOCTYPE html>
<html>
<head>
    <title>Lista de Eventos</title>
</head>
<body>
    <h1>Eventos Cadastrados</h1>

    % if events:
        <ul>
        % for event in events:
            <li>
                <strong>{{event.title}}</strong><br>
                Data: {{event.date}}<br>
                Local: {{event.location}}<br>
                <a href="/events/{{event.title}}">Ver detalhes</a> |
                <a href="/events/{{event.title}}/edit">Editar</a> |
                <a href="/events/{{event.title}}/delete">Excluir</a>
            </li>
        % end
        </ul>
    % else:
        <p>Nenhum evento cadastrado ainda.</p>
    % end

    <br>
    <a href="/events/new">Criar novo evento</a>
</body>
</html>
