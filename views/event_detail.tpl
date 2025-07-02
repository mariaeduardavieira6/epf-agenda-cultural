<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Detalhes do Evento</title>
</head>
<body>
    <h1>{{event.name}}</h1>

    <p><strong>Descrição:</strong> {{event.description}}</p>
    <p><strong>Data:</strong> {{event.date}}</p>
    <p><strong>Local:</strong> {{event.location}}</p>
    <p><strong>Capacidade:</strong> {{event.capacity}}</p>

    <br>
    <a href="/events/edit/{{event.id}}">Editar</a> |
    <form action="/events/delete/{{event.id}}" method="post" style="display:inline;">
        <button type="submit" onclick="return confirm('Deseja realmente excluir este evento?')">Excluir</button>
    </form> |
    
% if session.get('is_admin'):
    <a href="/events/edit/{{event.id}}">Editar</a> |
    <form action="/events/delete/{{event.id}}" method="post" style="display:inline;">
        <button type="submit" onclick="return confirm('Deseja realmente cancelar este evento?')">Cancelar Evento</button>
    </form> |
% end

% if session.get('user_id'):
    % if not registration_service.is_user_registered(session.get('user_id'), event.id):
        <a href="/events/{{event.id}}/register">Inscrever-se neste evento</a>
    % else:
        <p>Você já está inscrito neste evento.</p>
    % end
% else:
    <p><a href="/login">Faça login</a> para se inscrever.</p>
% end

<a href="/">Voltar para a lista</a>
</body>
</html>

