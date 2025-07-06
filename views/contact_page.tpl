% rebase('layout.tpl', title=title)

<section class="content-section">
    <div class="container py-5">
        <h1 class="text-center mb-4 display-4 text-dark-text">Fale Conosco!</h1>
        <p class="lead text-center text-muted-text mb-5">Envie-nos uma mensagem, adoraríamos ouvir você!</p>

        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card p-5 shadow-lg rounded-lg">
                    <form action="/contact" method="post">
                        % if success_message:
                        <div class="alert alert-success text-center mb-4" role="alert">
                            {{success_message}}
                        </div>
                        % end
                        % if error:
                        <div class="alert alert-danger text-center mb-4" role="alert">
                            {{error}}
                        </div>
                        % end

                        <div class="form-group mb-3">
                            <label for="name">Nome Completo:</label>
                            <input type="text" id="name" name="name" class="form-control" value="{{contact_form.get('name', '')}}" required> 
                        </div>

                        <div class="form-group mb-3">
                            <label for="email">Email:</label>
                            <input type="email" id="email" name="email" class="form-control" value="{{contact_form.get('email', '')}}" required> 
                        </div>

                        <div class="form-group mb-4">
                            <label for="message">Deixe aqui sua mensagem:</label>
                            <textarea id="message" name="message" rows="6" class="form-control" required>{{contact_form.get('message', '')}}</textarea> 
                        </div>

                        <div class="text-center">
                            <button type="submit" class="btn btn-primary btn-lg w-50">Enviar Mensagem</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>

        <div class="row mt-5 text-center">
            <div class="col-md-4">
                <div class="icon-box p-4 rounded-lg shadow-sm">
                    <i class="fas fa-map-marker-alt fa-3x mb-3 text-primary-color"></i>
                    <h4 class="text-dark-text">Endereço</h4>
                    <p class="text-muted-text">Brasília - DF, Brasil</p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="icon-box p-4 rounded-lg shadow-sm">
                    <i class="fas fa-phone-alt fa-3x mb-3 text-primary-color"></i>
                    <h4 class="text-dark-text">Telefone</h4>
                    <p class="text-muted-text">(61) 9999-9999</p>
                </div>
            </div>
            <div class="col-md-4">
                <div class="icon-box p-4 rounded-lg shadow-sm">
                    <i class="fas fa-envelope fa-3x mb-3 text-primary-color"></i>
                    <h4 class="text-dark-text">Email</h4>
                    <p class="text-muted-text">contato@agendacultural.com</p>
                </div>
            </div>
        </div>
    </div>
</section>