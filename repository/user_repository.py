from dao.user_dao import UserDAO
from models.User import User

class UserRepository:
    def __init__(self):
        self.user_dao = UserDAO()

    def get_user_by_id(self, user_id):
       return self.user_dao.get_user_by_id(user_id)

    def get_user_by_email(self, email):
        return self.user_dao.get_user_by_email(email)

    def add_user(self, name, email, password):
        user = User(name=name, email=email)
        user.set_password(password)
        self.user_dao.add_user(user)
        return user

    def update_user(self, user):
         self.user_dao.update_user(user)

    def delete_user(self, user):
         self.user_dao.delete_user(user)