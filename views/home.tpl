% rebase('layout.tpl', title='Página Inicial')
<div class="container my-5">
    <h1>Bem-vindo(a) à Agenda Cultural!</h1>

    % if user_name:
    <p>Você está logado como <strong>{{user_name}}</strong>.</p>
    % else:
    <p>Você não está logado. Por favor, <a href="/login">faça o login</a> ou <a href="/register">cadastre-se</a> para participar.</p>
    % end
</div>

<section class="category-section py-5" id="categorias">
    <div class="container">
        <div class="text-center mb-5">
            <h2 class="display-4 fw-bold mb-3 text-cosmos-blue">
                Explore por Categoria
            </h2>
            <p class="lead text-muted max-w-lg mx-auto">
                Encontre exatamente o tipo de evento cultural que você procura
            </p>
        </div>

        <div class="row row-cols-2 row-cols-md-4 g-4">
            % # Este loop itera sobre a lista 'categories' que é passada do seu app.py
            % for category in categories:
            <div class="col">
                <div class="category-card text-center h-100">
                    <div class="category-icon mb-3">
                        {{category['icon']}}
                    </div>
                    <h3 class="h5 fw-semibold mb-1">
                        {{category['label']}}
                    </h3>
                    <p class="small text-muted">
                        Descubra eventos
                    </p>
                </div>
            </div>
            % end
        </div>
    </div>
</section>