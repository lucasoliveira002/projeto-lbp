from flask import Blueprint, render_template, request, redirect, url_for, session
from database import db
from models.Curso import Curso
from models.Comment import Comment
from models.User import User
from functools import wraps

cursos_bp = Blueprint('cursos', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login.exibir_formulario'))
        return f(*args, **kwargs)
    return decorated_function

@cursos_bp.route('/cursos', methods=['GET', 'POST'])
def exibir_cursos():
    cursos = Curso.query.all()
    page_id = 1  # Defina o ID da página corretamente
    comments = Comment.query.filter_by(page_id=page_id).all()
    if request.method == 'POST':
        conteudo = request.form['conteudo']
        if 'user_id' in session:
            user_id = session['user_id']
            new_comment = Comment(user_id=user_id, conteudo=conteudo, page_id=page_id)  # Adiciona o page_id
            db.session.add(new_comment)
            db.session.commit()
            return redirect(url_for('cursos.exibir_cursos'))

    return render_template('cursos.html', cursos=cursos, comments=comments)

@cursos_bp.route('/add_cursos', methods=['GET', 'POST'])
@login_required
def add_curso():
    if request.method == 'POST':
        name = request.form['name']
        tipo = request.form['tipo']
        descricao = request.form['descricao']
        user_id = session['user_id']
        
        new_curso = Curso(name=name, tipo=tipo, descricao=descricao, user_id = user_id) #salva o user_id do criador
        db.session.add(new_curso)
        db.session.commit()
        return redirect(url_for('cursos.exibir_cursos'))
    return render_template('add_cursos.html')

@cursos_bp.route('/add_cursos')
@login_required
def exibir_formulario_add_curso():
    return render_template('add_cursos.html')

@cursos_bp.route('/edit_cursos/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_curso(id):
    curso = Curso.query.get_or_404(id)
    if request.method == 'POST':
       curso.name = request.form['name']
       curso.tipo = request.form['tipo']
       curso.descricao = request.form['descricao']
       db.session.commit()
       return redirect(url_for('cursos.exibir_cursos'))
    return render_template('edit_cursos.html', curso = curso)


@cursos_bp.route('/delete_cursos/<int:id>')
@login_required
def delete_curso(id):
    curso = Curso.query.get_or_404(id)
    if curso.user_id != session['user_id']: # verifica se o usuario logado é o criador
        return "Você não tem permissão para excluir este professor.", 403
    db.session.delete(curso)
    db.session.commit()
    return redirect(url_for('cursos.exibir_cursos'))