%# Usando o layout.tpl como base
% rebase('layout.tpl', title=event.name)

<div class="container mt-4">

    % if message:
        <div class="alert alert-info alert-dismissible fade show" role="alert">
            {{ message }}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    % end

    <div class="card">
        <div class="card-header">
            <h1>{{ event.name }}</h1>
        </div>
        <div class="card-body">
            <p><strong>Descrição:</strong> {{ event.description }}</p>
            <p><strong>Data:</strong> {{ event.date }}</p>
            <p><strong>Local:</strong> {{ event.location }}</p>
            <p><strong>Capacidade:</strong> {{ len(subscribers) }} / {{ event.capacity }}</p>
            <p><strong>Vagas restantes:</strong> {{ remaining_slots }}</p>

            <!-- INÍCIO DA ALTERAÇÃO: Exibição do Preço -->
            <p>
                <strong>Preço:</strong>
                % if event.price > 0:
                    R$ {{ '%.2f' % event.price }}
                % else:
                    Gratuito
                % end
            </p>
            <!-- FIM DA ALTERAÇÃO -->

            <hr>

            % if session and session.get('is_admin'):
                <a href="/events/edit/{{event.id}}" class="btn btn-warning">Editar Evento</a>
                <form action="/events/delete/{{event.id}}" method="post" style="display:inline;" onsubmit="return confirm('Deseja realmente excluir este evento?');">
                    <button type="submit" class="btn btn-danger">Excluir Evento</button>
                </form>
            % end

            % if session.get('user_id') and not session.get('is_admin'):
                % if is_subscribed:
                    <form action="/events/{{event.id}}/unsubscribe" method="post" style="display:inline;" onsubmit="return confirm('Deseja realmente cancelar sua inscrição?');">
                        <button type="submit" class="btn btn-warning">Cancelar Inscrição</button>
                    </form>
                % else:
                    % if remaining_slots > 0:
                        <form action="/events/{{event.id}}/subscribe" method="post" style="display:inline;">
                            <button type="submit" class="btn btn-success">Inscrever-se</button>
                        </form>
                    % else:
                        <button class="btn btn-secondary" disabled>Evento lotado</button>
                    % end
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
