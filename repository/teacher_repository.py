from dao.teacher_dao import TeacherDAO
from models.Teacher import Teacher

class TeacherRepository:
    def __init__(self):
        self.teacher_dao = TeacherDAO()

    def get_teacher_by_id(self, teacher_id):
        return self.teacher_dao.get_teacher_by_id(teacher_id)

    def get_all_teachers(self):
        return self.teacher_dao.get_all_teachers()

    def add_teacher(self, name, email, idade, descricao, user_id):
        teacher = Teacher(name=name, email=email, idade=idade, descricao=descricao, user_id=user_id)
        self.teacher_dao.add_teacher(teacher)
        return teacher

    def update_teacher(self, teacher):
         self.teacher_dao.update_teacher(teacher)

    def delete_teacher(self, teacher):
         self.teacher_dao.delete_teacher(teacher)