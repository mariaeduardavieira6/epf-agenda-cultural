<!DOCTYPE html>
<html>
<head>
    <title>Detalhes do Evento</title>
</head>
<body>
    <h1>{{event.title}}</h1>

    <p><strong>Descrição:</strong> {{event.description}}</p>
    <p><strong>Data:</strong> {{event.date}}</p>
    <p><strong>Local:</strong> {{event.location}}</p>
    <p><strong>Capacidade:</strong> {{event.capacity}}</p>

    <br>
    <a href="/events/{{event.title}}/edit">Editar</a> |
    <a href="/events/{{event.title}}/delete">Excluir</a> |
    <a href="/events">Voltar para a lista</a>
</body>
</html>
