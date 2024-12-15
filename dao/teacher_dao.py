from database import db
from models.Teacher import Teacher

class TeacherDAO:

    def get_teacher_by_id(self, teacher_id):
        return Teacher.query.get(teacher_id)

    def get_all_teachers(self):
        return Teacher.query.all()

    def add_teacher(self, teacher):
        db.session.add(teacher)
        db.session.commit()

    def update_teacher(self, teacher):
        db.session.commit()
    
    def delete_teacher(self, teacher):
        db.session.delete(teacher)
        db.session.commit()