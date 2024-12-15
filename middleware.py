from flask import request, session, redirect, url_for

def login_required_middleware():
    """Middleware para verificar se o usuário está logado."""
    if 'user_id' not in session:
       return redirect(url_for('login.exibir_formulario'))