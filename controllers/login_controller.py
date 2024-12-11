from flask import Blueprint, render_template, request, redirect, url_for

login_bp = Blueprint('login', __name__)

#usuarios pre definidos
users = [
    {"name": "julia", "email": "juju@example.com", "password": "123"},
    {"name": "gustavo", "email": "gustavo@example.com", "password": "123"},
    {"name": "lima", "email": "lima@example.com", "password": "123"},
]

@login_bp.route('/entrar',  methods=['GET', 'POST'])
def acessar_conta():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        users.append({"email": email, "password": password})
    return redirect(url_for('entrar.html'), users=users)