% rebase('layout.tpl', title='Eventos', categories=categories, locations=locations)

<style>
    /* Estilo para os botões de busca rápida */
    .quick-search {
        margin-top: 20px;
        text-align: center;
    }
    .quick-search .btn {
        margin: 0 5px;
    }
</style>

<h1>{{ title or 'Eventos Cadastrados' }}</h1>

<!-- Formulário de Busca -->
<div class="search-bar card mb-4">
    <div class="card-body">
        <form action="/events" method="GET" class="row g-3 align-items-end">
            <div class="col-md-4">
                <label for="query" class="form-label">O que você procura?</label>
                <input type="text" name="query" id="query" class="form-control" placeholder="Nome do evento...">
            </div>
            <div class="col-md-3">
                <label for="category_id" class="form-label">Categoria</label>
                <select name="category_id" id="category_id" class="form-select">
                    <option value="">Todas</option>
                    % for cat in categories:
                        <option value="{{cat.id}}">{{cat.name}}</option>
                    % end
                </select>
            </div>
            <div class="col-md-3">
                <label for="location" class="form-label">Local</label>
                <select name="location" id="location" class="form-select">
                    <option value="">Todos</option>
                    % for loc in locations:
                        <option value="{{loc}}">{{loc}}</option>
                    % end
                </select>
            </div>
            <div class="col-md-2">
                <button type="submit" class="btn btn-primary w-100">Buscar</button>
            </div>
        </form>

        <!-- INÍCIO DA ALTERAÇÃO: Adicionado o botão "Gratuitos" -->
        <div class="quick-search">
            <span class="me-2">Busca rápida:</span>
            <a href="/events?filter=today" class="btn btn-outline-secondary btn-sm">Hoje</a>
            <a href="/events?filter=weekend" class="btn btn-outline-secondary btn-sm">Este fim de semana</a>
            <a href="/events?filter=free" class="btn btn-outline-secondary btn-sm">Gratuitos</a>
        </div>
        <!-- FIM DA ALTERAÇÃO -->
    </div>
</div>


% if not events:
  <p>Nenhum evento encontrado.</p>
% else:
  <ul class="event-list list-group">
  % for event in events:
    <li class="event-item list-group-item">
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
