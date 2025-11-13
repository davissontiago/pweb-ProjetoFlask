from flask import Flask, render_template, request, redirect, flash
from dao.student_dao import StudentDAO
from dao.teacher_dao import TeacherDAO
from dao.course_dao import CourseDAO
from dao.class_dao import ClassDAO

import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

@app.route('/')
def home():
    return render_template('index.html')

# =========================================== Aluno ===========================================

@app.route('/students') 
def list_students(): 
    dao = StudentDAO() 
    data = dao.get_all()
    return render_template('students/students.html', data=data)

@app.route('/students/form')
def form_students():
    return render_template('students/form.html', student=None)

@app.route('/students/save/', methods=['POST'])
@app.route('/students/save/<int:id>', methods=['POST'])
def student_save(id=None):
    name = request.form['name']
    age = request.form['age']
    city = request.form['city']
    dao = StudentDAO()
    result = dao.save(name, age, city, id)

    if result["status"] == "ok":
        flash("Registro salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/students')

@app.route('/students/edit/<int:id>')
def student_edit(id):
    dao = StudentDAO()
    student = dao.get_by_id(id)
    return render_template('students/form.html', student=student)

@app.route('/students/delete/<int:id>')
def student_delete(id):
    dao = StudentDAO()
    result = dao.delete(id)
    if result['status'] == "ok":
       flash("Registro removido com sucesso!", "success") 
    else:
        flash(result["mensagem"], "danger")
    return redirect('/students')

# =========================================== Professor ===========================================

@app.route('/teachers') 
def list_teachers(): 
    dao = TeacherDAO() 
    data = dao.get_all()
    return render_template('teachers/teachers.html', data=data)


@app.route('/teachers/form')
def form_teacher():
    return render_template('teachers/form.html', teacher=None)

@app.route('/teachers/save/', methods=['POST'])
def teacher_save():
    name = request.form['name']
    subject = request.form['subject']
    dao = TeacherDAO()
    result = dao.save(name, subject)

    if result["status"] == "ok":
        flash("Registro salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/teachers')

# =========================================== Curso ===========================================

@app.route('/courses') 
def list_courses(): 
    dao = CourseDAO() 
    data = dao.get_all()
    return render_template('courses/courses.html', data=data)

@app.route('/courses/form')
def form_course():
    return render_template('courses/form.html', course=None)

@app.route('/courses/save/', methods=['POST'])
def course_save():
    name_course = request.form['name_course']
    duration = request.form['duration']
    dao = CourseDAO()
    result = dao.save(name_course, duration)

    if result["status"] == "ok":
        flash("Registro salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/courses')

# =========================================== Turma ===========================================

@app.route('/classes') 
def list_classes(): 
    dao = ClassDAO() 
    data = dao.get_all()
    return render_template('classes/classes.html', data=data)

# =========================================== Saudação ===========================================

@app.route('/greetings')
def greetings():
    return render_template('greetings/greetings.html')

@app.route('/greetings1/<name>')
def greetings1(name):
    return render_template('greetings/greetings.html', value=name)

@app.route('/greetings2/')
def greetings2():
    name = request.args.get('name')
    return render_template('greetings/greetings.html', value=name)

@app.route('/login', methods=['POST'])
def login():
    user = request.form['user']
    password = request.form['password']
    data = f"Usuário: {user} | Senha: {password}"
    return render_template('greetings/greetings.html', value=data)

# =========================================== Desafios ===========================================

@app.route('/challenge')
def challeng():
    return render_template('challenges/challenge.html')

@app.route('/registration', methods=['POST'])
def registration():
    name = request.form['name']
    birth_date = request.form['birth_date']
    cpf = request.form['cpf']
    name_mother = request.form['name_mother']
    data = f"Nome: {name} | Data Nascimento: {birth_date} | CPF: {cpf} | Noma da Mãe: {name_mother}"
    return render_template('challenges/challenge.html', value=data)

if __name__ == "__main__":
    app.run(debug=True)