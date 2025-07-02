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

    <form action="{{'/events/edit/' + str(event.id) if event else '/events/new'}}" method="post">
        <label>Nome do Evento:</label><br>
        <input type="text" name="name" value="{{event.name if event else ''}}" required><br><br>

        <label>Descrição:</label><br>
        <textarea name="description" required>{{event.description if event else ''}}</textarea><br><br>

        <label>Data:</label><br>
        <input type="date" name="date" value="{{event.date if event else ''}}" required><br><br>

        <label>Local:</label><br>
        <input type="text" name="location" value="{{event.location if event else ''}}" required><br><br>

        <label>Capacidade:</label><br>
        <input type="number" name="capacity" value="{{event.capacity if event else ''}}" min="1" required><br><br>

        <button type="submit">Salvar</button>
    </form>

    <p><a href="/">Voltar para a lista de eventos</a></p>
</body>
</html>
