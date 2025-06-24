<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{{'Editar Evento' if event else 'Novo Evento'}}</title>
</head>
<body>
    <h1>{{'Editar Evento' if event else 'Criar Novo Evento'}}</h1>

    % if error:
        <p style="color:red;">{{error}}</p>
    % end

    <form action="{{'/events/' + event.id + '/edit' if event else '/events/new'}}" method="post">
        <label>Título:</label><br>
        <input type="text" name="title" value="{{event.title if event else ''}}"><br><br>

        <label>Descrição:</label><br>
        <textarea name="description">{{event.description if event else ''}}</textarea><br><br>

        <label>Data:</label><br>
        <input type="date" name="date" value="{{event.date if event else ''}}"><br><br>

        <label>Local:</label><br>
        <input type="text" name="location" value="{{event.location if event else ''}}"><br><br>

        <label>Capacidade:</label><br>
        <input type="number" name="capacity" value="{{event.capacity if event else ''}}"><br><br>

        <button type="submit">Salvar</button>
    </form>

    <p><a href="/events">Voltar para lista de eventos</a></p>
</body>
</html>
