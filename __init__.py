from flask import Flask, render_template, session, request
from controllers.professores_controller import professores_bp
from controllers.login_controller import login_bp
from controllers.cursos_controller import cursos_bp
from controllers.ia_controller import ia_bp
from database import init_db
import os
from middleware import login_required_middleware

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.before_request
def middleware_handler():
    if request.endpoint in ('professores.add_teacher', 'professores.edit_teacher',
    'professores.delete_teacher', 'cursos.add_curso',
    'cursos.edit_curso', 'cursos.delete_curso'):
        return login_required_middleware()

@app.route("/")
def pagina_inicial():
    return render_template("home.html")

@app.route("/ia")
def ia():
    return render_template('ia.html')

app.register_blueprint(professores_bp, url_prefix='/professores')
app.register_blueprint(login_bp, url_prefix='/login')
app.register_blueprint(cursos_bp, url_prefix='/cursos')
app.register_blueprint(ia_bp, url_prefix='/ia')


if __name__ == "__main__":
    init_db(app)
    app.run(debug=True)