% rebase('layout.tpl', title=title)

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
            % for category in categories:
            <div class="col">
                <div class="category-card text-center h-100">
                    <div class="category-icon mb-3">
                        {{category['icon']}}
                    </div>
                    <h3 class="h5 fw-semibold mb-1">
                        <a href="/events?category_id={{category['id']}}" class="text-decoration-none text-cosmos-blue hover-crimson-blaze">
                            {{category['name']}}
                        </a>
                    </h3>
                    <p class="small text-muted">
                        Descubra eventos
                    </p>
                </div>
            </div>
            % end
        </div>
        % # A mensagem "Nenhuma categoria encontrada" foi movida para fora do grid para melhor layout
        % if not categories:
            <p class="text-center text-muted mt-5">Nenhuma categoria encontrada.</p>
        % end
    </div>
</section>