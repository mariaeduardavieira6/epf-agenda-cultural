% rebase('layout.tpl', title='Login')
<div class="form-section">
    <h1>Login</h1>
    % if error:
      <div class="error-message">{{error}}</div>
    % end
    <form action="/login" method="post" class="form-container">
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
        </div>
        <div class="form-group">
            <label for="password">Senha:</label>
            <input type="password" id="password" name="password" required>
        </div>
        <div class="form-actions">
            <button type="submit" class="btn-submit">Entrar</button>
        </div>
    </form>
    <p style="text-align: center; margin-top: 1rem;">Não tem uma conta? <a href="/register">Cadastre-se</a></p>
</div>