% rebase('layout.tpl', title=title)

<section class="content-section">
    <div class="container py-5">
        <h1 class="text-center mb-4 display-4 text-dark-text">Sobre a Agenda Cultural</h1>
        <p class="lead text-center text-muted-text mb-5">Nossa missão é conectar você aos melhores eventos culturais da sua cidade.</p>

        <div class="row align-items-center mb-5">
            <div class="col-md-6 mb-4 mb-md-0">
                <img src="/static/images/about-mission.jpg" alt="Equipe trabalhando" class="img-fluid rounded shadow-lg">
            </div>
            <div class="col-md-6">
                <h2 class="text-dark-text mb-3">Nossa Missão</h2>
                <p class="text-muted-text">A Agenda Cultural nasceu da paixão por arte, música, teatro e todas as formas de expressão cultural. Nosso objetivo é simplificar a forma como você descobre e participa de eventos, criando uma ponte entre artistas, produtores e o público.</p>
                <p class="text-muted-text">Acreditamos que a cultura é a alma de uma cidade e que todos devem ter acesso fácil a ela. Por isso, trabalhamos incansavelmente para trazer a você uma curadoria de eventos diversificada e atualizada.</p>
            </div>
        </div>

        <div class="row align-items-center flex-md-row-reverse">
            <div class="col-md-6 mb-4 mb-md-0">
                <img src="/static/images/about-vision.jpg" alt="Pessoas em um evento cultural" class="img-fluid rounded shadow-lg">
            </div>
            <div class="col-md-6">
                <h2 class="text-dark-text mb-3">Nossa Visão</h2>
                <p class="text-muted-text">Ser a plataforma de referência para eventos culturais, reconhecida pela facilidade de uso, abrangência e impacto na promoção da cultura local. Queremos que a Agenda Cultural seja o seu primeiro e único destino para planejar sua agenda de lazer e conhecimento.</p>
                <p class="text-muted-text">Visualizamos um futuro onde a participação cultural é incentivada e a comunidade se fortalece através da arte e do entretenimento.</p>
            </div>
        </div>

        <div class="card p-4 mt-5 shadow-lg rounded-lg text-center bg-light">
            <h3 class="text-dark-text mb-3">Junte-se à Nossa Comunidade!</h3>
            <p class="text-muted-text">Seja você um artista, produtor de eventos ou apenas um entusiasta da cultura, convidamos você a fazer parte da nossa jornada. Explore, descubra e inspire-se!</p>
            <a href="/register" class="btn btn-primary mt-3 w-50 mx-auto">Cadastre-se Agora</a>
        </div>

    </div>
</section>

<script>
    document.addEventListener('DOMContentLoaded', function() {
        const imgMission = document.querySelector('img[alt="Equipe trabalhando"]');
        const imgVision = document.querySelector('img[alt="Pessoas em um evento cultural"]');

        if (imgMission && !imgMission.src.includes('http') && !imgMission.src.includes('static/images')) {
            imgMission.src = 'https://via.placeholder.com/600x400?text=Nossa+Missao';
        }
        if (imgVision && !imgVision.src.includes('http') && !imgVision.src.includes('static/images')) {
            imgVision.src = 'https://via.placeholder.com/600x400?text=Nossa+Visao';
        }
    });
</script>