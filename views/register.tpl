%# Este comando indica que este template usa o 'layout.tpl' como base
% rebase('layout.tpl', title='Registrar-se')

<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <h2>Registrar Nova Conta</h2>
                </div>
                <div class="card-body">
                    % if error:
                    <div class="alert alert-danger">
                        {{error}}
                    </div>
                    % end

                    <form action="/register" method="post">
                        <div class="mb-3">
                            <label for="name" class="form-label">Nome Completo:</label>
                            <input type="text" class="form-control" id="name" name="name" required>
                        </div>
                        <div class="mb-3">
                            <label for="email" class="form-label">Email:</label>
                            <input type="email" class="form-control" id="email" name="email" required>
                        </div>
                        <div class="mb-3">
                            <label for="password" class="form-label">Senha:</label>
                            <input type="password" class="form-control" id="password" name="password" required>
                        </div>
                        <div class="mb-3">
                            <label for="birthdate" class="form-label">Data de Nascimento:</label>
                            <input type="date" class="form-control" id="birthdate" name="birthdate" required>
                        </div>
                        <button type="submit" class="btn btn-primary w-100">Registrar</button>
                    </form>
                </div>
                <div class="card-footer text-center">
                    <p>Já tem uma conta? <a href="/login">Faça o login aqui.</a></p>
                </div>
            </div>
        </div>
    </div>
</div>