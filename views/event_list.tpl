%# Usa o layout padrão (se existir)
% rebase('layout.tpl', title='Eventos')

<h1>Eventos Cadastrados</h1>

% if not events:
  <p>Nenhum evento cadastrado ainda.</p>
% else:
  <ul class="event-list">
  % for event in events:
    <li class="event-item">
      <strong>{{event.name}}</strong><br>
      Data: {{event.date}}<br>
      Local: {{event.location}}<br>
      <a href="/events/{{event.id}}">Ver detalhes</a>
    </li>
  % end
  </ul>
% end

% if session.get('is_admin'):
    <a href="/events/new">Criar Novo Evento</a>
% end


<br>
<a href="/events/new">Criar novo evento</a>
