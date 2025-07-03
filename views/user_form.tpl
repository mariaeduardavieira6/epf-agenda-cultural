% rebase('layout.tpl', title='Cadastro de Usuário')

<div class="form-section">
    <h1>Cadastrar Nova Conta</h1>

    <form action="/register" method="post" class="form-container">
        <div class="form-group">
            <label for="name">Nome Completo:</label>
            <input type="text" id="name" name="name" class="form-control" required>
        </div>
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" class="form-control" required>
        </div>
        <div class="form-group">
            <label for="password">Senha:</label>
            <input type="password" id="password" name="password" class="form-control" required>
        </div>
        <div class="form-group">
            <label for="birthdate">Data de Nascimento:</label>
            <input type="date" id="birthdate" name="birthdate" class="form-control" required>
        </div>
        <div class="form-actions">
            <button type="submit" class="btn-submit">Cadastrar</button>
            <a href="/login" class="btn-cancel">Já tem uma conta? Faça o login.</a>
        </div>
    </form>
</div>