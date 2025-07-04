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
      
      Descrição: {{event.description}}<br> 
      
      <a href="/events/{{event.id}}">Ver detalhes</a>
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