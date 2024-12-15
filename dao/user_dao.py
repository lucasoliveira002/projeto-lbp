from database import db
from models.User import User

class UserDAO:

    def get_user_by_id(self, user_id):
        return User.query.get(user_id)

    def get_user_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def add_user(self, user):
        db.session.add(user)
        db.session.commit()

    def update_user(self, user):
        db.session.commit()

    def delete_user(self, user):
        db.session.delete(user)
        db.session.commit()