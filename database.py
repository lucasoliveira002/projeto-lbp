from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://estudante1:estudante1@localhost/wiki'  # Pode ser MySQL, PostgreSQL etc.
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    with app.app_context():
        db.init_app(app)
        db.create_all()