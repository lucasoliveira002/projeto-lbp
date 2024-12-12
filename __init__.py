from flask import Flask, render_template, session
from controllers.professores_controller import professores_bp
from controllers.login_controller import login_bp
from database import init_db
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def pagina_inicial():
    return render_template("home.html")

app.register_blueprint(professores_bp, url_prefix='/professores')
app.register_blueprint(login_bp, url_prefix='/login')


if __name__ == "__main__":
    init_db(app)
    app.run(debug=True)