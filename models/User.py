from database import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(128), nullable=False)  # Armazena o hash da senha

    def __repr__(self):
        return f'<User id={self.id}, name={self.name}, email={self.email}>'

    def toJson(self):
        return {"id": self.id, "name": self.name, "email": self.email}

    def set_password(self, password):
      self.senha = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.senha, password)