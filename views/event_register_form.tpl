<h2>Inscrição no evento: {{event.name}}</h2>

% if error:
<p style="color:red;">{{error}}</p>
% end

<form action="/events/{{event.id}}/register" method="post">
    <p>Tem certeza que deseja se inscrever neste evento?</p>
    <button type="submit">Confirmar inscrição</button>
</form>

<a href="/events/{{event.id}}">Voltar</a>
