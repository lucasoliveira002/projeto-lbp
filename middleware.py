# middleware.py
from flask import request, session, redirect, url_for, flash
from functools import wraps
from models.Admin import Admin

def login_required_middleware():
    """Middleware para verificar se o usuário está logado."""
    if 'user_id' not in session:
        return redirect(url_for('login.exibir_formulario'))

def admin_required_middleware(f):
    """Middleware para verificar se o usuário é admin."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login.exibir_formulario'))
        user_id = session['user_id']
        admin = Admin.query.get(user_id)
        if not admin:
            flash('Você não tem permissão para acessar esta página.', 'danger')
            return redirect(url_for('pagina_inicial'))
        return f(*args, **kwargs)
    return decorated_function
