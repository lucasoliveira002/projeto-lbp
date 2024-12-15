from dao.curso_dao import CursoDAO
from models.Curso import Curso

class CursoRepository:
    def __init__(self):
        self.curso_dao = CursoDAO()

    def get_curso_by_id(self, curso_id):
        return self.curso_dao.get_curso_by_id(curso_id)

    def get_all_cursos(self):
        return self.curso_dao.get_all_cursos()

    def add_curso(self, name, tipo, descricao, user_id):
        curso = Curso(name=name, tipo=tipo, descricao=descricao, user_id=user_id)
        self.curso_dao.add_curso(curso)
        return curso
    
    def update_curso(self, curso):
         self.curso_dao.update_curso(curso)

    def delete_curso(self, curso):
        self.curso_dao.delete_curso(curso)