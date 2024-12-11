from flask import Flask, render_template
from controllers.professores_controller import professores_bp
from database import init_db

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return render_template("home.html")

app.register_blueprint(professores_bp, url_prefix='/professores')

if __name__ == "__main__":
    init_db(app)
    app.run(debug=True)
