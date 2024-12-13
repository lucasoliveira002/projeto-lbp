import os
from flask import Blueprint, render_template, request, redirect, url_for, session
from database import db
from models.User import User
from werkzeug.utils import secure_filename

login_bp = Blueprint('login', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'} # Extensões de arquivo permitidas

def allowed_file(filename): # Função auxiliar para verificar a extensão
     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@login_bp.route('/acessar_conta', methods=['GET', 'POST'])
def acessar_conta():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            return redirect(url_for('pagina_inicial'))
        else:
            return render_template('entrar.html', error="Email ou senha incorretos")
    return render_template('entrar.html')

@login_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        if User.query.filter_by(email=email).first():
            return render_template('register.html', error="Email já cadastrado.")

        new_user = User(name=name, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login.acessar_conta'))
    return render_template('register.html')

@login_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('pagina_inicial'))

@login_bp.route('/exibir_formulario')
def exibir_formulario():
    return render_template('entrar.html')

@login_bp.route('/editar_perfil', methods=['GET', 'POST'])
def editar_perfil():
    if 'user_id' not in session:
        return redirect(url_for('login.exibir_formulario'))
    
    user_id = session['user_id']
    user = User.query.get(user_id)
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        
         # Salvar a foto de perfil se o usuário enviou uma
        if 'profile_picture' in request.files:
              file = request.files['profile_picture']

              if file and file.filename != '' and allowed_file(file.filename):
                 filename = secure_filename(file.filename) # deixa o nome do arquivo seguro
                 upload_folder = 'static/uploads' #Pasta onde as imagens serão salvas, que será criada na pasta static
                 os.makedirs(upload_folder, exist_ok=True) # Cria a pasta caso ela não exista

                 file_path = os.path.join(upload_folder, filename)
                 file.save(file_path)
                 user.profile_picture = f'uploads/{filename}'# Salva o caminho do arquivo no banco de dados
                          
        user.name = name
        user.email = email
        db.session.commit()
        
        session['profile_picture'] = user.profile_picture #salva na sessão
        return redirect(url_for('pagina_inicial'))
    return render_template('editar_perfil.html', user=user)