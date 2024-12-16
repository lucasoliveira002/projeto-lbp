# controllers/admin_controller.py
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from functools import wraps
from models.Admin import Admin
from models.User import User
from models.Teacher import Teacher
from database import db
from werkzeug.security import generate_password_hash
from middleware import admin_required_middleware

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')
    
@admin_bp.route('/')
@admin_required_middleware
def painel():
    return render_template('admin/painel.html')
# Rota para listar todos os usuários
@admin_bp.route('/users')
@admin_required_middleware
def listar_usuarios():
    users = User.query.all()
    return render_template('admin/listar_usuarios.html', users=users)
# Rota para adicionar um admin
@admin_bp.route('/add_admin', methods=['GET', 'POST'])
@admin_required_middleware
def add_admin():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        new_admin = Admin(name=name, email=email, senha=hashed_password)
        db.session.add(new_admin)
        db.session.commit()
        flash('Admin adicionado com sucesso!', 'success')
        return redirect(url_for('admin.listar_usuarios'))
    return render_template('admin/add_admin.html')
# Rota para excluir um professor
@admin_bp.route('/delete_teacher/<int:id>')
@admin_required_middleware
def delete_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    db.session.delete(teacher)
    db.session.commit()
    flash('Professor excluido com sucesso', 'success')
    return redirect(url_for('admin.painel'))
# Rota para excluir um usuario
@admin_bp.route('/delete_user/<int:id>')
@admin_required_middleware
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('Usuario excluido com sucesso', 'success')
    return redirect(url_for('admin.listar_usuarios'))