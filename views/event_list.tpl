% rebase('layout.tpl', title='Eventos')

<h1>{{ title or 'Eventos Cadastrados' }}</h1>

% if not events:
  <p>Nenhum evento encontrado.</p>
% else:
  <ul class="event-list">
  % for event in events:
    <li class="event-item">
      <strong>{{event.name}}</strong><br>
      Data: {{event.date}}<br>
      Local: {{event.location}}<br>
      
      Descrição: {{event.description}}<br>
      
      <a href="/events/{{event.id}}">Ver detalhes</a>

      <!-- Bloco que adiciona os botões de Editar e Excluir para o admin -->
      % if session and session.get('is_admin'):
        <div class="admin-actions" style="margin-top: 5px;">
          <a href="/events/edit/{{event.id}}" class="admin-link">Editar</a>
          
          <!-- O botão de excluir fica dentro de um formulário por segurança -->
          <form action="/events/delete/{{event.id}}" method="POST" style="display: inline; margin-left: 10px;">
            <button type="submit" class="admin-link-delete" onclick="return confirm('Tem certeza que deseja excluir este evento?');">Excluir</button>
          </form>
        </div>
      % end

    </li>
  % end
  </ul>
% end

<br>
% if session and session.get('is_admin'):
  <div class="text-center mt-4">
      <a href="/events/new" class="btn btn-primary">Criar Novo Evento</a>
  </div>
% end