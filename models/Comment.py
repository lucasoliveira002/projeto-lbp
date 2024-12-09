from database import db

class Comments(db.Model):
    __tablename__='comments'

    id = db.Column(db.Integer, primary_key=True)
    conteudo = db.Column(db.string(120))