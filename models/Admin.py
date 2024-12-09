from database import db

class Admin(db.Model):
    __tablename__='admin'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.password(100), nullable=False)

    def __repr__(self):
        return f'{self.name} - {self.email}'

    def toJson(self):
        return {"id": self.id, "name": self.name, "email": self.email}
    