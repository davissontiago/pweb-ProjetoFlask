from flask import Flask, render_template
from dao.student_dao import StudentDAO
from dao.teacher_dao import TeacherDAO
from dao.course_dao import CourseDAO
from dao.class_dao import ClassDAO

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/student') 
def list_student(): 
    dao = StudentDAO() 
    lista = dao.get_all()
    return render_template('student/list_student.html', lista=lista)

@app.route('/teacher') 
def list_teacher(): 
    dao = TeacherDAO() 
    lista = dao.get_all()
    return render_template('teacher/list_teacher.html', lista=lista)

@app.route('/course') 
def list_course(): 
    dao = CourseDAO() 
    lista = dao.get_all()
    return render_template('course/list_course.html', lista=lista)

@app.route('/class') 
def list_class(): 
    dao = ClassDAO() 
    lista = dao.get_all()
    return render_template('class/list_class.html', lista=lista)

if __name__ == "__main__":
    app.run(debug=True)