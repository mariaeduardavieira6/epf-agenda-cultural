% rebase('layout.tpl', title='Editar Evento' if event else 'Novo Evento', categories=categories)

<div class="card">
    <div class="card-header">
        <h1>{{'Editar Evento' if event else 'Criar Novo Evento'}}</h1>
    </div>
    <div class="card-body">
        % if error:
            <div class="alert alert-danger">{{error}}</div>
        % end

        <form action="{{'/events/edit/' + str(event.id) if event else '/events/new'}}" method="post">
            <div class="mb-3">
                <label for="name" class="form-label">Nome do Evento:</label>
                <input type="text" id="name" name="name" class="form-control" value="{{event.name if event else ''}}" required>
            </div>

            <div class="mb-3">
                <label for="description" class="form-label">Descrição:</label>
                <textarea id="description" name="description" class="form-control" rows="4" required>{{event.description if event else ''}}</textarea>
            </div>

            <div class="row">
                <div class="col-md-4 mb-3">
                    <label for="date" class="form-label">Data:</label>
                    <input type="date" id="date" name="date" class="form-control" value="{{event.date if event else ''}}" required>
                </div>
                <div class="col-md-4 mb-3">
                    <label for="city" class="form-label">Cidade:</label>
                    <input type="text" id="city" name="city" class="form-control" placeholder="Ex: Brasília, Goiânia" value="{{event.city if event else ''}}" required>
                </div>
                <div class="col-md-4 mb-3">
                    <label for="location" class="form-label">Local (Endereço Específico):</label>
                    <input type="text" id="location" name="location" class="form-control" placeholder="Ex: Estádio Municipal" value="{{event.location if event else ''}}" required>
                </div>
            </div>
            <div class="row">
                <div class="col-md-4 mb-3">
                    <label for="capacity" class="form-label">Capacidade:</label>
                    <input type="number" id="capacity" name="capacity" class="form-control" value="{{event.capacity if event else ''}}" min="1" required>
                </div>
                <div class="col-md-4 mb-3">
                    <label for="category" class="form-label">Categoria:</label>
                    <select id="category" name="category" class="form-select" required>
                        % for cat in categories:
                            % if event and event.category == cat.name:
                                <option value="{{cat.name}}" selected>{{cat.name}}</option>
                            % else:
                                <option value="{{cat.name}}">{{cat.name}}</option>
                            % end
                        % end
                    </select>
                </div>
                <div class="col-md-4 mb-3">
                    <label for="price" class="form-label">Preço (R$):</label>
                    <input type="number" id="price" name="price" class="form-control" value="{{event.price if event else '0.00'}}" min="0" step="0.01" required>
                </div>
            </div>
            <div class="mb-3">
                <label for="image_url" class="form-label">URL da Imagem (opcional):</label>
                <input type="url" class="form-control" id="image_url" name="image_url" value="{{ event.image_url if event else '' }}" placeholder="Ex: https://example.com/imagem-do-evento.jpg">
                <div class="form-text text-muted">Cole aqui o link direto para a imagem do evento. Esta imagem será exibida na listagem e na página de detalhes.</div>
            </div>

            <hr>

            <button type="submit" class="btn btn-primary">Salvar Alterações</button>
            <a href="/events" class="btn btn-secondary">Cancelar</a>
        </form>
    </div>
</div>