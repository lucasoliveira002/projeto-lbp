from models.Admin import Admin
from werkzeug.security import generate_password_hash
from flask import Flask, render_template, session, request
from controllers.professores_controller import professores_bp
from controllers.login_controller import login_bp
from controllers.admin_controller import admin_bp
from controllers.cursos_controller import cursos_bp
from middleware import login_required_middleware, admin_required_middleware
from controllers.ia_controller import ia_bp
from database import db 
import logging
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

logging.basicConfig(filename='error.log', level=logging.ERROR)

# Configurações do SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app) # Inicializa o db

# Registro dos blueprints
app.register_blueprint(professores_bp, url_prefix='/professores')
app.register_blueprint(login_bp, url_prefix='/login')
app.register_blueprint(cursos_bp, url_prefix='/cursos')
app.register_blueprint(ia_bp, url_prefix='/ia')
app.register_blueprint(admin_bp, url_prefix='/admin')

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

@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('erros/404.html'), 404

@app.errorhandler(500)
def erro_interno_servidor(e):
    return render_template('erros/500.html'), 500

@app.errorhandler(Exception)
def tratamento_excecoes(error):
     app.logger.exception(error)  # Log da exceção
     return render_template('erros/erro_geral.html', error=error), 500

#Rota de teste, só tá aqui para testes
@app.route('/testar-excecao')
def testar_excecao():
    raise Exception("Teste de exceção!")

if __name__ == "__main__":
    with app.app_context():
       db.create_all()

       # cria um admin se não houver um admin no banco de dados
       if not Admin.query.first():
           admin = Admin(name="Admin", email="admin@example.com", senha=generate_password_hash("admin"))
           db.session.add(admin)
           db.session.commit()
    app.run(debug=True)
