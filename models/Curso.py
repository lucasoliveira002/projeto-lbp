from database import db
from sqlalchemy import ForeignKey
from models.User import User  # Importe seu modelo User

class Curso(db.Model):
    __tablename__='cursos'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    tipo = db.Column(db.String)
    descricao = db.Column(db.String(100))
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False) # Adicione o campo user_id
    
    user = db.relationship('User', backref=db.backref('cursos', lazy=True))  # Relação com a tabela User

    def __repr__(self):
        return f'<Curso id={self.id}, name={self.name}, tipo={self.email}, user_id={self.user_id}>'
        
    def toJson(self):
        return {"id": self.id, "name": self.name, "tipo": self.tipo, "descricao": self.descricao, "user_id": self.user_id}