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
@app.route('/teachers/save/<int:id>', methods=['POST'])
def teacher_save(id=None):
    name = request.form['name']
    subject = request.form['subject']
    dao = TeacherDAO()
    result = dao.save(name, subject, id)

    if result["status"] == "ok":
        flash("Registro salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/teachers')

@app.route('/teachers/edit/<int:id>')
def teacher_edit(id):
    dao = TeacherDAO()
    teacher = dao.get_by_id(id)
    return render_template('teachers/form.html', teacher=teacher)

@app.route('/teachers/delete/<int:id>')
def teacher_delete(id):
    dao = TeacherDAO()
    result = dao.delete(id)
    if result['status'] == "ok":
       flash("Registro removido com sucesso!", "success") 
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
@app.route('/courses/save/<int:id>', methods=['POST'])
def course_save(id=None):
    name_course = request.form['name_course']
    duration = request.form['duration']
    dao = CourseDAO()
    result = dao.save(name_course, duration, id)

    if result["status"] == "ok":
        flash("Registro salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/courses')

@app.route('/courses/edit/<int:id>')
def course_edit(id):
    dao = CourseDAO()
    course = dao.get_by_id(id)
    return render_template('courses/form.html', course=course)

@app.route('/courses/delete/<int:id>')
def course_delete(id):
    dao = CourseDAO()
    result = dao.delete(id)
    if result['status'] == "ok":
       flash("Registro removido com sucesso!", "success") 
    else:
        flash(result["mensagem"], "danger")
    return redirect('/courses')

# =========================================== Turma ===========================================

@app.route('/classes') 
def list_classes(): 
    dao = ClassDAO() 
    data = dao.get_all()
    return render_template('classes/classes.html', data=data)

@app.route('/classes/form')
def form_classe():
    daoCourse = CourseDAO() 
    dataCourse = daoCourse.get_all()
    daoTeacher = TeacherDAO()
    dataTeacher = daoTeacher.get_all()
    return render_template('classes/form.html', class_value=None, dataCourse=dataCourse, dataTeacher=dataTeacher)

@app.route('/classes/save/', methods=['POST'])
@app.route('/classes/save/<int:id>', methods=['POST'])
def classe_save(id=None):
    semester = request.form['semester']
    course_id = request.form['course_id']
    teacher_id = request.form['teacher_id']
    dao = ClassDAO()
    result = dao.save(semester, course_id, teacher_id, id)

    if result["status"] == "ok":
        flash("Registro salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/classes')

@app.route('/classes/edit/<int:id>')
def classe_edit(id):
    dao = ClassDAO()
    class_value = dao.get_by_id(id)
    daoCourse = CourseDAO() 
    dataCourse = daoCourse.get_all()
    daoTeacher = TeacherDAO()
    dataTeacher = daoTeacher.get_all()
    return render_template('classes/form.html', class_value=class_value, dataCourse=dataCourse, dataTeacher=dataTeacher)

@app.route('/classes/delete/<int:id>')
def classe_delete(id):
    dao = ClassDAO()
    result = dao.delete(id)
    if result['status'] == "ok":
       flash("Registro removido com sucesso!", "success") 
    else:
        flash(result["mensagem"], "danger")
    return redirect('/classes')

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