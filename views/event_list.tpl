%# Esta é a linha mais importante: ela faz a página usar o layout principal.
% rebase('layout.tpl', title='Eventos')

<h1>Eventos Cadastrados</h1>

%# Verificamos se a lista de eventos não está vazia.
% if not events:
  <p>Nenhum evento cadastrado ainda.</p>
% else:
  <ul class="event-list">
  % for event in events:
    <li class="event-item">
      <strong>{{event.name}}</strong><br>
      Data: {{event.date}}<br>
      Local: {{event.location}}
    </li>
  % end
  </ul>
% end

<br>
<a href="/events/new">Criar novo evento</a>