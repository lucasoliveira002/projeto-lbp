from flask import Blueprint, render_template, request, redirect, url_for

professores_bp = Blueprint('professores', __name__)

#professores pre definidos
teachers = [
    {"name": "Ana", "email": "ana@example.com", "idade": 30, "descricao": "Especialista em Matemática"},
    {"name": "Carlos", "email": "carlos@example.com", "idade": 40, "descricao": "Professor de Física"},
    {"name": "Joana", "email": "joana@example.com", "idade": 35, "descricao": "Professora de Química"},
]

@professores_bp.route('/professores')
def exibir_professores():
    return render_template('professores.html', teachers=teachers)

@professores_bp.route('/add_professores', methods=['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        idade = request.form['idade']
        descricao = request.form['descricao']

        teachers.append({"name": name, "email": email, "idade": int(idade), "descricao": descricao})
        return redirect(url_for('professores.exibir_professores')) 

    return redirect(url_for('professores.add_professores'))
