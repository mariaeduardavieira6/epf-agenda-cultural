from bottle import view 

def setup(app):

   
    @app.route('/register', method='GET')
    @view('user_form')
    def show_register_form():
        return dict(
            user=None,
            action='/register'
        )
    
    