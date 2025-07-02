% rebase('layout.tpl', title='Página Inicial')

<h1>Bem-vindo(a) à Agenda Cultural!</h1>

% if user_name:
  <p>Você está logado como <strong>{{user_name}}</strong>.</p>
% else:
  <p>Você não está logado. Por favor, <a href="/login">faça o login</a> ou <a href="/register">cadastre-se</a> para participar.</p>
% end