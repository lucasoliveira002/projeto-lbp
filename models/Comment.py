from database import db
from sqlalchemy import ForeignKey
from models.User import User


class Comment(db.Model):
    __tablename__='comments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)
    conteudo = db.Column(db.String(120))

    user = db.relationship('User', backref=db.backref('comments', lazy=True))  # Relação com a tabela User
    
    def __repr__(self):
        return f'<Comment id={self.id}, user_id={self.user_id}, conteudo={self.conteudo}>'
    
    def toJson(self):
        return {"id": self.id, "user_id": self.user_id, "conteudo": self.conteudo}