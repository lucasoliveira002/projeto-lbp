from flask import Blueprint, render_template, request, redirect, url_for, session
from database import db
from models.User import User # Importe seu modelo User

login_bp = Blueprint('login', __name__)

@login_bp.route('/acessar_conta', methods=['GET', 'POST'])
def acessar_conta():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first() #busca o usuario no banco
        if user and user.check_password(password):
           session['user_id'] = user.id #defini o id do usuario na sessão
           return redirect(url_for('pagina_inicial')) # se o usuario existir e a senha estiver correta redireciona para a home
        else:
             return render_template('entrar.html', error="Email ou senha incorretos") # caso contrario volta para o formulario com mensagem de erro
    return render_template('entrar.html') # se for um get retona o formulario

@login_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        if User.query.filter_by(email=email).first():
          return render_template('register.html', error="Email já cadastrado.")  # se ja existir um usuario com esse email retorna um erro

        new_user = User(name=name, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit() #adiciona o usuario no banco
        return redirect(url_for('login.acessar_conta'))# redireciona para o formulario de login
    return render_template('register.html')

@login_bp.route('/logout')
def logout():
    session.pop('user_id', None) #remove o id do usuario da sessão
    return redirect(url_for('pagina_inicial'))#redireciona para a home

@login_bp.route('/exibir_formulario')
def exibir_formulario():
    return render_template('entrar.html')