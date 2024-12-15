from database import db
from models.Curso import Curso

class CursoDAO:
    def get_curso_by_id(self, curso_id):
        return Curso.query.get(curso_id)

    def get_all_cursos(self):
        return Curso.query.all()

    def add_curso(self, curso):
        db.session.add(curso)
        db.session.commit()

    def update_curso(self, curso):
        db.session.commit()

    def delete_curso(self, curso):
        db.session.delete(curso)
        db.session.commit()