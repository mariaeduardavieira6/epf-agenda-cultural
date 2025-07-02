<h1>Usuários cadastrados</h1>
<table border="1">
    <thead>
        <tr><th>Nome</th><th>Email</th><th>Inscrições</th><th>Ações</th></tr>
    </thead>
    <tbody>
        % for user in users:
        <tr>
            <td>{{user.name}}</td>
            <td>{{user.email}}</td>
            <td>
                % for event in registration_service.get_events_for_user(user.id):
                    {{event.name}}<br>
                % end
            </td>
            <td>
                % for event in registration_service.get_events_for_user(user.id):
                    <form action="/adm/users/{{user.id}}/remove_registration/{{event.id}}" method="post" style="display:inline;">
                        <button type="submit" onclick="return confirm('Remover inscrição de {{user.name}} no evento {{event.name}}?')">Remover inscrição</button>
                    </form><br>
                % end
            </td>
        </tr>
        % end
    </tbody>
</table>
