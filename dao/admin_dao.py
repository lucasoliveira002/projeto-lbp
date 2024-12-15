# dao/admin_dao.py
from database import db
from models.Admin import Admin

class AdminDAO:
    def get_admin_by_id(self, admin_id):
        return Admin.query.get(admin_id)

    def get_admin_by_email(self, email):
        return Admin.query.filter_by(email=email).first()
    
    def add_admin(self, admin):
         db.session.add(admin)
         db.session.commit()