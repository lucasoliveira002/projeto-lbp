# controllers/login_controller.py

import os
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.utils import secure_filename
from repository.user_repository import UserRepository
from repository.admin_repository import AdminRepository

login_bp = Blueprint('login', __name__)
user_repository = UserRepository()
admin_repository = AdminRepository()

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@login_bp.route('/acessar_conta', methods=['GET', 'POST'])
def acessar_conta():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = user_repository.get_user_by_email(email)
        if user and user.check_password(password):
            session['user_id'] = user.id
            flash('Bem-vindo de volta!', 'success')
            return redirect(url_for('pagina_inicial'))
        
        admin = admin_repository.get_admin_by_email(email)
        if admin and admin.check_password(password):
            session['user_id'] = admin.id  # Sessão salva como admin
            flash('Bem-vindo de volta!', 'success')
            return redirect(url_for('pagina_inicial'))

        flash('Email ou senha incorretos', 'danger')
        return render_template('entrar.html', error="Email ou senha incorretos")

    return render_template('entrar.html')

@login_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        if user_repository.get_user_by_email(email):
            flash('Email já cadastrado.', 'danger')
            return render_template('register.html', error="Email já cadastrado.")

        # Cadastro de admin (alterar se necessário para usuários normais)
        admin_repository.add_admin(name, email, password)

        flash('Sua conta foi criada com sucesso!', 'success')
        return redirect(url_for('login.acessar_conta'))

    return render_template('register.html')

@login_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Você saiu... LAMENTÁVEL', 'dark')
    return redirect(url_for('pagina_inicial'))

@login_bp.route('/exibir_formulario')
def exibir_formulario():
    return render_template('entrar.html')

@login_bp.route('/editar_perfil', methods=['GET', 'POST'])
def editar_perfil():
    if 'user_id' not in session:
        return redirect(url_for('login.exibir_formulario'))

    user_id = session['user_id']
    user = user_repository.get_user_by_id(user_id)
    admin = admin_repository.get_admin_by_id(user_id)

    profile_picture = (
        admin.profile_picture if admin else user.profile_picture if user else None
    )

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        if 'profile_picture' in request.files:
            file = request.files['profile_picture']
            if file and file.filename != '' and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                upload_folder = 'static/uploads'
                os.makedirs(upload_folder, exist_ok=True)

                file_path = os.path.join(upload_folder, filename)
                file.save(file_path)

                if admin:
                    admin.profile_picture = f'uploads/{filename}'
                    admin_repository.update_admin(admin)
                    session['profile_picture'] = admin.profile_picture
                else:
                    user.profile_picture = f'uploads/{filename}'
                    user_repository.update_user(user)
                    session['profile_picture'] = user.profile_picture

        if admin:
            admin.name = name
            admin.email = email
            admin_repository.update_admin(admin)
        else:
            user.name = name
            user.email = email
            user_repository.update_user(user)

        return redirect(url_for('pagina_inicial'))

    return render_template('editar_perfil.html', user=user, profile_picture=profile_picture)
