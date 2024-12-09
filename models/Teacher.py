from database import db

class Teacher(db.Model):
    __tablename__='teachers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    idade = db.Column(db.Integer(100))
    descricao = db.Column(db.Integer(800))