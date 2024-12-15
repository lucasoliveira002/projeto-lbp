# repository/admin_repository.py
from dao.admin_dao import AdminDAO
from models.Admin import Admin

class AdminRepository:
    def __init__(self):
        self.admin_dao = AdminDAO()

    def get_admin_by_id(self, admin_id):
        return self.admin_dao.get_admin_by_id(admin_id)

    def get_admin_by_email(self, email):
        return self.admin_dao.get_admin_by_email(email)

    def add_admin(self, name, email, password):
        admin = Admin(name=name, email=email)
        admin.set_password(password)
        self.admin_dao.add_admin(admin)
        return admin