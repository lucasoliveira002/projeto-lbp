from database import db
from sqlalchemy import ForeignKey
from models.User import User  # Importe seu modelo User

class Teacher(db.Model):
    __tablename__='teachers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    idade = db.Column(db.Integer)
    descricao = db.Column(db.String(800))
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False) # Adicione o campo user_id
    
    user = db.relationship('User', backref=db.backref('teachers', lazy=True))  # Relação com a tabela User

    def __repr__(self):
        return f'<Teacher id={self.id}, name={self.name}, email={self.email}, user_id={self.user_id}>'
        
    def toJson(self):
        return {"id": self.id, "name": self.name, "email": self.email, "idade": self.idade, "descricao": self.descricao, "user_id": self.user_id}
    