% rebase('layout.tpl', title='Login')

<h1>Login</h1>

<form action="/login" method="post">
  <label for="email">Email:</label><br>
  <input type="email" id="email" name="email" required><br><br>

  <label for="password">Senha:</label><br>
  <input type="password" id="password" name="password" required><br><br>

  <input type="submit" value="Entrar">
</form>

<p>Não tem uma conta? <a href="/register">Cadastre-se</a></p>