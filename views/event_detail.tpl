%# Usando o layout.tpl como base
% rebase('layout.tpl', title=event.name)

<div class="container mt-4">
    <div class="card">
        <div class="card-header">
            <h1>{{ event.name }}</h1>
        </div>
        <div class="card-body">
            <p><strong>Descrição:</strong> {{ event.description }}</p>
            <p><strong>Data:</strong> {{ event.date }}</p>
            <p><strong>Local:</strong> {{ event.location }}</p>
            <p><strong>Capacidade:</strong> {{ len(subscribers) }} / {{ event.capacity }}</p>
            
            <hr>

            % if session.get('is_admin'):
                <a href="/events/edit/{{event.id}}" class="btn btn-primary">Editar Evento</a>
                
                <form action="/events/delete/{{event.id}}" method="post" style="display:inline;" onsubmit="return confirm('Tem certeza que deseja excluir este evento?');">
                    <button type="submit" class="btn btn-danger">Excluir Evento</button>
                </form>
            % end

            % if session.get('user_id') and not session.get('is_admin'):
                
                % if is_subscribed:
                    <form action="/events/{{event.id}}/unsubscribe" method="post" style="display:inline;">
                        <button type="submit" class="btn btn-warning">Cancelar Inscrição</button>
                    </form>
                % else:
                    <form action="/events/{{event.id}}/subscribe" method="post" style="display:inline;">
                        <button type="submit" class="btn btn-success">Inscrever-se</button>
                    </form>
                % end

            % end
            
            <a href="/" class="btn btn-secondary">Voltar para a lista</a>

        </div>
    </div>

    <div class="card mt-4">
        <div class="card-header">
            <h3>Participantes Inscritos ({{ len(subscribers) }})</h3>
        </div>
        <div class="card-body">
            % if subscribers:
                <ul class="list-group">
                    % for user in subscribers:
                        <li class="list-group-item">{{ user.name }}</li>
                    % end
                </ul>
            % else:
                <p>Ninguém se inscreveu neste evento ainda.</p>
            % end
        </div>
    </div>
</div>