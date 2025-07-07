# Projeto Template: POO com Python + Bottle + JSON

Este é um projeto de template educacional voltado para o ensino de **Programação Orientada a Objetos (POO)** do Prof. Lucas Boaventura, Universidade de Brasília (UnB).

Utiliza o microframework **Bottle**. Ideal para uso em disciplinas introdutórias de Engenharia de Software ou Ciência da Computação.

## 💡 Objetivo

Fornecer uma base simples, extensível e didática para construção de aplicações web orientadas a objetos com aplicações WEB em Python, ideal para trabalhos finais ou exercícios práticos.

---

## 🗂 Estrutura de Pastas

```bash
poo-python-bottle-template/
├── app.py # Ponto de entrada do sistema
├── config.py # Configurações e caminhos do projeto
├── main.py # Inicialização da aplicação
├── requirements.txt # Dependências do projeto
├── README.md # Este arquivo
├── controllers/ # Controladores e rotas
├── models/ # Definição das entidades (ex: User)
├── services/ # Lógica de persistência (JSON)
├── views/ # Arquivos HTML (Bottle Templating)
├── static/ # CSS, JS e imagens
├── data/ # Arquivos JSON de dados
└── .vscode/ # Configurações opcionais do VS Code
```


---

## 📁 Descrição das Pastas

### `controllers/`
Contém as classes responsáveis por lidar com as rotas da aplicação. Exemplos:
- `user_controller.py`: rotas para listagem, adição, edição e remoção de usuários.
- `base_controller.py`: classe base com utilitários comuns.
- '__init__.py': importa e ativa rotas principais no app (home, usuário, evento, autenticação e API).
- 'api_controller.py': fornece rotas de API com dados pro frontend.
- 'auth_controller.py': configura as rotas de autenticação (login, logout, registro).
- 'event_controller.py': gerencia eventos e inscrições, com login e permissões.
- 'home_controller.py': responsável por renderizar a página inicial (homepage) do site.

### `models/`
Define as classes que representam os dados da aplicação. Exemplo:
- `user.py`: classe `User`, com atributos como `id`, `name`, `email`, etc.
- 'category.py': classe 'Category', que representa uma categoria no sistema.
- 'event.py': classe 'Event', modelo da entidade evento na aplicação.
- 'inscription.py': classe 'Inscription, modelo de inscrição com id, user_id e event_id.

### `services/`
Responsável por salvar, carregar e manipular dados usando arquivos JSON. Exemplo:
- `user_service.py`: contém métodos como `get_all`, `add_user`, `delete_user`.
- 'category_service.py': gerencia lógica e dados das categorias.
- 'event_service.py': CRUD de eventos com arquivo JSON.
- 'inscription_service.py': gerencia inscrições entre usuários e eventos via arquivo JSON.
- 'registration_service.py': gerencia inscrições de usuários em eventos usando arquivo JSON.
  
### `views/`
Contém os arquivos `.tpl` utilizados pelo Bottle como páginas HTML:
- `layout.tpl`: estrutura base com navegação e bloco `content`.
- `users.tpl`: lista os usuários.
- `user_form.tpl`: formulário para adicionar/editar usuário.
- 'about_page.tpl': apresenta a história, missão e visão da Agenda Cultural.
- 'admin_users.tpl': lista usuários, mostra inscrições e permite admins removerem inscrições.
- 'category_list.tpl': exibe categorias com ícones para filtro de eventos.
- 'contact_page.tpl': formulário de contato com validação, mensagens e informações de contato.
- 'event_detail.tpl': mostra detalhes do evento, inscrições, preço, e botões para inscrever/cancelar ou editar/excluir (admin).
- 'event_form.tpl': formulário para criar ou editar evento com campos como nome, descrição, data, local, capacidade, categoria, preço e imagem.
- 'event_list.tpl': lista eventos com filtros e botões para ver, editar ou excluir (apenas admins).
- 'event_register_form.tpl': confirma inscrição em evento, exibe erro se houver, botão para confirmar e link para voltar.
- 'helper-final.tpl': MVC básico; Model guarda dados, Service trata lógica, Controller cuida rotas, Views exibem tela.
- 'home.tpl':  página inicial do site cultural exibe eventos, estatísticas e busca.
- 'login.tpl': exibe formulário para email e senha, mensagem de erro (se houver) e um link para cadastro.
- 'register.tpl': contém formulário para nome, email, senha e data de nascimento, exibindo mensagens de erro e link para login.

### `static/`
Arquivos estáticos como:
- `css/style.css`: estilos básicos.
- `js/main.js`: scripts JS opcionais.
- `img/BottleLogo.png`: exemplo de imagem.

### `data/`
Armazena os arquivos `.json` que simulam o banco de dados:
- `users.json`: onde os dados dos usuários são persistidos.
- 'categories.json': onde os dados das categorias são persistidos.
- 'events.json': onde os dados dos eventos são persistidos.
- 'inscriptions.json': onde os dados de inscrições de usuários em eventos são persistidos.
- 'registrations.json': onde os dados de inscrições de usuários em eventos são persistidos

---
## 📘 Diagrama de Classes
![Diagrama de classes](https://github.com/user-attachments/assets/e612649e-aa9a-48e6-8985-982f012f801f)




## ▶️ Como Executar

1. Crie o ambiente virtual na pasta fora do seu projeto:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate     # Windows
```

2. Entre dentro do seu projeto criado a partir do template e instale as dependências:
```bash
pip install -r requirements.txt
```

3. Rode a aplicação:
```bash
python main.py
```

4. Accese sua aplicação no navegador em: [http://localhost:8080](http://localhost:8080)

---

## ✍️ Personalização
Para adicionar novos modelos (ex: Atividades):

1. Crie a classe no diretório **models/**.

2. Crie o service correspondente para manipulação do JSON.

3. Crie o controller com as rotas.

4. Crie as views .tpl associadas.

---

## 🧠 Autor e Licença
Projeto desenvolvido como template didático para disciplinas de Programação Orientada a Objetos, baseado no [BMVC](https://github.com/hgmachine/bmvc_start_from_this).
Você pode reutilizar, modificar e compartilhar livremente.
