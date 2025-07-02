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
    <a href="/">Voltar para a lista</a>
</body>
</html>

