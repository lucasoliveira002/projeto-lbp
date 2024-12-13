from flask import Blueprint, render_template, request, redirect, url_for, session
from database import db
from models.Teacher import Teacher
from models.Comment import Comment
from models.User import User
from functools import wraps

professores_bp = Blueprint('professores', __name__)

# Decorator para verificar se o usuário está logado
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login.exibir_formulario'))
        return f(*args, **kwargs)
    return decorated_function

@professores_bp.route('/professores', methods=['GET', 'POST'])
def exibir_professores():
    teachers = Teacher.query.all()
    page_id = 1  # Defina o ID da página corretamente
    comments = Comment.query.filter_by(page_id=page_id).all()
    if request.method == 'POST':
        conteudo = request.form['conteudo']
        if 'user_id' in session:
            user_id = session['user_id']
            new_comment = Comment(user_id=user_id, conteudo=conteudo, page_id=page_id)  # Adiciona o page_id
            db.session.add(new_comment)
            db.session.commit()
            return redirect(url_for('professores.exibir_professores'))

    return render_template('professores.html', teachers=teachers, comments=comments)


@professores_bp.route('/add_professores', methods=['GET', 'POST'])
@login_required
def add_teacher():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        idade = request.form['idade']
        descricao = request.form['descricao']
        user_id = session['user_id']

        new_teacher = Teacher(name=name, email=email, idade=idade, descricao=descricao, user_id=user_id)  # salva o user_id do criador
        db.session.add(new_teacher)
        db.session.commit()
        return redirect(url_for('professores.exibir_professores'))
    return render_template('add_professores.html')

@professores_bp.route('/add_professores')
@login_required
def exibir_formulario_add_teacher():
    return render_template('add_professores.html')


@professores_bp.route('/edit_professores/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    if request.method == 'POST':
        teacher.name = request.form['name']
        teacher.email = request.form['email']
        teacher.idade = request.form['idade']
        teacher.descricao = request.form['descricao']
        db.session.commit()
        return redirect(url_for('professores.exibir_professores'))
    return render_template('edit_professores.html', teacher=teacher)


@professores_bp.route('/delete_professores/<int:id>')
@login_required
def delete_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    if teacher.user_id != session['user_id']:  # verifica se o usuario logado é o criador
        return "Você não tem permissão para excluir este professor.", 403
    db.session.delete(teacher)
    db.session.commit()
    return redirect(url_for('professores.exibir_professores'))