% rebase('views/layout.tpl', title=title)

<div class="page-content">
    <h1>{{ title }}</h1>
    
    % if not categories:
        <p>Nenhuma categoria encontrada.</p>
    % else:
        <ul class="category-list">
            % for category in categories:
                <li>
                    <!-- O link agora usa o ID da categoria, que é mais seguro -->
                    <a href="/events?category_id={{category.id}}">
                        {{ category.name }}
                    </a>
                </li>
            % end
        </ul>
    % end
</div>