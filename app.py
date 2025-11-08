from flask import Flask, render_template, request, redirect, flash
from dao.student_dao import StudentDAO
from dao.teacher_dao import TeacherDAO
from dao.course_dao import CourseDAO
from dao.class_dao import ClassDAO

app = Flask(__name__)
app.secret_key = "uma_chave_otima"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/students') 
def list_students(): 
    dao = StudentDAO() 
    data = dao.get_all()
    return render_template('students/students.html', data=data)

@app.route('/students/form')
def form_aluno():
    return render_template('students/form.html', aluno=None)

@app.route('/student/save/', methods=['POST'])
def student_save(id=None):
    name = request.form['name']
    age = request.form['age']
    city = request.form['city']
    dao = AlunoDAO()
    result = dao.save(id, name, age, city)


    if result["status"] == "ok":
        flash("Aluno salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")


    return redirect('/students')


@app.route('/teachers') 
def list_teachers(): 
    dao = TeacherDAO() 
    data = dao.get_all()
    return render_template('teachers/teachers.html', data=data)

@app.route('/courses') 
def list_courses(): 
    dao = CourseDAO() 
    data = dao.get_all()
    return render_template('courses/courses.html', data=data)

@app.route('/classes') 
def list_classes(): 
    dao = ClassDAO() 
    data = dao.get_all()
    return render_template('classes/classes.html', data=data)

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